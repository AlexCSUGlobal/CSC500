Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> Meal_Purchase = float(input("Enter the charge for the meal purchase: "))
Enter the charge for the meal purchase: 20.00
>>> tip = 0.18 * Meal_Purchase
>>> tax = 0.07 * Meal_Purchase
>>> total_cost = Meal_Purchase + tip + tax
>>> print(f"Meal Purchase: ${Meal_Purchase:.2f}")
Meal Purchase: $20.00
>>> print(f"Tip (18%): ${tip:.2f}")
Tip (18%): $3.60
>>> print(f"Tax (7%): ${tax:.2f}")
Tax (7%): $1.40
>>> print(f"Total Cost: ${total_cost:.2f}")
Total Cost: $25.00
