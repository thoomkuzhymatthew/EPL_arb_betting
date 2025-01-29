import pandas as pd

# Function to Obtain Highest Odds and Bookmaker for Each Fixture-Outcome
def process_row(row):
    
    # Initialize lists for each outcome
    home_odds = []
    away_odds = []
    draw_odds = []

    # Loop through all columns in the row and store the respective odds for each outcome
    for col, value in row.items():
        if 'home_odds' in col and pd.notna(value):
            home_odds.append((value, col))  
        elif 'away_odds' in col and pd.notna(value):
            away_odds.append((value, col))
        elif 'draw_odds' in col and pd.notna(value):
            draw_odds.append((value, col))

    # Find max odds and corresponding column for each outcome
    max_home, home_bookmaker = max(home_odds, default=(None, None))
    max_away, away_bookmaker = max(away_odds, default=(None, None))
    max_draw, draw_bookmaker = max(draw_odds, default=(None, None))

    # Extract bookmaker names from column names
    home_bookmaker = home_bookmaker.split('_')[0] if home_bookmaker else None
    away_bookmaker = away_bookmaker.split('_')[0] if away_bookmaker else None
    draw_bookmaker = draw_bookmaker.split('_')[0] if draw_bookmaker else None

    # Return the new values as a Series
    return pd.Series({
        'max_home': max_home,
        'home_bookmaker': home_bookmaker,
        'max_away': max_away,
        'away_bookmaker': away_bookmaker,
        'max_draw': max_draw,
        'draw_bookmaker': draw_bookmaker
    })

def get_implied_vs_actual(df, odds_column, bins, outcome_label):
    """    
    Parameters:
    - df: pandas DataFrame containing the data.
    - odds_column: str, column name for odds ('max_draw', 'max_home' or 'max_away').
    - bins: list, bin edges for grouping odds.
    - outcome_label: str, outcome label to filter on ('D', 'H' or 'A').
    """
    # Calculate implied probabilities
    df['implied_prob'] = 1 / df[odds_column]
    
    # Bin the odds
    df['odds_bin'] = pd.cut(df[odds_column], bins=bins, include_lowest=True)
    
    # Calculate actual probabilities
    actual_prob = (
        df.groupby('odds_bin')['FTR']
        .apply(lambda x: (x == outcome_label).mean())  # Filter by outcome
        .reset_index(name='actual_prob')
    )
    
    # Calculate average implied probabilities for each bin
    implied_prob = (
        df.groupby('odds_bin')['implied_prob']
        .mean()
        .reset_index(name='implied_prob')
    )
    
    # Merge actual and implied probabilities
    analysis = actual_prob.merge(implied_prob, on='odds_bin')
    
    # Prepare dataframe for plotting
    analysis['odds_bin'] = analysis['odds_bin'].astype(str)
    analysis_melted = analysis.melt(
        id_vars='odds_bin',
        value_vars=['actual_prob', 'implied_prob'],
        var_name='Type',
        value_name='Probability'
    )
    analysis_melted['Type'] = analysis_melted['Type'].replace({
        'actual_prob': 'Actual Probability',
        'implied_prob': 'Implied Probability'
    })
    
    return analysis_melted



import pandas as pd

# function to get df from database w/ row discrepancies
def merge_odds_data(odds_df, results_df, process_row):
    """
    Merges odds and results DataFrames, applies the process_row function, and selects relevant columns.

    Parameters:
    - odds_df (pd.DataFrame): The DataFrame containing odds data.
    - results_df (pd.DataFrame): The DataFrame containing match results.
    - process_row (function): The function to apply row-wise.

    Returns:
    - pd.DataFrame: Processed DataFrame with best odds and respective bookmakers.
    """

    # Merge odds data with results on fixture_id
    merged_df = odds_df.merge(results_df, on='fixture_id', how='inner')

    # Apply the row-processing function
    new_columns = merged_df.apply(process_row, axis=1)
    merged_df = pd.concat([merged_df, new_columns], axis=1)

    # Select only relevant columns
    merged_df = merged_df[['fixture_id', 'Date', 'home_team', 'away_team', 'FTR', 
                           'max_home', 'home_bookmaker', 'max_away', 'away_bookmaker', 
                           'max_draw', 'draw_bookmaker']]
    
    return merged_df
