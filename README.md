# 🧮 Python Calculator Project

---

![Elvates Lab Header](images/header.png)

---

## 📘 Project Documentation

### **Project Title:** Calculator Using Python  
This is a command-line based calculator built using Python.  
It performs basic arithmetic operations such as **Addition**, **Subtraction**, **Multiplication**, and **Division**.  
The program includes input validation and error handling (like division by zero).

---

## 🧑‍💻 Code Implementation

```python
def add(a,b):
    return a + b

def subtract(a,b):
    return a - b

def multiply(a,b):
    return a * b

def divide(a,b):
    if b == 0:
        raise ZeroDivisionError("Can't Divide by zero.")
    return a / b

def get_number(prompt):
    while True:
        s = input(prompt).strip()
        try:
            return float(s)
        except ValueError:
            print("Invalid number. Please Enter a Valid Numeric Integer.")

def main():
    menu = (
        "\nSelect operation:\n"
        "1) Add (+)\n"
        "2) Subtract (-)\n"
        "3) Multiply (*)\n"
        "4) Divide (/)\n"
        "5) Exit\n"
        "Enter choice (1-5): "
    )

    ops = {
        "1": ("+", add),
        "2": ("-", subtract),
        "3": ("*", multiply),
        "4": ("/", divide),
    }

    while True:
        choice = input(menu).strip()
        if choice == "5" or choice.lower() in ("q", "quit", "exit", "leave"):
            print("Good Bye & Thanks for using the calculator.")
            break
        if choice not in ops:
            print("Invlaid Choice. Choose between 1-5.")
            continue

        a = get_number("Enter First Number: ")
        b = get_number("Enter Second Number: ")
        symbol, func = ops[choice]
        try:
            result = func(a, b)
        except ZeroDivisionError as e:
            print("Error:", e)
        else:
            def fmt(x):
                return int(x) if x.is_integer() else x
            print(f"{fmt(a)} {symbol} {fmt(b)} = {fmt(result)}")

if __name__ == "__main__":
    main()
```

---

## 🖥️ Output Screenshot

![Calculator Output](84dd7a92-1b24-44b2-b7a9-3a54b84bf2c7.png)

---

## 💡 Interview Questions & Answers

### 1. What is normalization?
Normalization is a process of organizing the columns and tables of a relational database to minimize data redundancy and improve data integrity.

### 2. Explain primary vs foreign key.
- **Primary Key:** A column or a group of columns that uniquely identifies every row in a table. It cannot contain NULL values.  
- **Foreign Key:** A column or group of columns that refers to the primary key in another table, creating a link between the two.

### 3. What are constraints?
Constraints are rules enforced on data columns to maintain accuracy and reliability of data. Examples include **NOT NULL**, **UNIQUE**, **PRIMARY KEY**, and **FOREIGN KEY**.

### 4. What is a surrogate key?
A surrogate key is an artificial key assigned to a row, usually an auto-incremented integer, used for unique identification.

### 5. How do you avoid data redundancy?
By using normalization, which splits large tables into smaller related ones to ensure data is stored only once.

### 6. What is an ER diagram?
An ER (Entity-Relationship) Diagram visually represents the structure of a database — showing entities, attributes, and their relationships.

### 7. What are the types of relationships in DBMS?
1. One-to-One (1:1)  
2. One-to-Many (1:M)  
3. Many-to-Many (M:N)

### 8. Explain the purpose of AUTO_INCREMENT.
AUTO_INCREMENT automatically generates a unique number for new rows in a table, often used for Primary Keys.

### 9. What is the default storage engine in MySQL?
The default storage engine is **InnoDB** (since MySQL 5.5.5).

### 10. What is a composite key?
A composite (or compound) key combines two or more columns to uniquely identify each row in a table.

---

## 🗂️ Repository Contents
- `calculator.py` → Source code  
- `README.md` → Project documentation  
- `elvates_header.png` → Header image  
- `output.png` → Screenshot of calculator output  

---

## 🧑‍🏫 Author
**Prathamesh Sitaram Warak**  
B.E. Information Technology | Atharva College of Engineering  
Passionate about coding, cybersecurity, and building real-world tech projects.
