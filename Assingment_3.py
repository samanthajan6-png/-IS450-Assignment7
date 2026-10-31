#Samantha
# Description: Assignment 3 - Booster Pack Opener

import random

pack_cost = 4.50
common_value = 0.10
uncommon_value = 0.50
rare_value = 1.00
ultra_rare_value = 5.00

common_count = 0
uncommon_count = 0
rare_count = 0
ultra_rare_count = 0

# Get user input with validation
while True:
    try:
        num_packs = int(input("How many booster packs would you like to open? "))
        if num_packs <= 0:
            print("Error: Please enter a valid number.")
        else:
            break
    except ValueError:
        print("Error: Please enter a valid integer.")

continue_program = True
while continue_program:
    loop_count = 0
    while loop_count < num_packs:
        loop_count += 1
        print(f"\nOpening pack {loop_count}...")
        pack_contents = [None] * 5
        
        # Determine if pack has an ultra rare (1% chance - roll 1-100)
        ultra_rare_roll = random.randint(1, 100)
        has_ultra_rare = ultra_rare_roll == 1

       

        # Place ultra rare if it exists
        if has_ultra_rare:
            ultra_rare_position = random.randint(0, 4)
            pack_contents[ultra_rare_position] = "Ultra Rare"
            ultra_rare_count += 1
            print("*** ULTRA RARE PULLED ***")
        
        # Place exactly 1 rare card in a random position
        while True:
            rare_position = random.randint(0, 4)
            if pack_contents[rare_position] is None:
                pack_contents[rare_position] = "Rare"
                rare_count += 1
                break
        
        # Fill remaining slots with Common/Uncommon
        for i in range(5):
            if pack_contents[i] is None:
                card_type = random.choices(
                    ["Common", "Uncommon"],
                    weights=[77.5, 22.5],
                    k=1
                )[0]
                pack_contents[i] = card_type
                if card_type == "Common":
                    common_count += 1
                elif card_type == "Uncommon":
                    uncommon_count += 1

        print("Pack contents:", ", ".join(pack_contents))

    # Ask user if they want to continue
    while True:
        response = input("\nWould you like to open more packs? (yes/no): ").lower()
        if response in ["yes", "y"]:
            while True:
                try:
                    additional_packs = int(input("How many more packs would you like to open? "))
                    if additional_packs <= 0:
                        print("Error: Please enter a valid number.")
                    else:
                        num_packs += additional_packs
                        break
                except ValueError:
                    print("Error: Please enter a valid integer.")
            break
        elif response in ["no", "n"]:
            continue_program = False
            break
        else:
            print("Please enter 'yes' or 'no'.")

# Display final statistics
print("\n=== Final Statistics ===")
print(f"Total packs opened: {num_packs}")
print(f"\nCards Collected:")
print(f"Common cards: {common_count} x ${common_value} = ${common_count * common_value:.2f}")
print(f"Uncommon cards: {uncommon_count} x ${uncommon_value} = ${uncommon_count * uncommon_value:.2f}")
print(f"Rare cards: {rare_count} x ${rare_value} = ${rare_count * rare_value:.2f}")
print(f"Ultra Rare cards: {ultra_rare_count} x ${ultra_rare_value} = ${ultra_rare_count * ultra_rare_value:.2f}")

total_spent = num_packs * pack_cost
total_value = (common_count * common_value + uncommon_count * uncommon_value + 
               rare_count * rare_value + ultra_rare_count * ultra_rare_value)

print(f"\nTotal value of cards: ${total_value:.2f}")
print(f"Total spent on packs: ${total_spent:.2f}")
print(f"Profit/Loss: ${total_value - total_spent:.2f}")
print("Thank you for playing!")