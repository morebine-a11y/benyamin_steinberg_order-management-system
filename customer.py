from customer_type import CustomerType
from gift import Gift
from order_item import OrderItem


class Customer:
    _used_ids = set()

    def __init__(
        self,
        customer_id,
        first_name,
        last_name,
        email,
        delivery_address,
        customer_type,
        discount=None,
        gift=None
    ):
        if customer_id in Customer._used_ids:
            raise ValueError("Customer id already exists")

        for value in (first_name, last_name, email, delivery_address):
            if not isinstance(value, str) or value.strip() == "":
                raise ValueError(
                    "Name, email and address must be non-empty strings"
                )

        if not isinstance(customer_type, CustomerType):
            raise ValueError("customer_type must be a CustomerType")

        if discount is not None and (
            not isinstance(discount, (int, float))
            or discount < 0
            or discount > 1
        ):
            raise ValueError("Discount must be None or between 0 and 1")

        if gift is not None and not isinstance(gift, Gift):
            raise ValueError("gift must be a Gift or None")

        self.customer_id = customer_id
        self.first_name = first_name
        self.last_name = last_name
        self.email =  email
        self.delivery_address = delivery_address
        self.customer_type = customer_type
        self.discount = discount
        self.gift = gift

        self.favorite_items = []

        Customer._used_ids.add(customer_id)

    def add_favorite(self, item):
        if not isinstance(item, OrderItem):
            raise ValueError("item must be an OrderItem")

        for existing in self.favorite_items:
            if existing.name == item.name:
                return

        self.favorite_items.append(item)

    def remove_favorite(self, item):
        for existing in self.favorite_items:
            if existing.name == item.name:
                self.favorite_items.remove(existing)
                return

    def add_items_to_favorites(self, items):
        for x in items:
            self.add_favorite(x)

    def take_gift(self, gift):
        if not isinstance(gift, Gift):
            raise ValueError("gift must be a Gift")

        self.gift = gift

    def open_gift(self):
        if self.gift is None:
            print("No gift")
            return

        self.gift.open_gift()