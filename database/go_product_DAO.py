import mysql.connector
from database.DB_connect import DBConnect
class GoProductDAO:
    @staticmethod
    def dd_fill_brands():
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            print("errore connessione")
            return result
        else:
            cursor = cnx.cursor()
            query="""SELECT DISTINCT (gp.Product_brand)
                FROM go_products gp"""
            cursor.execute(query)
            for row in cursor:
                result.append(row[0])
            cursor.close()
            cnx.close()
            return result
