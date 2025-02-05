# 1. Technical Contributions

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

    Initially, all strategies ran my bankroll to zero. Whilst that's not necessarily surprising (we know gambling is bad), I figured that taking less aggressive approaches like **hard cap on stake limits** might see some success.


## Our Git Website
*Evidence: Commit history on the 4th and 5th of February*
I designed the 'Exploratory Data Analysis' portion of the website in addition to assisting Matthew with deciding the colour scheme, fonts, font sizes etc.

## Key Technical Decisions Influenced

1. Creation of `fixture_id`

    In the initial discussions, I suggested the creation of a unique `fixture_id` to merge match odds and outcomes which was thereafter implemented by Noah in NB02.

2. Creating an SQL Database

    Though an SQL Database wasn't necessary, I suggested that we should standardise our data inputs for NB03 and NB04 to streamline it and ensure our data sources were consistent.

3. Deprecating NB05 (Positive Expected Value Betting)

    I realised that our plan to construct a 'fair odds' based on the team's form (last 5 games performance) was probably already factored into bookmakers' pricing and it'll be difficult to get an edge. Hence, I suggested that we focus on more detailed analysis for the other two categories of strategies instead. 

# 2. Team Collaboration  

## Role in Team Collaboration
*Evidence: 'Issues' tab on Github, [Collaboration Space](https://caring-science-810.notion.site/1633c9e924fc8011af27f5ce14ed4d6a?v=d886cee50f394c1ab113446a24f6df59&pvs=4)*

My main role in team collaboration was ensuring a streamlined workflow. This included:

1. Creating a [Collaboration Space](https://caring-science-810.notion.site/1633c9e924fc8011af27f5ce14ed4d6a?v=d886cee50f394c1ab113446a24f6df59&pvs=4) where we could upload comments for each other's work and refer to the rubrics/standardisation.

2. Enforcing issue-tracking and creating separate branches for any edits to ensure the team is always updated on tasks and any potential conflicts would be flagged before merging. I assisted my teammates with this by uploading the standardised code for starting new branches on our [Collaboration Space](https://caring-science-810.notion.site/1633c9e924fc8011af27f5ce14ed4d6a?v=d886cee50f394c1ab113446a24f6df59&pvs=4) 


## Supporting Team Members
Beyond my primary responsibilities, I supported my teammates by 

1. Ensuring Clarity of Presentation (*Evidence: Pull Request #42*)

    I ensured that descriptions of specific code snippets and the overall flow of each notebook was sound, in addition to correcting any grammatical errors.

2. Code Reviews

    I reviewed all of Noah and Matthew's notebooks to ensure the code was efficient and streamlined, providing comments whenever required and running to ensure its error-free.

## Conflict Resolution
Thankfully, due to our meticulous issue-tracking and branch-creation, we did not run into any syncing conflicts on Github. 

The main conflict that occurred was the scope of our project as we wanted to investigate betting strategies across different leagues. We mediated that by considering the pros and cons of a more focused investigation - though we had less scope, we can focus on the intricacies of each League and better optimise our betting strategies. We reached a consensus easily and decided to focus on the Premier League, with the option to expand our investigation in the future. 

# 3. Learning Journey  

## Skills Developed  

- **Git Collaboration and Workflow Management**: Deepened my understanding of how to manage workflow on Git using issue-tracking and branch-creation, just like in real-world data science projects.

- **Pandas Proficiency**: Reinforced my data manipulation skills like being able to bin data, melt dataframes for better plotting etc.

- **Exploratory Data Analysis**: Working with very simple datasets (just odds and match outcomes) developed my ability to creatively manipulate the data and generate interesting findings like the presence of mispriced odds in home and away games. 

- **Code Documentation**: Writing concise markdown documentation and comments within my functions honed my ability to better communicate my coding logic.

## Challenges Overcome  
The most significant challenges I faced were:  

- **Troubleshooting the Backtesting Function**: My backtesting results were returning many NaN values as the final bankroll. After some df.iloc[] inspections, I concluded it was due to NaN values in the odds which I removed to resolve this issue.

- **Git Workflow Management**: There were a few instances where I accidentally made unwanted edits on the notebooks on my local version after I had already merged that previous branch into Github. This resulted in my local version being stuck at the deprecated branch because I couldn't run `git pull origin main` due to the un-pushed edits. Hence, I had to run `git reset --hard` to reset to the last commit and `git pull origin main` to reset my local version on VSCode.  

- **Displaying SVG Plots in Jupyter Notebooks**: Github had compatibility issues trying to display SVG plots within the notebooks as the visualisations always had the same formatting issues. Hence, I opted for a dynamic link that brings the reader to the referenced visualisation within `../data/visualisations` instead.  

## Areas for Future Growth  

- **Optimisation of Betting Strategies**: In addition to investigating the profitability of simple strategies themselves, I hope to leverage libraries like `SciPy` to engage in the optimisation of these strategies and derive a custom strategy with even higher profitability. 

- **Expanding into Other Bet Types**: In addition to just bet outcomes, I hope to research betting strategies involving match score, goals scored, yellow/red cards given etc. which can offer even more diversification to our betting approach.
