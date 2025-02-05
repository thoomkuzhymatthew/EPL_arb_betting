# Technical Contributions

## NB03: Simple Betting Strategies
One of my main responsibilities in this project was to conduct both exploratory data analysis (EDA) and backtesting with regards to simple, unidirectional betting strategies in the Premier League. 

### Designing Function to Obtain Highest Odds for Each Match and Outcome
*Reference: Pull Request #18*

I designed the `process_row` function in `functions.py` which will return the highest odds and the respective bookmaker for each outcome (Home, Away and Draw) given a specific fixture (as determined by the row). This was crucial in obtaining the best odds possible for our analyses of both simple and arbitrage betting strategies in NB03 and NB04 respectively.

### Exploratory Data Analysis for Simple Betting Strategies
*Reference: Pull Request #18*

1. Finding Bookmakers with Best Odds

    I wrote the `get_top_bookmakers` function to return the top 5 bookmakers for each outcome (Home, Away and Draw) such that we can better focus our attention on the bookmakers that offer better odds in real betting. 

2. Finding Potential Mispriced Odds

    I wrote the `get_implied_vs_actual` function in `functions.py` that first bins games based on odds, then calculates the implied probability of winning from 1/odds and the actual probability of winning from the percentage of wins in that bin. This allows me to plot the two line graphs and observe if there are any deviations in the implied vs actual probabilities that we could exploit.

### Backtesting These Strategies

I decided to backtest 6 strategies, as informed by the insights from my EDA above. 

| Strategy                           | Odds Range     | Strategy Type |
|-------------------------------------|---------------|----|
| Betting on Home Favourites         | 1.25 to 1.75  | Discretionary |
| Betting on Home Underdogs          | 4.5 to 5.5    | Discretionary |
| Betting on Away Underdogs          | 2.5 to 4.0    | Discretionary |
| Betting on Favourites  | NIL | Simple |
| Betting on Underdogs | NIL | Simple |
| Betting on Draws | NIL | Simple |

Because discretionary strategies were only applied if certain conditions were met, I encoded them with a binary '0' or '1' variable. This way, bet simulations can be more streamlined as we can just take this binary variable multiplied by the odds - so if no bet is made, no change to profit levels.

Then, I wrote the functions `calculate_discretionary_bankroll` and `calculate_simple_bankroll` to generate the simulation of a £1000 over the respective strategies.

The backtesting was challenging because:

1. Presence of NaN Values

    Because of the size of the dataset, some odds had NaN values and they were affecting my results initially with multiple strategies having rows of NaN. Hence, these had to be especially removed.

2. Difficult to See Any Strategy Generate Profit

    nitially, all strategies ran my bankroll to zero. Whilst that's not necessarily surprising (we know gambling is bad), I figured that taking less aggressive approaches like **hard cap on stake limits** might see some success.


## Our Git Website


## 


# Team Collaboration  


# Learning Journey  

### Skills Developed  
This project significantly enhanced my technical and collaborative skills:  

- **Data Processing & Cleaning**: I deepened my understanding of handling real-world datasets, particularly in sports analytics.  
- **SQL & Pandas Proficiency**: Working with structured and unstructured data improved my ability to manipulate large datasets efficiently.  
- **Markdown & Documentation**: Writing clear and structured documentation improved my ability to communicate technical concepts effectively.  
- **Collaboration & Code Integration**: I gained experience in working with a team on a shared codebase, handling dependencies, and ensuring code readability.  

### Challenges Overcome  
The biggest challenges I faced were:  

- **Handling Inconsistent Data Formats**: The data from different sources used varying team name formats. I resolved this by creating robust mapping dictionaries that standardized names.  
- **Ensuring Scalable Data Processing**: Given the large dataset, initial processing attempts were slow. By implementing batch processing and optimizing SQL storage, I significantly reduced runtime.  
- **Balancing Workload**: With documentation responsibilities in addition to coding, I managed my time effectively by setting clear milestones and prioritizing tasks.  

### Areas for Future Growth  
While I gained valuable experience, I recognize areas where I can further improve:  

- **Advanced SQL & Database Management**: Optimizing queries and database structures would further improve data handling efficiency.  
- **Machine Learning for Predictive Analysis**: Applying ML models to betting data could be a future extension of this research.  
