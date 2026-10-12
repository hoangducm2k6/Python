import sqlite3

# 1. Kết nối database
conn = sqlite3.connect("university.db")
cursor = conn.cursor()

# 2. Tạo bảng students
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    major TEXT,
    gpa REAL
)
""")

# Xóa dữ liệu cũ để tránh bị lặp khi chạy lại
cursor.execute("DELETE FROM students")

# 3. Thêm dữ liệu (ít nhất 5 sinh viên)
students_data = [
    ("An", "CNTT", 3.5),
    ("Anh", "Điện tử số", 2.8),
    ("Toan", "Ngôn ngữ Anh", 3.9),
    ("Dũng", "Toán rời rạc", 1.9),
    ("Minh", "Python", 3.2)
]

cursor.executemany(
    "INSERT INTO students (name, major, gpa) VALUES (?, ?, ?)",
    students_data
)

conn.commit()

# 4. Truy vấn tất cả sinh viên
print("Danh sách tất cả sinh viên:")
cursor.execute("SELECT * FROM students")
rows = cursor.fetchall()
for row in rows:
    print(row)

# 5. Truy vấn sinh viên GPA > 3.0
print("\nSinh viên có GPA > 3.0:")
cursor.execute("SELECT * FROM students WHERE gpa > 3.0")
rows = cursor.fetchall()
for row in rows:
    print(row)

# 6. Cập nhật GPA của Anh
cursor.execute(
    "UPDATE students SET gpa = ? WHERE name = ?",
    (3.7, "Anh")
)
conn.commit()

print("\nSau khi cập nhật GPA của Anh:")
cursor.execute("SELECT * FROM students")
rows = cursor.fetchall()
for row in rows:
    print(row)

# 7. Xóa sinh viên GPA < 2.0
cursor.execute("DELETE FROM students WHERE gpa < 2.0")
conn.commit()

print("\nSau khi xóa sinh viên GPA < 2.0:")
cursor.execute("SELECT * FROM students")
rows = cursor.fetchall()
for row in rows:
    print(row)

# 8. Đóng kết nối
conn.close()