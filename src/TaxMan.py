class TaxMan: 

    def __init__(self, items, tax):
        self.items = items
        self.tax = float(tax.strip('%'))/100
        self.__total = None

    def calc_total(self):
        total_price =  sum(item['price'] for item in self.items)
        self.__total = total_price + (total_price * self.tax)
        
    
    def get_total(self):
        if self.__total == 0:
            self.calc_total()
        return self.__total 