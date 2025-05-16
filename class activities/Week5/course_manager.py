from database import create_connection
import sqlite3
def insert_course(name, unit):
    conn = create_connection()
    cursor=conn.cursor()
    try:
        cursor.execute("INSERT INTO course (name, unit) VALUES (?, ?)", (name, unit))
        conn.commit()
        print(f"Course '{name}' inserted successfully.")
    except sqlite3.IntegrityError:
        print("Error")
    conn.close()

def search_course(keyword):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM course WHERE id = ? OR name LIKE ?", (keyword, f"%{keyword}%"))
    results = cursor.fetchall()
    if results:
        print(" Course(s) found:")
        for row in results:
            print(f"ID: {row[0]}, Name: {row[1]}, Unit: {row[2]}")
    else:
        print("No course found with that ID or name.")
    conn.close()
    