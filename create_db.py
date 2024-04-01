import sqlite3
def create_db():
    conn = sqlite3.connect(database = r"billsystem.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS Employee(Emp_ID INTEGER PRIMARY KEY AUTOINCREMENT, Name text, Email text, Gender text, Contact text, DoB text, DoJ text, Pass text, UserType text, Address text, Salary text)")
    conn.commit()

    cur.execute("CREATE TABLE IF NOT EXISTS Supplier(Invoice_No INTEGER PRIMARY KEY AUTOINCREMENT, Name text, Contact text,  Description text)")
    conn.commit()

    cur.execute("CREATE TABLE IF NOT EXISTS Types(Category_ID INTEGER PRIMARY KEY AUTOINCREMENT, Name text)")
    conn.commit()

    cur.execute("CREATE TABLE IF NOT EXISTS Product(Product_ID INTEGER PRIMARY KEY AUTOINCREMENT,  Supplier text, Type text, Name text, Price text, Kilos text, Status text)")
    conn.commit()

create_db()