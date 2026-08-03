# Punters Data - First Prediction Model

import csv

print("Punters Data prediction engine started")

with open("../../Data/raw/race_results.csv") as file:
    races = csv.DictReader(file)

    for horse in races:

        rating = (
            float(horse["Recent_Form"]) * 0.5 +
            float(horse["Jockey_Rating"]) * 0.25 +
            float(horse["Trainer_Rating"]) * 0.25
        )

        probability = rating / 100
        true_odds = 1 / probability

        print("----------------")
        print("Horse:", horse["Horse"])
        print("Rating:", round(rating,2))
        print("Probability:", round(probability*100,2), "%")
        print("True Odds: $", round(true_odds,2))
