# Individual Reflection
Matthew Thoomkuzhy

## Technical Contributions-

I had 2 main roles: Collecitng data in NB01 and carrying out backtesting for arbitrage functions in NB04.

NB01:

I connected to the API server for the odds API. 

The first problem I had to overcome was that the api only collected historical data for a signle day so I wrote a fucntion (def fetch_odds) to loop from the start date to end date, collect the data for each date in the range, and append the results to a JSON file.

The 2nd problem I faced was that the data in the file was too large to be pushed to github so I had to resplit the collected data into smaller files. So I wrote a function (def split_JSON_By_month) which splits the data for matches collected by month. These monthly files do not exceed the 30MB limit os could be pushed to github.

Evidence can be seen through commits to pull requests 11,13,14,15 and 16. Which were directed at resolving issue #3

NB04:

Here I faced less problems, I created a backtesting function (def Sim_arb) to backtest how different strategies would affect an inital bankroll of 1000 pounds over time. Evidenced by commits to pull requests 23,24,25,29,30

I also produced simulation plots with the funciton I created called (def plot_arb). Evidenced by commits to pull requests 23,24,25,29,30

I carried out EDA on matches with arbitrage opportunities. I investigated the nature of arbitrage to produce insights about matches with arbitrage opportunities and how they vary from the sample. Evidenced by commits to pull requests 19,20,21,22.

Initially my graphs were very volatile and going up and down, which didn't make sense for arbitrage (non loss events). So I changed the bias logic to rely on a base stake for all events (ensuring break even) and an extra stake to be allocated to the bias outcome, which would pay out when the bias outcome for the Full time result matched (the bet was successful).




## Team Collaboration  

google meets images
issue tracking
code comments

### Role in Team Coordination  

### Conflict Resolution  
Co
## Learning Journey  

### Skills Developed  
Markdown
python programming

### Challenges Overcome  

HTML
### Areas for Future Growth  

ML
