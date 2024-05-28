import mysql.connector
from database.DB_connect import DBConnect
from model.Retailers import Retailers
class GoRetailersDAO:
    @staticmethod
    def dd_fill_retailers():
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            print("errore connessione")
            return result
        else:
            cursor = cnx.cursor(dictionary=True)
            query = """SELECT gr.*
                FROM go_retailers gr """
            cursor.execute(query)
            for row in cursor:
                result.append(Retailers(row["Retailer_code"],row["Retailer_name"], row["Type"], row["Country"]))
            cursor.close()
            cnx.close()
            return result