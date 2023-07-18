import pyodbc

class Connection():

    def __init__(self) -> None:
        self.conn = pyodbc.connect("Driver={ODBC Driver 17 for SQL Server};Server=CYBERHIKI\SQLEXPRESS;Database=MEUBANCO;Trusted_Connection=yes;")
    
    def consulta(self, query):
        cursor = self.conn.cursor()
        cursor.execute(query)
        all = cursor.fetchall()
        self.conn.close()
        print(all)
        return all, cursor