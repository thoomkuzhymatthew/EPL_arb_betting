[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/_SwzfpU1)

# Wanna Outsmart the Bookies This EPL Season? Aight, Bet!

##### **Authors:** Matthew Thoomkuzhy, Xinyan Liao and Noah Salehi
##### **Research Question:** What is the Best Betting Strategy for English Premier League games?
---
![projectimage](https://github.com/user-attachments/assets/b2593057-fafc-4083-866d-2e828eb9d0df)
*Source: OpenAI*

## Project Overview

**We want to figure out what the best betting strategy is for premier league games.**

To do this we want to create a function which backtests different betting strategies on a Sample of historic premier league games.

We will then be using this function to backtest different strategies and track the returns of 100 pounds 




**In order to do this, we need to collect 2 pieces of data:** 

1. Historical odds data for premier league games for the past 5 seasons, we will be collecting this using ['the odds API'](https://the-odds-api.com/)
2. Fixture outcomes for all premier league games for the past 5 seasons, this can be found at  ['Premier League Matches'](https://www.football-data.co.uk/englandm.php)

*our project chronology:*
---
![chron](https://github.com/user-attachments/assets/3bf9b4bd-188f-4a70-9a60-4df0c13747cc)
---

## Technical Implementation

### Research Goals
The purpose of this project is to investigate different betting strategies, in order of increasing complexity:
- Betting on Win/Lose/Draws
  - Betting on the Favourite (Lower Odds)
  - Betting on the Underdog (Higher Odds)
  - Betting on the Draw
- Arbitrage
- Biased Arbitrage
- Positive Expected Value (EV) Betting

### Target Visualisations
- Line Charts
- Heatmaps

### Mock Data

Historical Odds Data
| sport | event_id        | event_name               | bookie_team1 | bookie_team2 | bookie_draw | odds_team1 | odds_team2 | odds_draw | arbitrage_profit_margin | commence_time               |
|-------|-----------------|--------------------------|--------------|--------------|-------------|------------|------------|-----------|-------------------------|-----------------------------|
| 30    | soccer_spl      | 1b4b38cffca35329314cee0e01c22f26 | St Mirren vs Motherwell | Coral        | Betfair      | Betfair     | 2.00       | 4.70       | 3.55      | 0.554390                | 2024-12-07 15:00:00+00:00 |

Historical Match Data
| Div | Date       | Time  | HomeTeam   | AwayTeam | FTHG | FTAG | FTR |
|-----|------------|-------|------------|----------|------|------|-----|
| E0  | 16/08/2024 | 20:00 | Man United | Fulham   | 1    | 0    | H   |

Here we can see that `FTR` stands for the full-time result, and *H* means that the home team had won.

### Data Aggregation
In line with the course's coding philosophy, we have decided to create our very own `fixture_id` so that the historical odds and results can be merged efficiently. 

The format will be as such:
`XXXYYYddmmyy`, where `XXX` and `YYY` are the 3-letter abbreviations of the home and away teams respectively. `ddmmyy` is the date of the match itself. This ensures that each match has a unique `fixture_id` and the data can be merged accurately.

The two dataframes will then be stored in an SQLite Database which feeds into the individual analyses for each of the strategies.

## Work Distribution

NB-01: Data Collection (All Members)

NB-02: Data Processing (All Members)

NB-03: Analysis of Simple Win/Lose/Draw Strategies (Xinyan)

NB-04: Analysis of Arbitrage and Biased Arbitrage Strategies (Matthew)

NB-05: Analysis of Positive Expected Value Strategy (Noah)

## Risks, Mitigants and Backup Plans

### Risks:

1. **API Data Limitations**: The Odds API or Premier League data source may have rate limits, missing data, or restricted access, which could prevent complete data collection.
2. **Merging Dataset Error**: Issues with our custom `fixture_id` system may lead to incorrect merging of odds and match outcomes, skewing the analysis results.
3. **Strategy Biases**: Betting strategies may perform well on historical data but fail to generalize due to market inefficiencies or changes in team dynamics.

### Mitigants:

1. We will test the APIs early to understand their limitations and, if necessary, pre-download data to mitigate rate limits or access restrictions.
2. Our custom `fixture_id` will undergo rigorous testing with sample datasets to ensure accuracy before full-scale implementation.
3. We will evaluate strategies under realistic assumptions, such as fluctuating odds, betting limits, and varying market conditions, to reduce reliance on idealized results.

### Backup Plans:
If access to the APIs fails, we will source alternative datasets, such as publicly available odds and results archives. For merging issues, we will manually validate a subset of the data to ensure the system works before scaling. If time becomes a constraint, we will prioritize simpler strategies like betting on favorites or underdogs to deliver meaningful insights within the timeline.

---
