---
title: "Backtesting Results"
layout: default
---

<link rel="stylesheet" type="text/css" href="./assets/css/style.css">

<div class="header">
    <a href="index.html">Home</a>
    <a href="about.html">About</a>
    <a href="eda.html">Exploratory Data Analysis</a>
    <a href="backtesting.html">Backtesting</a>
</div>

# Backtesting Results

In this section, we developed backtesting functions to simulate betting strategies on the 5-year sample. We categorized these into simple strategies explored in NB03 and arbitrage strategies explored in NB04.

### **Simulation of simple betting strategies**:

#### **overview:**

The following section shows the results of simulating simple betting strategies. The 6 following strategies were simulated:

- Betting on favourites
- Betting on Underdogs
- Betting on Draws
- Betting on home favourites
- Betting on home underdogs
- Betting on away underdogs

<img src="bet_simulation.png" alt="Simple Betting Strategies Simulation" width="900" height="600">

---
## **Performance Breakdown by Strategy**

### **1. Profitability Across Strategies**
| Strategy                     | Final Bankroll (£) | Growth (%) | Risk Level |
|------------------------------|--------------------|------------|------------|
| **Bet on Away Underdogs**    | **£12,000**       | **+500%**  | High       |
| **Bet on Underdogs**         | £0                | -100%      | Very High  |
| **Bet on Favourites**        | £0                | -100%      | Moderate   |
| **Bet on Draws**             | £0                | -100%      | Moderate   |
| **Bet on Home Favourites**   | £0                | -100%      | Low        |
| **Bet on Home Underdogs**    | £0                | -100%      | Very High  |

### **Key Insights**
✔ **Only betting on away underdogs resulted in long-term profitability, suggesting market inefficiencies in away team pricing.**  
✔ **All other strategies led to full bankroll depletion, indicating efficient bookmaker pricing in home favorites, draws, and general underdog markets.**  
✔ **Away underdog betting displayed significant bankroll fluctuations, requiring a strong risk management approach to mitigate downturns.**  
✔ **Betting on generic underdogs (both home and away) was not profitable, reinforcing that home underdogs are correctly priced by bookmakers.**  

---

## **2. Trade-Off Between Return and Volatility**
One of the most important takeaways from this backtest is the **high volatility associated with the only profitable strategy**:

- **Betting on away underdogs yielded the highest bankroll growth but came with substantial drawdowns.**  
- **A risk-averse bettor would struggle to maintain confidence in the strategy** due to periods of severe downturns before eventual recoveries.  
- **All other strategies had much lower variance but ultimately led to zero bankroll**, showing that bookmakers efficiently price favorites, draws, and home underdogs.  

This suggests that **capital allocation and proper bankroll management** are essential for sustaining a profitable edge in away underdog betting.

---

## **3. Why Away Underdog Betting Succeeds**
The **consistent outperformance of away underdog betting** suggests that **bookmakers systematically underprice this category in Premier League betting**:

📌 **Public bias inflates home team prices** → Most bettors prefer backing home favorites, leading to **less favorable odds for them and better value on away underdogs**.  
📌 **Away underdogs have unpredictable but high-return moments** → While they win less frequently, **their high odds compensate for the lower hit rate**.  
📌 **Premier League unpredictability benefits this strategy** → The league sees **regular upsets**, making away underdog betting more viable than in other leagues with more dominant home teams.  

---

## **Conclusion**
Our findings confirm that **simple betting strategies are largely ineffective in Premier League betting, with one key exception: betting on away underdogs**. However, even this approach requires **careful bankroll management due to high volatility**.

To **maximize profitability**, further refinements should include:
- **Dynamic stake sizing models to account for risk-adjusted returns.**
- **Market analysis to determine ideal away underdog betting conditions (e.g., team form, injuries, fixture congestion).**
- **Incorporation of statistical models to refine selection beyond blindly backing away underdogs.**

---

### **Simulation of arbitrage strategies**  :

#### **overview:**

The following sections show the results of simulating different arbitrage strategies. The 5 following strategies were simulated:

- Unbiased arbitrage betting
- Biased arbitrage betting towards the favourite outcome (outcome with the lowest odds)
- Biased arbitrage betting towards the second favourite outcome (outcome with second the lowest odds)
- Biased arbitrage betting towards the third favourite outcome (underdog, outcome with the highest odds)
- Custom arbitrage strategy for bias towards weak facourites and strong underdogs

Note that outcomes for each event are ordered numerically to determine if the outcome is a favourite or underdog. Thus draw odds can take the value of the underdog.

<img src="arb_simulation.png" alt="Arbitrage Strategies Simulation" width="900" height="600">

Key findings include:
- **"Only Second Favorite" arbitrage strategy produced the highest long-term returns**, indicating a persistent pricing inefficiency in Premier League markets.
- **A trade-off exists between betting frequency and return per event**, where **higher-volume strategies yield smaller, stable returns** and **lower-frequency strategies generate higher per-event gains**.
- **Custom strategies incorporating multi-bookmaker arbitrage insights provide strong risk-adjusted returns**, making them viable for professional betting syndicates.
- **Underdog-focused arbitrage underperformed**, reinforcing the idea that **Premier League bookmakers price longshots more accurately than second-favorites**.

---

## **Performance Breakdown by Strategy**

### **1. Profitability Across Strategies**
| Strategy                    | Final Bankroll (£) | Growth (%) | Trade Frequency | Return Per Event |
|-----------------------------|--------------------|------------|-----------------|------------------|
| **Only Second Favorite**    | **£4,500**        | **+350%**  | Low             | High             |
| **Custom Strategy**         | £3,700            | +270%      | Moderate        | Moderate         |
| **No Bias Strategy**        | £3,500            | +250%      | High            | Low              |
| **Only Favorite**           | £3,000            | +200%      | Moderate        | Moderate         |
| **Only Underdog**           | £2,700            | +170%      | Lowest          | Highest          |

### **Key Insights**
✔ **Second-favorite arbitrage betting yields the highest long-term gains.**  
✔ **High-frequency strategies (No Bias) generate smaller returns per event but provide more stability.**  
✔ **Underdog arbitrage strategies underperform, likely due to sharper bookmaker pricing.**  
✔ **Custom strategies, incorporating multiple pricing inefficiencies, deliver a well-balanced risk-adjusted return.**

---

### **2. Trade-Off Between Betting Frequency & Return Per Event**
The key takeaway from this backtest is the **inverse relationship between trade frequency and per-event profitability**:

- **High-frequency strategies (No Bias, Favorites) execute more trades**, but **each bet provides smaller incremental profits**.
- **Low-frequency strategies (Underdogs, Second-Favorites) place fewer bets**, yet **each event yields a significantly larger return**.
- **"Only Second Favorite" strikes the optimal balance**, leveraging **bookmaker mispricing** while maintaining **consistent capital compounding**.

---

### **3. Why Second-Favorites Yield the Highest Returns**
The **consistent outperformance of the second-favorite strategy** suggests that **bookmakers systematically underprice this category in Premier League betting**:

📌 **Public bias skews favorite odds** → Heavy public betting on top teams (Liverpool, Man City, Chelsea) inflates their prices, leading to mispriced second-favorites.  
📌 **Sharp bettors correct underdog pricing faster** → Longshot odds tend to **adjust more rapidly** due to professional money, reducing arbitrage value.  
📌 **Second-favorites receive less sharp attention** → These odds move more slowly, **providing arbitrage traders with more exploitable inefficiencies**.

---

## **Conclusion**
Our findings confirm that **arbitrage betting remains a viable strategy in Premier League markets** when focused on **second-favorite inefficiencies**. The most successful approach balances **high per-event profitability with sustainable trade frequency**, positioning the **"Only Second Favorite" strategy as the most effective long-term model**.

To **maximize profitability**, further refinements should include:

- **Algorithmic bet execution to minimize delays.**
- **Data-driven stake sizing models to enhance compounding.**
- **Expansion of arbitrage detection to international leagues for cross-market inefficiencies and larger samples, to spot mmore opportunities.**
  
---

