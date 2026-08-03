# Punters Data - Model Testing

## Purpose

This document defines how the Punters Data prediction model will be tested, measured and improved.

The goal is to determine whether Punters Data can accurately predict outcomes and identify value opportunities compared with available market odds.

---

# 1. Testing Method

The model will be tested using historical data where:

- Past events are analysed
- Predictions are generated
- Predictions are compared against actual results
- Accuracy and profitability are measured

---

# 2. Back Testing

Back testing will use historical races and sporting events.

Process:

1. Load historical data
2. Run prediction model
3. Generate probability predictions
4. Calculate true odds
5. Compare predictions against actual outcomes
6. Record results

---

# 3. Accuracy Measurements

The model will track:

## Prediction Accuracy

Measures how often the model correctly predicts winners.

Example:

Predictions made: 100

Correct predictions: 35

Accuracy: 35%

---

## Probability Accuracy

Measures whether predicted percentages match actual results.

Example:

Model predicts:

100 horses with a 30% winning chance

Expected winners:

30

Actual winners:

28

The model is performing close to expectation.

---

# 4. Value Testing

The model will compare:

Punters Data True Odds

against

Available Market Odds

Example:

Horse:
Example Horse

Punters Data Probability:
30%

Punters Data True Odds:
$3.33

Bookmaker Odds:
$5.00

Value:
YES

---

# 5. Profit and Loss Testing

The system will track:

- Starting bank
- Bets placed
- Winning bets
- Losing bets
- Total profit/loss
- Return on investment (ROI)

Example:

Starting Bank: $1,000

Total Bets: 100

Final Bank: $1,120

ROI: +12%

---

# 6. Model Performance Tracking

Each prediction should record:

- Date
- Event
- Selection
- Predicted probability
- True odds
- Market odds
- Result
- Profit/loss

---

# 7. Improving the Model

The model will be improved by:

- Adding more historical data
- Testing new variables
- Adjusting weighting factors
- Removing inaccurate data
- Comparing different algorithms

---

# 8. Testing Goals

Initial goals:

Phase 1:
- Build basic prediction model
- Test with historical data

Phase 2:
- Improve accuracy
- Identify value opportunities

Phase 3:
- Compare performance against market

Phase 4:
- Automate daily predictions

---

# Future Testing

Future testing may include:

- Machine learning validation
- Multiple sports testing
- Live prediction testing
- Long-term profitability analysis
