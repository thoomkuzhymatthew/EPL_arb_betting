[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/_SwzfpU1)

# What is the best betting strategy for betting on premier league games?

Authors: Matthew Thoomkuzhy, Leo Liao and Noah Salehi 
---
![projectimage](projectimage.jpg)

## Project Overview 🗂

**We want to figure out what the best betting strategy is for premier league games.**

To do this we want to create a function which backtests different betting strategies on a Sample of historic premier league games. It will have a range of parameters e.g. stake limits, strategy type, start and end dates. 

We will then be using this function to backtest different strategies and track the returns of £100. 

**In order to do this, we need to collect 2 pieces of data:** 

1. Historical odds data for premier league games for the past 5 seasons, we will be collecting this using ['the odds API'](https://the-odds-api.com/)
2. Fixture outcomes for all premier league games for the past 5 seasons, can be found at  ['Premier League Matches'](https://www.football-data.co.uk/englandm.php)

### API Plan
![api_plan](api_plan.png)

Reasons Why We Like Odds API:
1. Access to Real-Time and Historical Odds
2. Offers Odds from Various Bookmakers to Better Investigate Arbitrage Opportunities
3. Data Reliability and Authenticity

---

### Repository Structure
```bash
.
├─ README.md
├─ .gitignore
├─ code
│  ├─ NB-01: Data Collection.ipynb
│  ├─ NB-02: Data Processing.ipynb
│  ├─ NB-03: Visualisation of Simple Betting Strategies.ipynb
│  ├─ NB-04: Visualisation of Arbitrage Betting Strategies.ipynb
│  ├─ auth.py
│  └─ functions.py
└─ data
   ├─ sports_odds.db
   ├─ raw
   │  ├─ historical_odds_data.json
   │  └─ historical_match_data.csv
   └─ visualisations
      ├─ arb_betting_strategies
      └─ simple_betting_strategies
```

## Technical Implementation 💻

### Research Goals
The purpose of this project is to investigate different betting strategies, in order of increasing complexity:
- Betting on Win/Lose/Draws
  - Betting on the Favourite (Lower Odds)
  - Betting on the Underdog (Higher Odds)
  - Betting on the Draw
- Arbitrage
- Biased Arbitrage

### Visualisations
- Line Charts: To observe the growth in our virtual £100 over time across different strategies
- Heatmaps:
   - Visualise the prevalence of arbitrage opportunities across different bookmakers and seasons
   - Visualise the profitability of various strategies across different teams and seasons

## 🛠️ How to Recreate This Project

### 1. Clone the Repository  
Clone this repository to your local machine:  
```bash
git clone git@github.com:lse-ds105/ds105a-2024-project-good_gamblers.git
cd ds105a-2024-project-good_gamblers

```
### 2. Set Up the Python Environment  
Use **conda** or **pyenv** to create and activate the environment.

#### With Conda:  
```bash
conda create -n good-gamblers python=3.9 -y
conda activate good-gamblers
pip install -r requirements.txt
```

#### With Pyenv + Virtualenv:
``` bash
python -m venv .venv
.venv\Scripts\activate # If on Windows
source .venv/bin/activate # If on macOS/Linux
pip install -r requirements.txt
```
### 3. Run the Code  

#### Notebook 1: Data Collection  
Navigate to the `code/` directory and open `NB01 - Data Collection.ipynb`.  
This notebook collects raw data from the Historical Odds API and saves it in the `data/raw/` folder.  

#### Notebook 2: Data Processing  
Run `NB02 - Data Processing.ipynb` to process the raw data and merge it into an SQL database along with historical outcome data.  

#### Notebook 3: Simple Betting Strategies  
Execute `NB03 - Simple Betting Strategies.ipynb` to explore various basic betting strategies and backtest their performance.  

#### Notebook 4: Arbitrage Betting Strategies  
Run `NB04 - Arbitrage Betting Strategies.ipynb` to investigate both biased and unbiased arbitrage betting strategies and backtest them.  

## Acknowledgements  
- **Data Source**: [The Odds API](https://the-odds-api.com/) for providing comprehensive sports betting data.  
- **Libraries Used**: `requests`, `json`, `pandas`, `os`, `SQLAlchemy`, `datetime`, `python-dotenv`, `lets-plot`, `IPython`, `matplotlib`, `seaborn`, `numpy` for data processing, analysis, and visualization.  

---

## Contact  
For questions or feedback, please reach out via GitHub Issues or contribute to this project through pull requests.

