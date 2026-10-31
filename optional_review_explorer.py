from pathlib import Path

import pandas as pd


df = pd.read_csv("/Users/samanthakaiser/Downloads/YelpReviews.csv")
results_path = Path(__file__).resolve().parent / "search_results.csv"

text_columns = ["review_title", "review_text", "pros", "cons"]
df[text_columns] = df[text_columns].fillna("")
df["searchable_text"] = df[text_columns].agg(" ".join, axis=1).str.strip()

print(f"Number of reviews: {len(df)}")
print(f"Number of columns: {len(df.columns)}")

try:
    keyword = input("Enter a keyword to search reviews: ").strip()
except KeyboardInterrupt:
    print("\nSearch cancelled before a keyword was entered; no results were exported.")
    raise SystemExit(130)
except EOFError:
    print("No interactive input is available. Run this script in a terminal and enter a keyword.")
    raise SystemExit(1)

filtered_df = df[
    df["searchable_text"].str.contains(keyword, case=False, regex=False)
]

print(f"Number of matching reviews: {len(filtered_df)}")
if filtered_df.empty:
    print(f"No reviews matched the keyword '{keyword}'.")
    print("There are no results to export.")
else:
    print(f"Average overall rating: {filtered_df['overall_rating'].mean():.2f}")
    print(f"Highest overall rating: {filtered_df['overall_rating'].max()}")
    print(f"Lowest overall rating: {filtered_df['overall_rating'].min()}")

    display_columns = ["overall_rating", "role", "location", "review_title"]
    print(filtered_df[display_columns].to_string(index=False))

    export_columns = [
        "date",
        "role",
        "location",
        "current_employee",
        "overall_rating",
        "review_title",
        "review_text",
    ]
    new_results = filtered_df[export_columns]
    if results_path.exists():
        existing_results = pd.read_csv(results_path)
        if existing_results.columns.tolist() != export_columns:
            raise ValueError(
                f"{results_path} does not have the expected columns; "
                "please rename or remove it before exporting."
            )
        new_results = pd.concat(
            [existing_results, new_results], ignore_index=True
        ).drop_duplicates()

    new_results.to_csv(results_path, index=False)
    print(f"Added matching reviews to {results_path}.")
