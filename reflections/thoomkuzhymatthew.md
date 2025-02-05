# Individual Reflection
Matthew Thoomkuzhy

## Technical Contributions-

I had 2 main roles: Collecitng data in NB01 and carrying out EDA and backtesting for arbitrage functions in NB04.

**NB01:**

The first problem I had to overcome was that the api only collected historical data for a signle day so I wrote a fucntion (def fetch_odds) to loop from the start date to end date, collect the data for each date in the range, and append the results to a JSON file.

The 2nd problem I faced was that the data in the file was too large to be pushed to github so I had to resplit the collected data into smaller files. So I wrote a function (def split_JSON_By_month) which splits the data for matches collected by month. These monthly files do not exceed the 30MB limit os could be pushed to github.

This meant a change in the folder structure for the directory was crucial so that all of these new JSON's could be stored clearly, so a new folder was created within data/raw called grouped events. This was a technical decision I influenced.

Evidence can be seen through commits to pull requests 11,13,14,15 and 16. Which were directed at resolving issue #3

**NB04:**

Here I faced less problems, I created a backtesting function (def Sim_arb) to backtest how different strategies would affect an inital bankroll of 1000 pounds over time. Evidenced by commits to pull requests 23,24,25,29,30

I also produced simulation plots with the function I created called (def plot_arb). Evidenced by commits to pull requests 23,24,25,29,30

I carried out EDA on matches with arbitrage opportunities. I investigated the nature of arbitrage to produce insights about matches with arbitrage opportunities and how they vary from the sample. Evidenced by commits to pull requests 19,20,21,22.

The main problem faced was that initially my graphs were very volatile and going up and down, which didn't make sense for arbitrage (non loss events). So I changed the bias logic to rely on a base stake for all events (ensuring break even) and an extra stake to be allocated to the bias outcome, which would pay out when the bias outcome and the Full time result matched. (the bet was successful).

Due to this, another technical decision I made was to make my own backtesting funciton rather than use Xinyan's due to stark differences in the strategy logic. All attempts of manipulating his logic to fit an arbitrage function didn't work, so I decided it was easier to make my own backtesting function from scratch (def sim_arb)



## Team Collaboration  

We frequently stayed in touch with regular google meetings.
In these meetings we would discuss our work and notebooks and give feedback to our peers for suggestions to improve our visualisations or documentation
This way all feedback given was constructive. 

After I completed my issues, if another person's task was overwhelming e.g. the creation of the website, I contributed to the completion of the task. This can be seen thruugh commits on the 4th and 5th of February regarding the Markdown, HTML and CSS elements.

We also met up early on to decide the allocation of work and issues on github were assigned accordingly, this meant that it was alot easier to co-ordinate workflow as all I had to do was commit to my assigned issues which were #3 NB01 and #6 NB04.

I also informed Noah about the problem I faced in NB01, and the creation of the grouped events folder to overcome this. This way he knew where to access the files, and that the files were split by month. This helped him develop function (process_all_files) to iterate through the folder and clean the data

When editing the website , Xinyan and I organised the times we would be editing. This way it would prevent double editing and bottlenecks, delaying progress.

Not much conflict arose other than varying opinions on design choice for notebooks and website, all of these were brought up formally in meetings and decided on at the time.
 
## Learning Journey  

### Skills Developed 

- **Python proficiency and API familiarirty:** Working on NB01 improved my familiarity with learning and implementing API documentation. The bias logic in NB04 developed my ability to code logically and abstractly

- **Markdown, HTML and CSS proficiency:** Working on NB01/NB04 improved my ability to style in markdown. Working on the website improved my proficiency in CSS and HTML
  
- **Code collaboration:** I gained experience in working with a team on a shared codebase. I also improved my ability to understand code others have written. It meant I could use their functions previusly written to save time. Xinyan wrote a fucntion (process_row). Using it saved me alot of time obtaining the DF from the database for NB04.


### Challenges Overcome

- **Navigating platform constraints:** When I couldn't push the data due to the JSON file being too large to push to github, I had to split the file up
- **Preventing data leakage:** When backtesting I had to ensure my insights from EDA weren't being used to produce bias results with artificially high profits. So I kept my strategies abstract enough to avoid bias.


### Areas for Future Growth  

**Machine learning-** The next logical step for this project is to deploy more advance models with more parameters and develop a machine learning model to learn what makes a good and bad strategy.
**Advanced statistical techniques-** To develop more sophisticated models this will require an understanding of advanced statistics to increase the sophistication of my parameters.
**Web Scraping-** although other API's could be used, scraping data may be very useful and it might've prevented use from needing to use a **Paid API**
