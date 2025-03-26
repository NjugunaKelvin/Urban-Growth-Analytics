import requests
import pandas as pd
import os

# World Bank API base URL for population and urbanization data
POPULATION_API_URL = "http://api.worldbank.org/v2/country/{}/indicator/SP.POP.TOTL?date=1960:2023&format=json"
URBANIZATION_API_URL = "http://api.worldbank.org/v2/country/{}/indicator/SP.URB.TOTL.IN.ZS?date=1960:2023&format=json"

# Countries to analyze
COUNTRIES = {
    "USA": "United States",
    "CHN": "China",
    "IND": "India",
    "BRA": "Brazil",
    "NGA": "Nigeria"
}

def fetch_data(url, country_code):
    """Fetch data from World Bank API."""
    response = requests.get(url.format(country_code))
    if response.status_code == 200:
        data = response.json()
        return data[1] if data and len(data) > 1 else None
    return None

def process_data():
    """Fetch and process data for selected countries."""
    records = []
    
    for code, country in COUNTRIES.items():
        pop_data = fetch_data(POPULATION_API_URL, code)
        urb_data = fetch_data(URBANIZATION_API_URL, code)
        
        if pop_data and urb_data:
            for i in range(len(pop_data)):
                year = pop_data[i]["date"]
                population = pop_data[i]["value"]
                urban_rate = urb_data[i]["value"] if i < len(urb_data) else None
                
                records.append([country, year, population, urban_rate])

    # Convert to DataFrame
    df = pd.DataFrame(records, columns=["Country", "Year", "Population", "Urbanization Rate"])
    df.dropna(inplace=True)
    df["Year"] = df["Year"].astype(int)
    
    return df

if __name__ == "__main__":
    df = process_data()
    DATA_DIR = "../data"
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)  # Create the directory

    df.to_csv(os.path.join(DATA_DIR, "population_data.csv"), index=False)
    print("✅ Data fetched and saved successfully!")


# Ensure the data directory exists


