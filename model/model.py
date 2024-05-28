from database.go_daily_sales_DAO import GoDailySalesDAO
from database.go_product_DAO import GoProductDAO
from database.go_retailersDAO import GoRetailersDAO
class Model:
    def __init__(self):
        pass
    def dd_fill_anni(self):
        return GoDailySalesDAO.dd_fill_anni()
    def dd_fill_brands(self):
        return GoProductDAO.dd_fill_brands()
    def dd_fill_retailers(self):
        return GoRetailersDAO.dd_fill_retailers()
    def handle_top_vendite(self,anno, brand,retailer):
        return GoDailySalesDAO.handle_top_vendite(anno, brand,retailer)