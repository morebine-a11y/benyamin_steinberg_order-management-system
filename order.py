from abc import ABC, abstractmethod
from datetime import datetime
from customer import Customer
from order_item import OrderItem
from payment_type import PaymentType

class Order(ABC):
    _used_ids = set()
    def __init__(self, order_id, name, delivery_address, items, customer, payment_type, order_date=None):
        if order_id in Order._used_ids:
            raise ValueError("Order id already exists")

        for value in (name, delivery_address):
            if not isinstance(value, str) or value.strip() == "":
                raise ValueError("Name and address must be non-empty strings")

        if not isinstance(items, list) or len(items) == 0:
            raise ValueError("Items must be a non-empty list")

        for item in items:
            if not isinstance(item, OrderItem):
                raise ValueError("Every item must be an OrderItem")

        ids = [item.item_id for item in items]
        if len(ids) != len(set(ids)):
            raise ValueError("Same item appears twice in this order")

        if not isinstance(customer, Customer):
            raise ValueError("customer must be a Customer")

        if not isinstance(payment_type, PaymentType):
            raise ValueError("payment_type must be a PaymentType")

        if order_date is None:
            order_date = datetime.now()

        self.order_id = order_id
        self.name = name
        self.delivery_address = delivery_address
        self.items = list(items)
        self.customer = customer
        self.payment_type = payment_type
        self.order_date = order_date
        self.total_price = self.calculate_total_price()

        Order._used_ids.add(order_id)
        customer.add_items_to_favorites(items)

    @abstractmethod
    def calculate_total_price(self):
        pass

    def _sum_items(self):
        total = 0
        for item in self.items:
            total += item.price
        return total