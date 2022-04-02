import mysql.connector

conexion = mysql.connector.connect(host='localhost',
                                            database='db_diccionario',
                                            user='root',
                                            password='123456')

cursor = conexion.cursor()

ok = True
while ok:
    def porfaFunciona():
            select_query = """select * from palabras order by rand() limit 1"""
            cursor.execute(select_query)
            records = cursor.fetchone()
            print(f"a ver una palabra: {records[1]}")

    porfaFunciona()

    basta = input("cuando quieras salir ingresa A:")
    if basta == "A":
        ok = False
