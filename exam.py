#exam 1
#Samantha Kaiser
#October 14, 2026
#Question 1
#Using MAC IOS not windows
#using help with code with my little chat bot

import random
import csv
from itertools import zip_longest
from pathlib import Path


def calculateAverage(listOfNums: list[int | float]) -> float:
    return sum(listOfNums) / len(listOfNums)


print(calculateAverage([1, 2.5, 3.5]))


#Question 2 
#file path in ios not windows

with Path(__file__).with_name("lightSim.txt").open("w") as file:
    for _ in range(1000):
        file.write(f"{random.choice(['red', 'orange', 'green'])}\n")


#Question 3 

csv_path = Path(__file__).parent / "AAAGames.csv"
with csv_path.open(newline="") as file:
    for row in csv.DictReader(file):
        if row["winner"] == "Reno Aces":
            print(row["homeTeam"], row["awayTeam"], row["winner"])



 #Question 4


def getWeather(numberOfDays: int) -> dict[int, str]:
    weather_by_day: dict[int, str] = {}
    for day in range(1, numberOfDays + 1):
        weather_by_day[day] = random.choice(["sunny", "rain", "snow"])
    return weather_by_day


print(getWeather(random.randint(1, 10)))


#Question 5

def getContent(file_path: str | Path) -> list[str]:
    with Path(file_path).open("r", encoding="utf-8") as file:
        return [line.rstrip("\n") for line in file]
content_list = getContent(Path(__file__).with_name("lightSim.txt"))



#Question 6

def listsToCSV(first_list: list[object], second_list: list[object]):
    csv_path = Path(__file__).with_name("output.csv")
    with csv_path.open("w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerows(zip_longest(first_list, second_list, fillvalue=""))


names = ["Sammy", "Tom", "Desiree"]
scores = [92, 72, 82]
listsToCSV(names, scores)
