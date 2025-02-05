---
title: "About"
layout: default
---

<link rel="stylesheet" type="text/css" href="./assets/css/style.css">

<div class="header">
    <a href="index.html">Home</a>
    <a href="about.html">About</a>
    <a href="eda.html">Exploratory Data Analysis</a>
    <a href="backtesting.html">Backtesting</a>
</div>

## Project Objectives
- Analyze sports betting odds to identify arbitrage opportunities
- Identify potential inefficiencies in odds pricing that are exploitable
- Incorporate these findings into backtesting both simple directional betting and arbitrage betting strategies

Finally, we aim to synthesize the findings from these objectives to inform us on what the best betting strategy in the English Premier League is.

## Research Areas  

We explore three main areas in our project:  

### 1. Simple Directional Strategies  
These involve placing bets based on an expected match outcome. To uncover potential **alpha**, we analyze **odds mispricing** in both home and away teams to inform our **discretionary strategies**.  

We backtest **six directional strategies** in total:  
- **Three simple strategies:** Betting on the **favorite, underdog, or draw**.  
- **Three discretionary strategies:** Betting on **home favorites, home underdogs, and away underdogs**.  


### 2. Arbitrage Strategies  
These strategies exploit **pricing inefficiencies** across bookmakers to guarantee **risk-free returns**. We investigate whether certain games have **higher win probabilities**, allowing for potential **biased arbitrage opportunities**.  

We backtest **four arbitrage strategies**:  
- **One unbiased arbitrage strategy**  
- **Three biased arbitrage strategies:** Favoring the **favorite, second-favorite, or underdog**.


### 3. Exploratory Data Analysis (EDA)  
In preparation for backtesting, we conducted **extensive EDA** on betting trends in EPL matches, including:  
- **Bookmakers offering the best odds**  
- **Prevalence of arbitrage opportunities**  
- **Win rates of various strategies**  

These findings can be accessed in:  
- 📂 **`/data/visualisations`**  
- 📓 **`NB03-Simple_Betting_Strategies.ipynb`**  
- 📓 **`NB04-arbitrage_betting_strategies.ipynb`**  


## Team Background

- Matthew Thoomkuzhy - Bsc Economics 1st Year, Cheerful Chelsea Fan
- Xinyan Liao - Bsc  Economics 1st Year, Melancholic Man United Fan
- Noah Salehi - Politics Philosophy and Economics 4th Year, Lively Liverpool Fan 

---

Excited to find out more about how to outsmart the bookmakers? Head over to [Exploratory Data Analysis](eda.md) and find out more!
