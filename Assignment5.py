#assignment5
#Samantha I. Kaiser
#National Park Assignment

Display_menu = {
    "1": "View All Parks",
    "2": "View Total Visitors",
    "3": "View Average Visitors",
    "4": "View Estimated Revenue",
    "5": "Exit",
}

Display_parks = [
    {"park": "Redwood Valley", "visitors": 1250, "fee": 20.00},
    {"park": "Silver Lake", "visitors": 980, "fee": 15.00},
    {"park": "Eagle Canyon", "visitors": 1675, "fee": 25.00},
    {"park": "Desert Springs", "visitors": 750, "fee": 10.00},
    {"park": "Pine Ridge", "visitors": 1425, "fee": 18.00},
]


def extract_visitor_counts(parks):
    return [park["visitors"] for park in parks]


def calculate_total_visitors(parks):
    return sum(extract_visitor_counts(parks))


def calculate_average_visitors(parks):
    visitor_counts = extract_visitor_counts(parks)
    return sum(visitor_counts) / len(visitor_counts) if visitor_counts else 0


def calculate_estimated_revenue(parks):
    return sum(park["visitors"] * park["fee"] for park in parks)


def display_menu():
    print("1. View All Parks")
    print("2. View Total Visitors")
    print("3. View Average Visitors")
    print("4. View Estimated Revenue")
    print("5. Exit")


def handle_menu_choice(choice):
    if choice == "1":
        print("\nPark Details:")
        for park in Display_parks:
            print(f"- {park['park']}: {park['visitors']} visitors, ${park['fee']:.2f} fee")
    elif choice == "2":
        print(f"\nTotal Visitors: {calculate_total_visitors(Display_parks):,}")
    elif choice == "3":
        print(f"\nAverage Visitors: {calculate_average_visitors(Display_parks):,.2f}")
    elif choice == "4":
        print(f"\nEstimated Revenue: ${calculate_estimated_revenue(Display_parks):,.2f}")
    elif choice == "5":
        print("\nProgram Exited.")
        return False
    else:
        print("\nInvalid selection. Please choose a valid option.")
    return True


def main():
    display_menu()
    choice = input("\nSelect an option: ").strip()
    while handle_menu_choice(choice):
        display_menu()
        choice = input("\nSelect an option: ").strip()


if __name__ == "__main__":
    main()