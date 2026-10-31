#assignment4- Wolf Pack Coffee Shoppe
#SamanthaKaiser

def display_menu():
    print("\n" + "="*40)
    print("   Wolf Pack Coffee Shoppe Menu")
    print("="*40)
    print("1. Coffee:    $3.99")
    print("2. Latte:     $5.99")
    print("3. Espresso:  $4.99")
    print("="*40 + "\n")

def print_receipt(order, subtotal, discount_amount, subtotal_after_discount, tax, total, qualifies_for_discount):
    receipt_lines = [
        "\n" + "=" * 40,
        "   ORDER SUMMARY",
        "=" * 40,
    ]

    for item, price in order:
        receipt_lines.append(f"{item}: ${price:.2f}")

    receipt_lines.append(f"\nSubtotal: ${subtotal:.2f}")

    if qualifies_for_discount:
        receipt_lines.append(f"Discount (10%): -${discount_amount:.2f}")
        receipt_lines.append(f"Subtotal after discount: ${subtotal_after_discount:.2f}")
    else:
        receipt_lines.append("No discount applied")

    receipt_lines.append(f"Sales Tax (8%): ${tax:.2f}")
    receipt_lines.append(f"Total: ${total:.2f}")
    receipt_lines.append("=" * 40 + "\n")

    return "\n".join(receipt_lines)


def main():
    menu_items = {
        '1': ('Coffee', 3.99),
        '2': ('Latte', 5.99),
        '3': ('Espresso', 4.99)
    }
    sales_tax_rate = 0.08
    discount_rate = 0.10

    order = []

    display_menu()
    while True:
        choice = input("Enter your choice (1-3), 'c' to checkout, or 'q' to quit: ").lower()

        if choice == 'q':
            print("Thank you for visiting Wolf Pack Coffee Shoppe!")
            break
        elif choice == 'c':
            if not order:
                print("Your cart is empty. Please select items first.\n")
                continue

            subtotal = sum(price for item, price in order)
            num_items = len(order)
            qualifies_for_discount = (num_items >= 3) or (subtotal >= 15.00)

            if qualifies_for_discount:
                discount_amount = subtotal * discount_rate
                subtotal_after_discount = subtotal - discount_amount
                tax = subtotal_after_discount * sales_tax_rate
                total = subtotal_after_discount + tax
            else:
                discount_amount = 0.00
                subtotal_after_discount = subtotal
                tax = subtotal * sales_tax_rate
                total = subtotal + tax

            receipt = print_receipt(
                order,
                subtotal,
                discount_amount,
                subtotal_after_discount,
                tax,
                total,
                qualifies_for_discount,
            )
            print(receipt)
            order = []
        elif choice in menu_items:
            item_name, price = menu_items[choice]
            order.append((item_name, price))
            print(f"Added {item_name} (${price:.2f}) to cart. Items in cart: {len(order)}\n")
        else:
            print("Invalid choice. Please try again.")
        print()


if __name__ == "__main__":
    main()

