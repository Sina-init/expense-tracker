import pyodbc

connection=pyodbc.connect(
    "DRIVER={ODBC Driver 18 for SQL Server};"
    "SERVER=.\\SQL2025;"
    "DATABASE=expensetracker;"
    "Trusted_Connection=yes;"
    "TrustServerCertificate=yes;"
)

print("connected successfully")
cursor=connection.cursor()
cursor.execute("SELECT * FROM expenses")
rows=cursor.fetchall()
for row in rows:
    print(row)