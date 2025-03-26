import pandas as pd

def load_data(filepath):
    """Loads the population dataset."""
    df = pd.read_csv(filepath)
    return df

def clean_data(df):
    """Cleans and preprocesses the dataset."""
    df.dropna(inplace=True)  # Remove missing values
    df = df[df['Year'] >= 1960]  # Focus on relevant years
    return df

if __name__ == "__main__":
    filepath = "../data/population_data.csv"
    df = load_data(filepath)
    df = clean_data(df)
    print(df.head())  # Display first few rows
