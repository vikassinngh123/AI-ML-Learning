# 02. Object-Oriented Programming (OOP)

This folder contains projects and exercises dedicated to mastering **Object-Oriented Programming (OOP)** principles in Python, progressing from basic class structures to modular, production-ready application architectures.

---

## 📂 Projects Directory

### 1. 💼 Employee Management System (`employee_management.py`)
* **Concepts Covered:** Classes, Objects, Instance Methods, Input Validation.
* **Description:** A foundational script to handle, update, and manage employee records dynamically within a clean console interface.

### 2. 📚 Library Management System (`library_system/`)
A production-style modular application split cleanly using the **Separation of Concerns** design pattern into backend domain logic and an interactive user-facing layout.

* **`library_models.py` (The Backend):** Houses the core logical structures of the system using advanced OOP concepts:
    * **Composition:** The master `Library` class directly acts as a container holding and coordinating `Book` and `Member` objects via fast dictionary lookups.
    * **Inheritance & Polymorphism:** Extends the standard `Member` base class to create a specialized `PremiumMember` class that automatically overrides default book borrowing limits.
    * **Encapsulation:** Self-contained state validation methods like `mark_as_borrowed()` and `can_borrow()` protect internal class attributes from invalid updates.
* **`main.py` (The Frontend / UI):** The application entry point managing the command-line admin menu. It captures terminal text inputs and feeds them seamlessly into the backend objects.

---

## 🚀 How to Run the Projects

To test any of these terminal dashboards locally, navigate to this directory in your terminal and run the execution command:

```bash
# To run the Employee Management system:
python employee_management.py

# To run the Modular Library Management system:
cd library_system
python main.py
