# 💰 Expense Tracker CLI

A modular, file-based command-line Expense Tracker built using Python.

This project demonstrates core backend development concepts including:
- File handling
- JSON data persistence
- Input validation
- Date parsing
- Aggregation logic
- CLI menu design
- Git workflow

---

# 📌 Project Objective

The goal of this project is to build a fully functional expense tracking system that:

- Stores user data persistently
- Allows structured data retrieval
- Performs aggregation (monthly & category-wise)
- Handles invalid input gracefully
- Follows clean modular design

This project simulates how backend systems manage structured financial data.

---

# 🧠 System Design Overview

The application follows a modular function-based architecture.

Main Flow:

1. Program starts
2. Displays CLI menu
3. User selects operation
4. Data is loaded from JSON
5. Operation is performed
6. Data is saved back (if modified)

Data is stored locally in a JSON file to simulate database persistence.

---

# 📂 Required Files

Below are the essential files needed for this project:

---

## 1️⃣ main.py

This is the core application file.

It contains:

- File initialization logic
- load_data() → reads JSON file
- save_data() → writes to JSON file
- Adding_Expense() → adds new expense
- view_expense() → monthly summary
- filter_by_category() → category filter
- category_summary() → grouped totals
- CLI menu loop
- Exception handling

This file controls the entire application.

---

## 2️⃣ expense.json

This file acts as a lightweight database.

It stores all expense records in list format:

```json
[
    {
        "amount": 500,
        "category": "Food",
        "date": "27/06/2023"
    }
]
```

If the file does not exist, it is automatically created.

This ensures persistent storage across runs.

---

## 3️⃣ .gitignore

Prevents unnecessary or sensitive files from being pushed to GitHub.

Recommended contents:

```
__pycache__/
*.pyc
venv/
expense.json
```

This ensures:
- No cache files are committed
- No local virtual environments are committed
- No personal expense data is made public

---

## 4️⃣ README.md

Project documentation file.

Explains:
- Purpose
- Features
- How to run
- Architecture
- Future improvements

---

# 🏗 Functional Modules Breakdown

---

## 🔹 1. Adding Expense

- Takes user input
- Validates amount
- Validates date format (DD/MM/YYYY)
- Appends expense to JSON file

---

## 🔹 2. View Expense (Monthly Summary)

- Reads all expense entries
- Converts date string → datetime object
- Extracts month
- Aggregates totals per month
- Displays overall total

Uses dictionary-based aggregation logic.

---

## 🔹 3. Filter by Category

- Takes category input
- Performs case-insensitive comparison
- Displays matching expenses
- Handles "no result" scenario

---

## 🔹 4. Category Summary

- Groups expenses by category
- Uses dictionary to accumulate totals
- Prints category-wise totals

---

# ⚙️ Technical Concepts Demonstrated

This project demonstrates understanding of:

- JSON file handling
- Data serialization
- Dictionary aggregation patterns
- datetime.strptime()
- Exception handling
- CLI interaction loops
- match-case (Python 3.10+)
- Git initialization & push workflow

---

# ▶️ How to Run

Clone repository:

```bash
git clone https://github.com/yourusername/expense-tracker-cli.git
```

Navigate into folder:

```bash
cd expense-tracker-cli
```

Run:

```bash
python main.py
```

---

# 🔮 Future Improvements

To evolve this into a production-level system:

- Add edit/delete expense functionality
- Add sorting by date
- Add CSV export
- Add logging module
- Convert to OOP design
- Add unit tests (pytest)
- Build FastAPI REST API version
- Add database (SQLite)
- Deploy web interface

---

# 👩‍💻 Author

Ishita Pinto

---

# ⭐ Why This Project Matters

This project moves beyond basic Python scripts.

It demonstrates:
- Structured thinking
- Data persistence
- Clean architecture
- Git workflow
- Real-world application logic

It serves as a foundation for backend development and API-based systems.



expense-tracker-cli/
│
├── app.py
├── .gitignore
├── README.md
└── expense.json (optional, usually ignored)
