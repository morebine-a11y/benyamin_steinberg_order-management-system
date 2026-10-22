from customer import Customer
from customer_type import CustomerType
from order_item import OrderItem
from payment_type import PaymentType
from regular_order import RegularOrder
from vip_order import VIPOrder
from basic_gift import BasicGift
from not_vip_customer_error import NotVipCustomerError


vip = Customer(1, "Dan", "Cohen", "d@x.com", "Haifa", CustomerType.VIP, 0.1)
reg = Customer(2, "Ron", "Levi", "r@x.com", "Tel Aviv", CustomerType.REGULAR)

pen = OrderItem(1, "Pen", 50)
book = OrderItem(2, "Book", 10)
pen2 = OrderItem(3, "Pen", 55)

print("Test 1: VIP total (expect 54.0)")
o1 = VIPOrder(1, "Order A", "Haifa", [pen, book], vip, PaymentType.CASH)
print(o1.total_price)

print("Test 2: Regular total (expect 60)")
o2 = RegularOrder(2, "Order B", "Tel Aviv", [pen, book], reg, PaymentType.CHECK)
print(o2.total_price)

print("Test 3: Regular customer VIP order is blocked")
try:
    VIPOrder(3, "Order C", "Tel Aviv", [pen], reg, PaymentType.CASH)
except NotVipCustomerError as e:
    print("Blocked:", e)

print("Test 4: Favorites after order (expect Pen, Book)")
print([i.name for i in vip.favorite_items])
RegularOrder(4, "Order D", "Haifa", [pen2], vip, PaymentType.OTHER)
print("Same name, different id, not re-added (expect 2):", len(vip.favorite_items))

print("Test 5: Add and remove favorites")
lamp = OrderItem(4, "Lamp", 20)
vip.add_favorite(lamp)
print([i.name for i in vip.favorite_items])
vip.remove_favorite(lamp)
print([i.name for i in vip.favorite_items])

print("Test 6: Gifts")
vip.open_gift()
vip.take_gift(BasicGift())
vip.open_gift()

print("Test 7: Duplicate ids")
try:
    OrderItem(1, "Other", 5)
except ValueError as e:
    print("Item:", e)

try:
    Customer(1, "A", "B", "a@x.com", "X", CustomerType.REGULAR)
except ValueError as e:
    print("Customer:", e)

try:
    RegularOrder(1, "Dup", "X", [lamp], reg, PaymentType.CASH)
except ValueError as e:
    print("Order:", e)