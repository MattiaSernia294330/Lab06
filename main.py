import flet as ft

from model.model import Model
from UI.view import View
from UI.controller import Controller


def main(page: ft.Page):
    my_model = Model()
    my_view = View(page)
    my_controller = Controller(my_view, my_model)
    my_view.set_controller(my_controller)
    my_view.load_interface()


ft.app(target=main)
#SELECT (SUM(gds.Unit_sale_price *gds.Quantity)) as Total_sales, COUNT(gds.Product_number) as Number_of_sales, COUNT(DISTINCT gds.Retailer_code) AS Number_of_retailers,
    #COUNT(DISTINCT gds.Product_number) AS Number_of_products
#FROM go_daily_sales gds, go_products gp
#where gp.Product_number = gds.Product_number and gds.Retailer_code =(COALESCE (NULL, gds.Retailer_code)) and Year(gds.Date) =COALESCE (NULL, YEAR(gds.`Date`)) and gp.Product_brand = COALESCE (NULL, gp.Product_brand)

