from order import Order

class RegularOrder(Order):
    def calculate_total_price(self):
        return self._sum_items()