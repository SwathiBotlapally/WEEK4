import pandas as pd
import numpy as np

def generate_weather_data(out_path="data/weather_raw.csv"):
    months = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
    avg_temp = [18, 20, 24, 28, 32, 30, 28, 27, 26, 24, 20, 18]
    rainfall = [12, 10, 8, 15, 25, 120, 180, 160, 90, 25, 10, 5]

    df = pd.DataFrame({
        "month": months,
        "avg_temp_c": avg_temp,
        "rainfall_mm": rainfall
    })
    
    df.to_csv(out_path, index=False)
    print("Generated:", out_path)

if __name__ == "__main__":
    generate_weather_data()
