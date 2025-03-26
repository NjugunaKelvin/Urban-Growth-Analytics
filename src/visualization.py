import pandas as pd
import matplotlib.pyplot as plt

def plot_population_trends(df):
    """Plots population growth over time."""
    plt.figure(figsize=(10, 5))

    for country in df["Country"].unique():
        country_data = df[df["Country"] == country]
        plt.plot(country_data["Year"], country_data["Population"], label=country)

    plt.xlabel("Year")
    plt.ylabel("Population (in billions)")
    plt.title("Population Growth Over Time")
    plt.legend()
    plt.grid(True)
    plt.show()

def plot_urbanization_trends(df):
    """Plots urbanization percentage over time."""
    plt.figure(figsize=(10, 5))

    for country in df["Country"].unique():
        country_data = df[df["Country"] == country]
        plt.plot(country_data["Year"], country_data["Urbanization Rate"], label=country)

    plt.xlabel("Year")
    plt.ylabel("Urbanization Rate (%)")
    plt.title("Urbanization Growth Over Time")
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    filepath = "../data/population_data.csv"
    df = pd.read_csv(filepath)
    
    plot_population_trends(df)
    plot_urbanization_trends(df)
