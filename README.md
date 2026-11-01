# BAN701 Python Projects

A collection of independently developed Python assignments and small
command-line programs. The projects practice core programming concepts,
interactive input, calculations, and working with CSV data.

## Initial Features

- **Python basics:** introductory scripts for printing output and practicing
  functions and loops.
- **Login challenge (`assignment2.py`):** a simple username-and-password
  exercise with a three-attempt limit. This is a learning example, not a
  secure authentication system.
- **Booster pack simulator (`Assingment_3.py`):** opens randomized card packs,
  tracks card rarities and values, and reports total spending and profit or
  loss.
- **Coffee shop ordering (`assignment4.py`):** builds an order, applies an
  eligible discount and sales tax, and prints a receipt.
- **National park statistics (`Assignment5.py`):** displays park details and
  calculates visitor totals, averages, and estimated revenue.
- **Restaurant review data (`assignment6.py`, `optional_review_explorer.py`):
  generates sample restaurant ratings from a locations file and searches a
  Yelp review dataset by keyword, with summary statistics and CSV export.
- **File and data exercises (`exam.py`):** calculates an average, generates
  random light and weather data, filters game results, reads text files, and
  writes paired lists to CSV.
- **[Shopping Cart Tracker Project](#shopping-cart-tracker-project) (`main.py`):**
  prompts for items and prices, displays the cart, and applies a 10% discount
  when the subtotal is over $50.
- **Die roll simulation (IS450 Assignment 7):** simulates 20 six-sided die
  rolls and displays their average. The assignment is in the
  [`-IS450-Assignment7`](./-IS450-Assignment7/) subproject.
- **Grocery list (`#assignment 8.py`):** greets the user by name and displays
  a predefined list of five groceries.

Each script is a separate exercise and can be run on its own with Python 3.

## Running a Program

From the project directory, run a script with:

```bash
python3 "main.py"
```

Replace `main.py` with the script you want to run. Some programs prompt for
input in the terminal. The review-data scripts require the relevant input data
files; `optional_review_explorer.py` also requires pandas:

```bash
python3 -m pip install pandas
```

## Shopping Cart Tracker Project

The shopping cart is an interactive Python program for adding priced items and
checking out. It validates empty item names and invalid or negative prices,
displays the cart as items are added, and prints a final itemized receipt.
Subtotals over $50 receive a 10% discount.

Run it from the project directory:

```bash
python3 main.py
```

Enter an item and its price when prompted. Type `done` to check out.

### Source Code

```python
# Main py
# Shopping Cart tracker

# Samantha Kaiser


def calculate_total(cart):
    """Function to calculate total cost and apply a 10% discount if total is over $50."""
    subtotal = sum(cart.values())
    if subtotal > 50:
        discount = subtotal * 0.10
        final_total = subtotal - discount
        discount_applied = True
    else:
        discount = 0
        final_total = subtotal
        discount_applied = False

    return subtotal, discount, final_total, discount_applied


# dictionary: to store items and their prices
shopping_cart = {}

print("Welcome to the Shopping Cart Tracker!")

# loop: a while loop to continuously collect user input
while True:
    item = input("Enter an item to add to your cart (or type 'done' to finish): ")
    if item.lower() == 'done':
        break

    if not item:
        print("Item name cannot be empty. Please try again.")
        continue

    try:
        price = float(input(f"Enter the price for {item}: $"))
    except ValueError:
        print("Invalid price input. Please enter a valid number.")
        continue

    if price < 0:
        print("Price cannot be negative. Please try again.")
        continue

    # updating dictionary with the user's input
    shopping_cart[item] = price

    # loop and meaningful output: to display the items in the cart and their prices
    if shopping_cart:
        print("\n" + "=" * 30)
        print("RECEIPT")
        print("=" * 30)

        for item_name, item_price in shopping_cart.items():
            print(f"- {item_name}: ${item_price:.2f}")

        print("-" * 30)

if not shopping_cart:
    print("Your shopping cart is empty.")
else:
    subtotal, discount, final_total, discount_applied = calculate_total(shopping_cart)
    print("\n" + "=" * 30)
    print("FINAL RECEIPT")
    print("=" * 30)
    for item_name, item_price in shopping_cart.items():
        print(f"- {item_name}: ${item_price:.2f}")
    print(f"Subtotal: ${subtotal:.2f}")
    print(f"Discount: ${discount:.2f}")
    print(f"Final Total: ${final_total:.2f}")
    print(f"Discount applied: {'Yes' if discount_applied else 'No'}")
```

## IS450 Assignment 7

- **Student:** Samantha Kaiser
- **GitHub username:** [@samanthajan6-png](https://github.com/samanthajan6-png)

The program simulates rolling a six-sided die 20 times. It does not require
user input and displays the roll results and their average.

Run the assignment from its directory with:

```bash
cd -- -IS450-Assignment7
python3 program.py
```
