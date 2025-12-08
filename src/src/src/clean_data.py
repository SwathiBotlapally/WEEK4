import pandas as pd

def clean_weather(df):
    df = df.drop_duplicates()
    df["month"] = df["month"].str.strip()

    month_order = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
    df["month_num"] = df["month"].apply(lambda x: month_order.index(x) + 1)

    df = df.sort_values("month_num")
    return df
