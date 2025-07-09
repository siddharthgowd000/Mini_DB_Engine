# 🗃️ Mini DB Engine — Python CLI Project

> A fully functional, console-based mini database system built using core Python.  
> Designed to impress placement teams by showcasing practical skills like CRUD logic, file handling, authentication, data validation, timestamping, and more — **without using any external database**!

---

## 🚀 Features

✅ User Authentication (Register & Login)  
✅ Create Tables (with typed fields)  
✅ Insert, View, Update, Delete Records  
✅ Search by any field  
✅ Timestamped entries (`created_at`, `updated_at`)  
✅ JSON-based file storage  
✅ Backup & Restore functionality  
✅ CSV Export  
✅ Unit Testing with `unittest`  
✅ CLI Interface with color-enhanced output via `colorama`

---

## 📁 Project Structure

```
mini_db_engine_beast/
├── auth.py              # Login & Register system
├── backup.py            # Backup and restore logic
├── db_engine.py         # Core DB logic (CRUD, search, validation)
├── main.py              # CLI menu interface
├── utils.py             # File operations, helpers, table printer
├── requirements.txt     # External libraries (colorama)
├── tests/
│   └── test_core.py     # Unit tests for validation
├── data/                # Stores all JSON-based tables & users
└── README.md            # This file
```

---

## 🧑‍💻 How It Works

Each table is saved as a `.json` file in the `/data` directory.  
Data is validated by type (int, float, str, bool) before insertion.  
Users login before accessing DB features, ensuring basic security.

---

## 🛠 Setup & Run

### ✅ Step 1: Install Requirements
```bash
pip install -r requirements.txt
```

### ✅ Step 2: Run the App
```bash
python main.py
```

### ✅ Step 3: Run Tests
```bash
python -m unittest discover tests
```

---

## 📦 Example Table Flow

1. Create a table `students` with fields:
   - name (str)
   - age (int)
   - enrolled (bool)

2. Insert records:
   - name = "Ram", age = 21, enrolled = true

3. View, Update, Search, or Delete entries

4. Export to CSV or Backup anytime

---

## 💡 Tech Used

- Python 3.x
- JSON (for DB storage)
- Colorama (for CLI styling)
- `unittest` (for test cases)

---

## 🌐 Deployment Ideas

While this is a CLI-based app, you can:
- Run it live via [Replit](https://replit.com/@siddharthgowd00/MiniDBEngine)


---

## 🧑‍🎓 Built With ❤️ By

**Siddharth**  
[LinkedIn](https://www.linkedin.com/in/siddharthgowd/) • [GitHub](https://github.com/siddharthgowd)

---

## 📜 License

This project is licensed under the MIT License — use it, modify it, learn from it!
