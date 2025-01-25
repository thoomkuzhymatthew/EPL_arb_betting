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
