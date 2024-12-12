[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/_SwzfpU1)

# What is the Best Betting Strategy for English Premier League games?

**Authors:** Matthew Thoomkuzhy, Leo Liao and Noah Salehi 
---
![projectimage](https://github.com/user-attachments/assets/b2593057-fafc-4083-866d-2e828eb9d0df)
*Source: OpenAI*

## Project Overview

**We want to figure out what the best betting strategy is for premier league games.**

To do this we want to create a function which backtests different betting strategies on a Sample of historic premier league games.

We will then be using this function to backtest diffrerent strategies and track the returns of 100 pounds 




**In order to do this, we need to collect 2 pieces of data:** 

1. Historical odds data for premier league games for the past 5 seasons, we will be collecting this using ['the odds API'](https://the-odds-api.com/)
2. Fixture outcomes for all premier league games for the past 5 seasons, this can be found at  ['Premier League Matches'](https://www.football-data.co.uk/englandm.php)

*our project chronology:*
---
![chron](https://github.com/user-attachments/assets/3bf9b4bd-188f-4a70-9a60-4df0c13747cc)
---

sport	event_id	event_name	bookie_team1	bookie_team2	bookie_draw	odds_team1	odds_team2	odds_draw	arbitrage_profit_margin	commence_time
30	soccer_spl	1b4b38cffca35329314cee0e01c22f26	St Mirren vs Motherwell	Coral	Betfair	Betfair	2.00	4.70	3.55	0.554390	2024-12-07 15:00:00+00:00


## Technical Implementation

##### Research Goals
The purpose of this project is to investigate different betting strategies, in order of increasing complexity:
- Betting on Win/Lose/Draws
  - Betting on the Favourite (Lower Odds)
  - Betting on the Underdog (Higher Odds)
  - Betting on the Draw
- Arbitrage
- Biased Arbitrage
- Positive Expected Value (EV) Betting

##### Target Visualisations


##### Data Collection and Aggregation
As mentioned in the Project Overview, the historical odds and match results will be collected from the Odds API and a supplementary dataset from Kaggle. This is because the historical odds data from Odds API does not contain the match results to analyse the profitability of our strategy.

In line with the course's coding philosophy, we have decided to create our very own `fixture_id` so that the historical odds and results can be merged efficiently. 

The format will be as such:
`XXXYYYddmmyy`, where `XXX` and `YYY` are the 3-letter abbreviations of the home and away teams respectively. `ddmmyy` is the date of the match itself. This ensures that each match has a unique `fixture_id` and the data can be merged accurately.

##### Mock Data
| sport | event_id        | event_name               | bookie_team1 | bookie_team2 | bookie_draw | odds_team1 | odds_team2 | odds_draw | arbitrage_profit_margin | commence_time               |
|-------|-----------------|--------------------------|--------------|--------------|-------------|------------|------------|-----------|-------------------------|-----------------------------|
| 30    | soccer_spl      | 1b4b38cffca35329314cee0e01c22f26 | St Mirren vs Motherwell | Coral        | Betfair      | Betfair     | 2.00       | 4.70       | 3.55      | 0.554390                | 2024-12-07 15:00:00+00:00 |



## Work Distribution


## Risks, Mitigants and Backup Plans
