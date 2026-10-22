from customer import Customer
from customer_type import CustomerType
from order_item import OrderItem
from payment_type import PaymentType
from regular_order import RegularOrder
from vip_order import VIPOrder
from not_vip_customer_error import NotVipCustomerError


vip = Customer(1, "Dan", "Cohen", "d@x.com", "Haifa", CustomerType.VIP, 0.1)
reg = Customer(2, "Ron", "Levi", "r@x.com", "Tel Aviv", CustomerType.REGULAR)

pen = OrderItem(1, "Pen", 50)
book = OrderItem(2, "Book", 10)

o1 = VIPOrder(1, "Order A", "Haifa", [pen, book], vip, PaymentType.CASH)
print(o1.total_price)

o2 = RegularOrder(2, "Order B", "Tel Aviv", [pen, book], reg, PaymentType.CHECK)
print(o2.total_price)

try:
    VIPOrder(3, "Order C", "Tel Aviv", [pen], reg, PaymentType.CASH)
except NotVipCustomerError as e:
    print("Blocked:", e)

print(len(vip.favorite_items))