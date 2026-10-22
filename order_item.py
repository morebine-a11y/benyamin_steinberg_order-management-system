class OrderItem:
    _used_ids = set()

    def __init__(self, item_id, name, price):
        if item_id in OrderItem._used_ids:
            raise ValueError("Item id already exists")

        if not isinstance(name, str) or name.strip() == "":
            raise ValueError("Item name must be a non-empty string")

        if not isinstance(price, (int, float)) or price < 0:
            raise ValueError("Item price must be a non-negative number")

        self.item_id = item_id
        self.name = name
        self.price = price

        OrderItem._used_ids.add(item_id)

