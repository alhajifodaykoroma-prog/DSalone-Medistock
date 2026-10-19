DSalone MediStock

Medicine Stock and Dispensing Tracker

A simple Python Object-Oriented Programming project for managing medicine stock and basic dispensing operations in a health facility.

Project Information

- Project Name: DSalone MediStock
- Course: PROG211 – Object-Oriented Programming 1
- Domain: Health
- Programming Language: Python
- Application Type: Command-Line Application
- Academic Year: 2026/2027

1. Introduction

DSalone MediStock is an educational project developed using Python. It demonstrates how Object-Oriented Programming concepts can be applied to a basic medicine stock management problem.

The application allows users to view registered medicines, add stock, dispense medicine, search for medicine records, and view stock status.

2. Problem Being Addressed

Health facilities need to monitor available medicine quantities. Without regularly updated records, it may be difficult to identify low-stock medicines or determine whether enough stock is available for dispensing.

DSalone MediStock demonstrates a simple computerized approach to recording medicine information and performing basic stock operations.

3. Main Objectives

The project aims to:

1. Create and manage medicine objects.
2. Store multiple medicine objects in a Python list.
3. Add medicine stock.
4. Dispense medicine when sufficient stock is available.
5. Search for medicines by ID.
6. Display medicine details and stock status.
7. Demonstrate instance, class, and static methods.
8. Demonstrate interaction between objects.
9. Consider Digital Public Good principles.

4. Main Classes

Medicine

Represents a medicine and contains its ID, name, category, quantity, and reorder level.

HealthFacility

Represents the health facility and maintains a list of Medicine objects.

StockTransaction

Represents stock operations of type "ADD" or "DISPENSE".

MediStockSystem

Controls the main menu and connects the user to the system operations.

5. Object-Oriented Programming Concepts

The project demonstrates:

- Classes and objects
- Attributes
- Instance methods
- A class method
- A static method
- Object interaction
- A Python list for storing multiple Medicine objects

The class method is "Medicine.basic_medicine()". The static method is "Medicine.check_quantity()".

6. Main Features

- View registered medicines
- Add medicine stock
- Dispense medicine
- Search for a medicine
- Display medicine quantities
- Identify available, low-stock, and out-of-stock medicines
- Display transaction results

7. Data Structure

The project uses a Python list in the "HealthFacility" class:

self.medicines = []

Medicine objects are added to the list using:

self.medicines.append(medicine)

The list allows the facility to store and search through multiple Medicine objects.

8. Sample Medicine Records

The demonstration program includes these sample medicines:

Medicine ID| Medicine| Category| Initial Quantity
MED001| Paracetamol| Pain Relief| 100
MED002| Amoxicillin| Antibiotic| 50
MED003| Oral Rehydration Salts| General| 30

These are example records used to demonstrate the application.

9. Requirements

You need:

- Python 3
- Visual Studio Code or another Python editor
- Git, if you want to clone the repository

The current version does not require external Python packages.

10. Installation and Running

Step 1: Clone the repository

git clone https://github.com/alhajifodaykoroma/DSalone-MediStock.git

Step 2: Enter the project directory

cd DSalone-MediStock

Step 3: Run the application

python main.py

If your system uses "python3", run:

python3 main.py

11. Main Menu

The program displays the following menu:

==============================
       DSALONE MEDISTOCK
==============================
1. View Medicines
2. Add Stock
3. Dispense Medicine
4. Search Medicine
5. Exit

Enter the number corresponding to the operation you want to perform.

12. Example Transaction

For example, if Paracetamol has 100 units and the user dispenses 30 units, the resulting quantity is 70.

Transaction ID: TXN1
Medicine: Paracetamol
Type: DISPENSE
Quantity: 30
Status: Successful
Remaining Stock: 70

This is an illustrative example. Actual transaction IDs depend on the operations performed during the program run.

13. Testing

The following operations should be tested before submission:

Test| Expected Result
View medicines| Registered medicines displayed
Add stock| Quantity increases
Dispense stock| Quantity decreases
Search medicine| Medicine information displayed
Search unknown ID| Medicine not found
Enter invalid quantity| Operation rejected
Reach reorder level| Low Stock displayed
Reach zero stock| Out of Stock displayed
Exit| Program terminates

14. Digital Public Good Considerations

Open Source

The source code can be shared through a public GitHub repository with an appropriate open-source license.

Privacy

The system focuses on medicine and facility information and does not require patient medical records.

Accessibility

The program uses a simple command-line menu.

Modularity

The program separates medicine information, facility management, stock transactions, and the main application into different classes.

15. Privacy

The project uses sample demonstration data. It is not intended to store sensitive patient information or serve as a production healthcare system.

16. Project Structure

DSalone-MediStock/
├── main.py
├── README.md
├── LICENSE
├── .gitignore
├── screenshots/
│   ├── 01_main_menu.png
│   ├── 02_inventory.png
│   ├── 03_add_stock.png
│   ├── 04_dispense_medicine.png
│   ├── 05_search_medicine.png
│   └── 06_low_stock.png
└── documentation/
    └── DSalone_MediStock_Report.pdf

17. Limitations

The current educational version does not include:

- Database storage
- User authentication
- Patient records
- Medicine expiry tracking
- SMS or email notifications
- Barcode scanning
- Online synchronization
- Web or mobile interfaces

Medicine records are kept in memory while the program is running and are not automatically saved between separate runs.

18. Future Improvements

Future versions could include database integration, user accounts, expiry-date tracking, stock history, automated alerts, multiple health facilities, a graphical interface, and secure data backup.

19. Author

Alhaji Foday Koroma

Bachelor of Science in Software Engineering with Multimedia

Limkokwing University of Creative Technology, Sierra Leone

20. License

This project is released under the MIT License. See the "LICENSE" file for details.

21. Conclusion

DSalone MediStock demonstrates the application of Python Object-Oriented Programming to a basic health-related problem. It focuses on classes, objects, methods, object interaction, a Python list, and basic medicine stock operations.