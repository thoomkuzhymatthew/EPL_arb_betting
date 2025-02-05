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

The largest probelm I had was in the encoding for bias


## Team Collaboration  

### Role in Team Coordination  

### Conflict Resolution  

## Learning Journey  

### Skills Developed  

### Challenges Overcome  

### Areas for Future Growth  


