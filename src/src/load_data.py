import pandas as pd

def load_weather(path="data/weather_raw.csv"):
    df = pd.read_csv(path)
    return df
