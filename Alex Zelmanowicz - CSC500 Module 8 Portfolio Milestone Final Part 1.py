Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> class ItemToPurchase:
...     def __init__(self):
...         self.item_name = "none"
...         self.item_price = 0.0
...         self.item_quantity = 0
...     def print_item_cost(self):
...         print(f"{self.item_name} {self.item_quantity} @ ${self.item_price} = ${self.item_quantity * self.item_price}")
... 
...         
>>> notebooks = ItemToPurchase()
>>> notebooks.item_name = "Notebook"
>>> notebooks.item_price = 3.0
>>> notebooks.item_quantity = 10
>>> notebooks.print_item_cost()
Notebook 10 @ $3.0 = $30.0
