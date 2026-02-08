import sqlite3

try:
    with sqlite3.connect("data.db") as conn:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS students (
                name TEXT,
                class TEXT,
                marks INTEGER,
                company TEXT
            )
        """)
        
        data = [
            ("Ravi", "CSE", 85, "Google"),
            ("Anu", "ECE", 78, "Amazon"),
            ("Sita", "CSE", 92, "Microsoft"),
            ("Kiran", "IT", 88, "Infosys"),
            ("Rahul", "ECE", 69, "TCS")
        ]
        cursor.executemany("INSERT INTO students VALUES (?,?,?,?)", data)
        print(f"{cursor.rowcount} rows inserted.")
except sqlite3.Error as e:
    print(f"Error: {e}")
print("Database created successfully")