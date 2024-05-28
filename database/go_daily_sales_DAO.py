import mysql.connector
from database.DB_connect import DBConnect
from model.Daily_Sales import Daily_Sales
class GoDailySalesDAO:
    @staticmethod
    def dd_fill_anni():
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            print("errore connessione")
            return result
        else:
            cursor = cnx.cursor()
            query="""SELECT DISTINCT (YEAR(gds.Date))
                FROM go_daily_sales gds """
            cursor.execute(query)
            for row in cursor:
                result.append(row[0])
            cursor.close()
            cnx.close()
            return result
    @staticmethod
    def handle_top_vendite(anno, brand,retailer):
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            print("errore connessione")
            return result
        else:
            cursor = cnx.cursor(dictionary=True)
            query= """SELECT gds.*
                FROM go_daily_sales gds, go_products gp 
                where gp.Product_number = gds.Product_number and gds.Retailer_code =(COALESCE (%s, Retailer_code)) and Year(gds.Date) =COALESCE (%s, YEAR(gds.`Date`)) and gp.Product_brand = COALESCE (%s, gp.Product_brand)"""
            cursor.execute(query, [retailer, anno, brand])
            for row in cursor:
                result.append(Daily_Sales(row["Retailer_code"], row["Product_number"], row["Order_method_code"], row["Date"], row["Quantity"], row["Unit_price"], row["Unit_sale_price"],row["Unit_sale_price"]*row["Quantity"]))
            cursor.close()
            cnx.close()
            return result