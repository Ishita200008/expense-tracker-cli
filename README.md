# 💰 Expense Tracker CLI

A simple and modular command-line based Expense Tracker application built using Python.  
This project allows users to record, track, and analyze expenses using JSON file storage.

---

## 📌 Project Overview

Expense Tracker CLI is a beginner-to-intermediate level Python project that demonstrates:

- File handling with JSON
- Modular function design
- Date parsing using datetime
- CLI menu handling
- Error handling using try-except
- Git & GitHub workflow

---

## 🚀 Features

✅ Add new expenses  
✅ View month-wise expense summary  
✅ Filter expenses by category  
✅ View category-wise summary  
✅ Persistent storage using JSON  
✅ Input validation and error handling  

---

## 🛠 Technologies Used

- Python 3
- JSON
- datetime module
- Git
- GitHub

---

## 📂 Project Structure

```
expense-tracker-cli/
│
├── app.py
├── expense.json
├── .gitignore
└── README.md
```

---

## ▶️ How to Run the Project

1. Clone the repository:

```bash
git clone https://github.com/yourusername/expense-tracker-cli.git
```

2. Navigate into the project folder:

```bash
cd expense-tracker-cli
```

3. Run the program:

```bash
python main.py
```

---

## 🧠 How It Works

- All expenses are stored in a JSON file (`expense.json`)
- Each expense contains:
  - Amount
  - Category
  - Date (DD/MM/YYYY)
- Monthly summaries are calculated dynamically
- Category summaries aggregate expense totals

---

## 📊 Sample Expense Format (JSON)

```json
{
    "amount": 500,
    "category": "Food",
    "date": "27/06/2023"
}
```

---

## ⚠️ Input Rules

- Date format must be: `DD/MM/YYYY`
- Amount must be numeric
- Category is case-insensitive when filtering

---

## 🔮 Future Improvements

- Add CSV export functionality
- Add sorting by date
- Add delete/edit expense feature
- Convert to OOP structure
- Add unit tests
- Build FastAPI backend version
- Deploy web version

---

## 👩‍💻 Author

**Ishita Pinto**

---
git add README.md
git commit -m "Added professional README file"
git push
