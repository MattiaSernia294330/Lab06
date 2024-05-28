from dataclasses import dataclass
@dataclass
class Retailers:
    Retailer_code:str
    Retailer_name:str
    Type:str
    Country:str
    def __eq__(self, other):
        return self.Retailer_code == other.Retailer_code
    def __hash__(self):
        return hash(self.Retailer_code)
    def __str__(self):
        return f"{self.Retailer_name}"