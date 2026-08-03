# Punters Data - Database Structure

## Purpose
This document defines the database design required to store racing, sports, betting market and prediction data used by Punters Data.

---

# 1. Horse Racing Database

## Table: Races

Stores information about every race.

Fields:
- Race_ID (unique identifier)
- Date
- Time
- Venue
- Country
- Race_Number
- Distance
- Race_Class
- Track_Condition
- Weather
- Prize_Money

---

## Table: Horses

Stores information about every horse.

Fields:
- Horse_ID
- Horse_Name
- Age
- Sex
- Trainer_ID
- Career_Wins
- Career_Starts
- Win_Percentage
- Place_Percentage

---

## Table: Race Results

Stores individual horse performance in each race.

Fields:
- Result_ID
- Race_ID
- Horse_ID
- Barrier
- Weight
- Jockey_ID
- Finishing_Position
- Margin
- Race_Time
- Sectional_Times
- Starting_Price

---

## Table: Jockeys

Stores jockey information.

Fields:
- Jockey_ID
- Jockey_Name
- Career_Wins
- Strike_Rate
- Track_Performance
- Recent_Form

---

## Table: Trainers

Stores trainer information.

Fields:
- Trainer_ID
- Trainer_Name
- Career_Wins
- Strike_Rate
- Recent_Form
- Track_Performance

---

# 2. Sports Database

## Table: Teams

Fields:
- Team_ID
- Team_Name
- Competition
- Season
- Ranking

---

## Table: Players

Fields:
- Player_ID
- Player_Name
- Team_ID
- Position
- Statistics
- Injury_Status

---

## Table: Matches

Fields:
- Match_ID
- Date
- Competition
- Home_Team
- Away_Team
- Result
- Score

---

# 3. Betting Market Database

## Table: Odds

Stores bookmaker market information.

Fields:
- Odds_ID
- Event_ID
- Bookmaker
- Opening_Odds
- Current_Odds
- Closing_Odds
- Market_Percentage

---

# 4. Prediction Database

## Table: Predictions

Stores Punters Data calculations.

Fields:
- Prediction_ID
- Event_ID
- Selection
- Model_Probability
- True_Odds
- Market_Odds
- Value_Percentage
- Prediction_Result

---

# 5. Performance Tracking

## Table: Model Performance

Measures how accurate Punters Data is.

Fields:
- Prediction_ID
- Predicted_Result
- Actual_Result
- Accuracy
- Profit/Loss
- Return_On_Investment

---

# 6. Relationships

Examples:

Horse → Race Results → Race → Track

Horse → Trainer

Horse → Jockey

Event → Odds → Prediction

Prediction → Result → Model Accuracy

---

# Future Expansion

Database should allow adding:
- AFL
- NRL
- NBA
- NFL
- Soccer
- Cricket
- Tennis
- Greyhound Racing
- Other betting markets
