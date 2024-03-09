Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> class ItemToPurchase:
...     def __init__(self):
...         self.item_name = "none"
...         self.item_price = 0.0
...         self.item_quantity = 0
... 
...     def print_item_cost(self):
...         print(f"{self.item_name} {self.item_quantity} @ ${self.item_price} = ${self.item_quantity * self.item_price}")
... 
...     
>>> item1 = ItemToPurchase()
>>> item1.item_name = input("Item name: ")
Item name: Peanut Butter
>>> item1.item_price = float(input("Item price: "))
Item price: 3.00
>>> item1.item_quantity = int(input("item quantity: "))
item quantity: 10
>>> item2 = ItemToPurchase()
>>> item2.item_name = input("Item name: ")
Item name: Jelly
>>> item2.item_price = float(input("Item price: "))
Item price: 2.00
>>> item2.item_quantity = int(input("item quantity: "))
item quantity: 20
