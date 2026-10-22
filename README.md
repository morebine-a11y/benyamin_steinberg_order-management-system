# Order Management System

A Python OOP project that manages customer orders. It supports regular orders and VIP orders, customers with favorite items and gifts, and system-wide unique IDs.

How to run

Open a terminal in the project folder and run: python main.py

main.py demonstrates every feature and prints labeled results.

Files

Each class is in its own file: payment_type.py, customer_type.py, not_vip_customer_error.py, gift.py, basic_gift.py, order_item.py, customer.py, order.py, regular_order.py, vip_order.py, and main.py (the demonstration).

Design decisions
Discounts are fractions between 0 and 1. For example, 0.1 means 10% off. A discount of None means no discount.
Order IDs, item IDs, and customer IDs are each unique across the whole system. Creating a duplicate raises a ValueError.
An item ID cannot appear twice in the same order.
Favorite items are matched by name, so two items with the same name but different IDs count as the same favorite.
Removing a favorite that is not in the list does nothing.
Order and Gift are abstract classes. RegularOrder and VIPOrder implement calculate_total_price, and BasicGift implements open_gift.
A VIP order for a customer who is not VIP raises NotVipCustomerError. The check runs before the order ID is reserved and before the customer's favorites change, so a failed order leaves no trace.
Input is validated before any ID is registered, so a failed constructor does not reserve an ID.