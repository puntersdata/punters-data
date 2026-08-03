# Punters Data - First Prediction Model

print("Punters Data prediction engine started")

horse = "Example Horse"

rating = 82

probability = rating / 100

true_odds = 1 / probability

print("Horse:", horse)
print("Rating:", rating)
print("Probability:", probability * 100, "%")
print("True Odds: $", round(true_odds, 2))
