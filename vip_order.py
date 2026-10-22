from order import Order
from customer_type import CustomerType
from not_vip_customer_error import NotVipCustomerError

class VIPOrder(Order):
    def calculate_total_price(self):
        if self.customer.customer_type != CustomerType.VIP:
            raise NotVipCustomerError("Customer is not a VIP customer")

        discount = self.customer.discount
        if discount is None:
            discount = 0

        return self._sum_items() * (1 - discount)