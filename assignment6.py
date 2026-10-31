# Samantha Kaiser
# Description: Assignment 6 - Restaurant Review Dataset Generator

import csv
import random
import re
from pathlib import Path

random.seed(42)

base_dir = Path("/Users/samanthakaiser/Desktop/BAN701")
input_file = base_dir / "locations.txt"
output_file = base_dir / "restaurant_reviews.csv"

restaurant_names = [
    "Maple Grove Grill", "Luna Bistro", "Cedar Street Cafe", "Sunset Diner", "Harbor House",
    "Rosewood Kitchen", "Bluebird Tavern", "Oak & Vine", "Golden Fork", "City Lights Eatery",
    "Riverbend Grill", "Elm & Spice", "Pine & Pepper", "Twilight Table", "North Star Cafe",
    "Cranberry Creek", "Amber Lantern", "Hearth & Harvest", "Silver Spoon", "Willow Branch",
    "Riverside Bistro", "Stonefire Grill", "Copper Pot", "Bayside Diner", "Sunflower Kitchen",
    "Maple & Co.", "The Velvet Fork", "Red Lantern", "Autumn Harvest", "Cinder & Co.",
    "Pearl Street Cafe", "Main Street Grill", "Bloom & Barrel", "Midnight Mingle", "Field & Fire",
    "The Green Table", "Old Town Eatery", "Parkview Bistro", "Crimson Vine", "Morning Dew Cafe",
    "Cedar & Pine", "Harvest Moon", "Fireside Grill", "Lakeside Cafe", "The Orchard Room",
    "The Rustic Spoon", "Sunny Side Kitchen", "Beacon Bistro", "Hollow Oak", "Maple Lane Grill"
]

cities = []
with input_file.open("r", encoding="utf-8") as infile:
    for line in infile:
        line = line.strip()
        if not line:
            continue

        parts = [part.strip() for part in line.split(" - ")]
        if len(parts) < 3:
            continue

        city = parts[0]
        state_field = parts[1]

        state_match = re.match(r"^(.*?)(?:\s+\(([^)]+)\))?$", state_field)
        if state_match:
            state_name = state_match.group(1).strip()
        else:
            state_name = state_field

        cities.append((city, state_name))

with output_file.open("w", newline="", encoding="utf-8") as outfile:
    writer = csv.writer(outfile)
    writer.writerow(["Restaurant", "City", "State", "Rating"])

    selected_restaurants = random.sample(restaurant_names, 50)
    selected_cities = random.choices(cities, k=50)
    total_restaurants = 0
    rating_total = 0.0
    high_rated_count = 0

    for restaurant, (city, state) in zip(selected_restaurants, selected_cities):
        rating = f"{random.uniform(1.0, 5.0):.1f}"
        writer.writerow([restaurant, city, state, rating])
        numeric_rating = float(rating)
        total_restaurants += 1
        rating_total += numeric_rating
        if numeric_rating >= 4.0:
            high_rated_count += 1

average_rating = rating_total / total_restaurants if total_restaurants else 0.0
print(f"Created {output_file}")
print("Dataset Summary:")
print(f"Restaurants created: {total_restaurants}")
print(f"Average rating: {average_rating:.1f}")
print(f"Restaurants rated 4.0 or higher: {high_rated_count}")
