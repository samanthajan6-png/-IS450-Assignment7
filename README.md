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
- **Shopping cart tracker (`main.py`):** collects item prices and calculates
  a 10% discount when the cart total exceeds $50.
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

## IS450 Assignment 7

- **Student:** Samantha Kaiser
- **GitHub:** [@samanthajan6-png](https://github.com/samanthajan6-png)

The program simulates rolling a six-sided die 20 times and calculates the
average result. It does not require user input.

Run the assignment from its directory with:

```bash
cd -- -IS450-Assignment7
python3 program.py
```
