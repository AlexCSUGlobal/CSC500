Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
class ItemToPurchase:
    def __init__(self, item_name="none", item_price=0.0, item_quantity=0, description=""):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity
        self.description = description

    def print_item_cost(self):
        print(f"{self.description} {self.item_name} {self.item_quantity} @ ${self.item_price:.2f} = ${self.item_quantity * self.item_price:.2f}")

        
class ShoppingCart:
    def __init__(self, customer_name="none", current_date="January 1, 2020"):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = []

    def add_item(self, item):
        self.cart_items.append(item)

    def remove_item(self, item_name):
        removed = False
        for item in self.cart_items:
            if item.item_name == item_name:
                self.cart_items.remove(item)
                removed = True
                break
        if not removed:
            print("Item not found in cart. Nothing removed.")

    def modify_item(self, new_item):
        modified = False
        for item in self.cart_items:
            if item.item_name == new_item.item_name:
                if new_item.item_price != 0.0:
                    item.item_price = new_item.item_price
                if new_item.item_quantity != 0:
                    item.item_quantity = new_item.item_quantity
                modified = True
                break
        if not modified:
            print("Item not found in cart. Nothing modified.")

    def get_num_items_in_cart(self):
        return sum(item.item_quantity for item in self.cart_items)

    def get_cost_of_cart(self):
        return sum(item.item_price * item.item_quantity for item in self.cart_items)

    def print_total(self):
        total_cost = self.get_cost_of_cart()
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        if self.cart_items:
            print(f"Number of Items: {self.get_num_items_in_cart()}")
            for item in self.cart_items:
                item.print_item_cost()
            print(f"Total: ${total_cost:.2f}")
        else:
            print("SHOPPING CART IS EMPTY")

    def print_descriptions(self):
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print("Item Descriptions:")
        for item in self.cart_items:
            print(f"{item.description} {item.item_name}: {item.item_quantity} @ ${item.item_price:.2f}")

            
johns_cart = ShoppingCart("John Doe", "February 1, 2020")
items = [ItemToPurchase("Peanut Butter", 3.00, 2, "Crunchy"), ItemToPurchase("Jelly", 2.00, 2, "Strawberry"), ItemToPurchase("Chocolate Spread", 4.00, 2, "Nutella")]
for item in items:
    johns_cart.add_item(item)

    
def print_menu(cart):
    while True:
        print("\nMENU")
        menu_options = {'a': "Add item to cart",
            'r': "Remove item from cart",
            'c': "Change item quantity",
            'i': "Output items' descriptions",
            'o': "Output shopping cart",
            'q': "Quit"}
        for key, value in menu_options.items():
            print(f"{key} - {value}")

        choice = input("Choose option: ").lower()

        if choice in menu_options:
            if choice == 'a':
                item_name = input("Item name: ")
                item_price = float(input("Item price: "))
                item_quantity = int(input("Item quantity: "))
                item_description = input("Item description: ")
                item_to_purchase = ItemToPurchase(item_name, item_price, item_quantity, item_description)
                cart.add_item(item_to_purchase)
...             elif choice == 'r':
...                 item_name = input("Item to remove: ")
...                 cart.remove_item(item_name)
...             elif choice == 'c':
...                 item_name = input("Item name to modify: ")
...                 new_quantity = int(input("New quantity: "))
...                 new_price = float(input("New price: "))
...                 new_description = input("New description: ")
...                 modified_item = ItemToPurchase(item_name, new_price, new_quantity, new_description)
...                 cart.modify_item(modified_item)
...             elif choice == 'i':
...                 cart.print_descriptions()
...             elif choice == 'o':
...                 cart.print_total()
...             elif choice == 'q':
...                 print("Ending program.")
...                 break
...         else:
...             print("Error. Please choose again.")
... 
...             
>>> def main():
...     johns_cart = ShoppingCart("John Doe", "February 1, 2020")
... 
...     
>>> if __name__ == "__main__":
...     main()
... 
...     
>>> print_menu(johns_cart)

MENU
a - Add item to cart
r - Remove item from cart
c - Change item quantity
i - Output items' descriptions
o - Output shopping cart
q - Quit
