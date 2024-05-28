from dataclasses import dataclass
from datetime import date
@dataclass
class Daily_Sales:
    Retailer_code:str
    Product_number:str
    Order_method_code:str
    Date:date
    Quantity:int
    Unit_Price:float
    Unit_sale_price:int
    Ricavo:float
    def __eq__(self, other):
        return self.Retailer_code == other.Retailer_code, self.Product_number == other.Product_number, self.Order_method_code==other.Order_method_code
    def __hash__(self):
        return hash(self.Retailer_code)
    def __str__(self):
        return f"Data {self.Date} Ricavo {self.Ricavo} retailer {self.Retailer_code} product {self.Product_number}"