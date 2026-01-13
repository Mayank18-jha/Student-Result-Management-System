import sqlite3
import os

DB_DIR = "database"
DB_PATH = os.path.join(DB_DIR, "students.db")
os.makedirs(DB_DIR, exist_ok=True)

conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    maths INTEGER,
    science INTEGER,
    english INTEGER,
    total INTEGER,
    percent REAL,
    grade TEXT
)
""")
conn.commit()

def calculate_grade(percent):
    if percent >= 90:
        return "A+"
    elif percent >= 75:
        return "A"
    elif percent >= 60:
        return "B"
    elif percent >= 45:
        return "C"
    else :
        return "Fail"
    
def add_student():
    name = input("Student Name: ")
    maths = int(input("Maths Marks: "))
    science = int(input("Science Marks: "))
    english = int(input("English Marks: "))
    
    total = maths + science + english
    percent = total/3
    grade = calculate_grade(percent)
    cursor.execute("""
    INSERT INTO students (name, maths, science, english, total, percent, grade)
    VALUES (?,?,?,?,?,?,?)""", (name, maths, science, english, total, percent, grade))
    conn.commit()
    print("Student record added!")
    
def view_students():
    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()
    
    print("\nID | Name | Maths | Science | English | Total | % | Grade")
    print("-" * 60)
    for row in rows:
        print(row)
        
def update_marks():
    student_id = int(input("Enter Student ID: "))
    maths = int(input("Maths Marks: "))
    science = int(input("Science Marks: "))
    english = int(input("English Marks: "))
    
    total = maths + science + english
    percent = total/3
    grade = calculate_grade(percent) 
    
    cursor.execute("""
    UPDATE students
    SET maths=?, science=?, english=?, total=?, percent=?, grade=?
    WHERE id=?""",
    (maths, science, english, total, percent, grade, student_id))
    
    conn.commit()
    print("Student record updated!")
    
def menu():
    while True:
        print("""===== Student Result Management System =====
            1. Add Students
            2. View Students
            3. Update Marks
            4. Exit""")
        
        choice = input("Enter choice: ")
        
        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            update_marks()
        elif choice == "4":
            print("Exiting System...")
            break
        else:
            print("Invalid Choice")

menu()
conn.close()