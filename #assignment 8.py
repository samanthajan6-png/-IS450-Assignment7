#assignment 8

# Grocery List Application

def display_grocery_list(grocery_list):
    print("\nGrocery List:")
    for item in grocery_list:
        print("- " + item)


# Grocery list with 5 items
grocery_list = [
    "Formula",
    "Toilet Paper",
    "Gum",
    "Shampoo",
    "Orange Juice",
]

# User input
name = input("Enter your name: ")

# Meaningful output with user's name and list
print(f"\nHello, {name}!")
print("Here is your grocery list:")

# Function call
display_grocery_list(grocery_list)
