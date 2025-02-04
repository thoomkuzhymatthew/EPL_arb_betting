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

### **Simulation of arbitrage strategies**  :

#### **overview:**

The following sections show the results of simulating different arbitrage strategies. The 5 following strategies were simulated:

- Unbiased arbitrage betting
- Biased arbitrage betting towards the favourite outcome
- Biased arbitrage betting towards the second favourite outcome
- Biased arbitrage betting towards the third favourite outcome (underdog)
- Custom arbitrage strategy for bias towards weak facourites and strong underdogs

Note that outcomes for each event are ordered numerically to determine if the outcome is a favourite or underdog. Thus draw odds can take the value of the underdog.

---
title: "Arbitrage Betting Strategy Performance in Premier League"
layout: default
---

<link rel="stylesheet" type="text/css" href="./assets/css/style.css">

<div class="header">
    <a href="index.html">Home</a>
    <a href="about.html">About</a>
    <a href="eda.html">Exploratory Data Analysis</a>
    <a href="backtesting.html">Backtesting</a>
</div>

# **Arbitrage Betting Strategy Performance in Premier League**
**Prepared for: [Your Business/Project Name]**  
**Date: [Insert Date]**  

---

## **Executive Summary**
This report evaluates the **performance of arbitrage betting strategies** applied to **Premier League football markets** over a five-year backtesting period. Since these are arbitrage events, negative bankroll periods are not expected; instead, our focus is on the **efficiency, profitability, and trade-offs between strategy types**.

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
- **Expansion of arbitrage detection to international leagues for cross-market inefficiencies and larger samples.**
- 
---

<img src="arb_simulation.png" alt="Arbitrage Strategies Simulation" width="900" height="600">

