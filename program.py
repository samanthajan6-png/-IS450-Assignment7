import random


def main() -> None:
    results = []

    for roll_number in range(1, 21):
        result = random.randint(1, 6)
        results.append(result)
        print(f"Roll {roll_number}: {result}")

    print(f"Results: {results}")
    average = sum(results) / len(results)
    print(f"Average: {average:.2f}")


if __name__ == "__main__":
    main()
