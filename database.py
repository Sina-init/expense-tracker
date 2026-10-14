import pyodbc

connection=pyodbc.connect(
    "DRIVER={ODBC Driver 18 for SQL Server};"
    "SERVER=.\\SQL2025;"
    "DATABASE=expensetracker;"
    "Trusted_Connection=yes;"
    "TrustServerCertificate=yes;"
)

cursor=connection.cursor()
