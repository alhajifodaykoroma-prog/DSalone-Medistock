# DSALONE MEDISTOCK
# Medicine Stock & Dispensing Tracker

# CLASS 1: MEDICINE

class Medicine:

    def __init__(self, medicine_id, name, category, quantity, reorder_level):
        self.medicine_id = medicine_id
        self.name = name
        self.category = category
        self.quantity = quantity
        self.reorder_level = reorder_level

    # STATIC METHOD

    @staticmethod
    def validate_quantity(quantity):
        """
        Checks whether a quantity is a valid non-negative integer.
        """
        return isinstance(quantity, int) and quantity >= 0

    # CLASS METHOD

    @classmethod
    def create_basic(cls, medicine_id, name):
        """
        Creates a basic medicine using standard default values.
        """
        return cls(
            medicine_id,
            name,
            "General",
            0,
            10
        )

    # INSTANCE METHOD
    def add_stock(self, amount):
        """
        Adds stock to the medicine.
        """
        if not self.validate_quantity(amount) or amount == 0:
            return False

        self.quantity += amount
        return True


    # INSTANCE METHOD

    def dispense(self, amount):
        """
        Removes stock when medicine is dispensed.
        """
        if not self.validate_quantity(amount) or amount == 0:
            return False

        if amount > self.quantity:
            return False

        self.quantity -= amount
        return True


    # INSTANCE METHOD

    def is_low_stock(self):
        """
        Checks whether the medicine has reached its
        reorder level.
        """
        return self.quantity <= self.reorder_level

    
    # INSTANCE METHOD

    def get_status(self):
        """
        Returns the current stock status.
        """
        if self.quantity == 0:
            return "OUT OF STOCK"

        if self.is_low_stock():
            return "LOW STOCK"

        return "IN STOCK"


    # INSTANCE METHOD

    def display_info(self):
        """
        Displays complete information about the medicine.
        """
        print("-" * 55)
        print(f"Medicine ID   : {self.medicine_id}")
        print(f"Name          : {self.name}")
        print(f"Category      : {self.category}")
        print(f"Quantity      : {self.quantity}")
        print(f"Reorder Level : {self.reorder_level}")
        print(f"Status        : {self.get_status()}")
        print("-" * 55)



# CLASS 2: HEALTH FACILITY

class HealthFacility:

    def __init__(self, facility_id, name, location):
        self.facility_id = facility_id
        self.name = name
        self.location = location

        self.medicines = []
 
    def add_medicine(self, medicine):
        """
        Adds a Medicine object to the facility's inventory.
        """
        if not isinstance(medicine, Medicine):
            return False

        if self.find_medicine(medicine.medicine_id) is not None:
            return False

        self.medicines.append(medicine)
        return True


    # INSTANCE METHOD

    def find_medicine(self, medicine_id):
        """
        Searches the medicine list using the medicine ID.
        """
        for medicine in self.medicines:

            if medicine.medicine_id.upper() == medicine_id.upper():
                return medicine

        return None

    
    # INSTANCE METHOD

    def display_medicines(self):
        """
        Displays all medicines registered at the facility.
        """
        if not self.medicines:
            print("\nNo medicines are currently registered.")
            return

        print("\n" + "=" * 55)
        print(f"{self.name} - MEDICINE INVENTORY")
        print("=" * 55)

        for medicine in self.medicines:
            medicine.display_info()



# CLASS 3: STOCK TRANSACTION

class StockTransaction:

    # Class attribute used to generate transaction IDs.
    next_id = 1

    def __init__(self, medicine, transaction_type, quantity):

        self.transaction_id = (
            f"TXN{StockTransaction.next_id:03d}"
        )

        StockTransaction.next_id += 1

        self.medicine = medicine
        self.transaction_type = transaction_type.upper()
        self.quantity = quantity
        self.success = False


    # INSTANCE METHOD

    def process(self):
        """
        Processes either an ADD or DISPENSE transaction.
        """

        if self.transaction_type == "ADD":

            self.success = self.medicine.add_stock(
                self.quantity
            )

        elif self.transaction_type == "DISPENSE":

            self.success = self.medicine.dispense(
                self.quantity
            )

        return self.success

    
    # INSTANCE METHOD

    def display_receipt(self):
        """
        Displays the result of a stock transaction.
        """

        print("\n" + "=" * 55)
        print("              STOCK TRANSACTION")
        print("=" * 55)

        print(f"Transaction ID : {self.transaction_id}")
        print(f"Type           : {self.transaction_type}")
        print(f"Medicine       : {self.medicine.name}")
        print(f"Quantity       : {self.quantity}")

        if self.success:
            status = "SUCCESS"
        else:
            status = "FAILED"

        print(f"Status         : {status}")
        print(f"Remaining Stock: {self.medicine.quantity}")

        print("=" * 55)



# CLASS 4: DSALONE MEDISTOCK SYSTEM

class MediStockSystem:

    def __init__(self, facility):

        self.system_name = "DSalone MediStock"
        self.facility = facility


    # INSTANCE METHOD
    
    def register_medicine(self, medicine):
        """
        Registers a Medicine object with the facility.
        """
        return self.facility.add_medicine(medicine)

    
    # INSTANCE METHOD

    def find_medicine(self, medicine_id):
        """
        Finds a medicine through the health facility.
        """
        return self.facility.find_medicine(medicine_id)

    
    # INSTANCE METHOD
    
    def show_inventory(self):
        """
        Displays the facility's complete inventory.
        """
        self.facility.display_medicines()

    
    # INSTANCE METHOD

    def add_stock(self, medicine_id, quantity):
        """
        Creates and processes an ADD stock transaction.
        """

        medicine = self.find_medicine(medicine_id)

        if medicine is None:
            print("\nMedicine not found.")
            return

        transaction = StockTransaction(
            medicine,
            "ADD",
            quantity
        )

        transaction.process()
        transaction.display_receipt()


    # INSTANCE METHOD

    def dispense_medicine(self, medicine_id, quantity):
        """
        Creates and processes a DISPENSE transaction.
        """

        medicine = self.find_medicine(medicine_id)

        if medicine is None:
            print("\nMedicine not found.")
            return

        transaction = StockTransaction(
            medicine,
            "DISPENSE",
            quantity
        )

        transaction.process()
        transaction.display_receipt()


    # INSTANCE METHOD
    
    def get_quantity(self, prompt):
        """
        Safely receives a positive whole-number quantity.
        """

        try:

            quantity = int(input(prompt).strip())

            if Medicine.validate_quantity(quantity) and quantity > 0:
                return quantity

            print("\nQuantity must be a positive whole number.")

        except ValueError:

            print("\nPlease enter a valid whole number.")

        return None


    # INSTANCE METHOD

    def register_from_input(self):
        """
        Collects medicine information from the user
        and registers a new Medicine object.
        """

        medicine_id = input(
            "Enter Medicine ID: "
        ).strip().upper()

        name = input(
            "Enter medicine name: "
        ).strip()

        category = input(
            "Enter category: "
        ).strip()

        if not medicine_id or not name or not category:
            print("\nAll fields are required.")
            return

        if self.find_medicine(medicine_id):
            print("\nA medicine with that ID already exists.")
            return

        quantity = self.get_quantity(
            "Enter opening stock: "
        )

        if quantity is None:
            return

        reorder_level = self.get_quantity(
            "Enter reorder level: "
        )

        if reorder_level is None:
            return

        medicine = Medicine(
            medicine_id,
            name,
            category,
            quantity,
            reorder_level
        )

        if self.register_medicine(medicine):

            print(
                f"\n{name} registered successfully."
            )

        else:

            print(
                "\nMedicine could not be registered."
            )


    # INSTANCE METHOD

    def run_menu(self):
        """
        Runs the main application menu.
        """

        while True:

            print("\n" + "=" * 55)
            print("              DSALONE MEDISTOCK")
            print("       Medicine Stock & Dispensing Tracker")
            print("=" * 55)

            print(f"Facility: {self.facility.name}")
            print(f"Location: {self.facility.location}")

            print("\n1. View Inventory")
            print("2. Register Medicine")
            print("3. Add Stock")
            print("4. Dispense Medicine")
            print("5. Search Medicine")
            print("6. Exit")

            print("=" * 55)

            choice = input(
                "Enter your choice: "
            ).strip()

            
            # VIEW INVENTORY
            
            if choice == "1":

                self.show_inventory()


            # REGISTER MEDICINE
            
            elif choice == "2":

                self.register_from_input()

            
            # ADD STOCK
            
            elif choice == "3":

                medicine_id = input(
                    "Enter Medicine ID: "
                ).strip()

                quantity = self.get_quantity(
                    "Enter quantity to add: "
                )

                if quantity is not None:

                    self.add_stock(
                        medicine_id,
                        quantity
                    )

            
            # DISPENSE MEDICINE
            
            elif choice == "4":

                medicine_id = input(
                    "Enter Medicine ID: "
                ).strip()

                quantity = self.get_quantity(
                    "Enter quantity to dispense: "
                )

                if quantity is not None:

                    self.dispense_medicine(
                        medicine_id,
                        quantity
                    )

            
            # SEARCH MEDICINE
        
            elif choice == "5":

                medicine_id = input(
                    "Enter Medicine ID: "
                ).strip()

                medicine = self.find_medicine(
                    medicine_id
                )

                if medicine:

                    medicine.display_info()

                else:

                    print("\nMedicine not found.")

            
            # EXIT
            
            elif choice == "6":

                print(
                    "\nThank you for using DSalone MediStock."
                )

                break

            
            # INVALID OPTION
            
            else:

                print(
                    "\nInvalid choice. Please select 1-6."
                )



# SAMPLE DATA

def load_sample_data(system):
    """
    Creates sample Medicine objects for demonstration
    and testing purposes.
    """

    paracetamol = Medicine(
        "MED001",
        "Paracetamol",
        "Pain Relief",
        100,
        20
    )

    amoxicillin = Medicine(
        "MED002",
        "Amoxicillin",
        "Antibiotic",
        50,
        10
    )

    # Demonstrates the class method.
    ors = Medicine.create_basic(
        "MED003",
        "Oral Rehydration Salts"
    )

    # Add initial stock to the ORS object.
    ors.add_stock(30)

    # Register all Medicine objects with the facility.
    system.register_medicine(paracetamol)
    system.register_medicine(amoxicillin)
    system.register_medicine(ors)



# PROGRAM START


if __name__ == "__main__":

    # Create HealthFacility object.
    facility = HealthFacility(
        "HF001",
        "Freetown Community Health Centre",
        "Freetown, Sierra Leone"
    )

    # Create MediStockSystem object.
    system = MediStockSystem(facility)

    # Load sample Medicine objects.
    load_sample_data(system)

    # Start the application.
    system.run_menu()