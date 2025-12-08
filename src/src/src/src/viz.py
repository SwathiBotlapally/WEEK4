import matplotlib.pyplot as plt

def line_temperature(df, output="outputs/figures/line_temperature_trend.png"):
    plt.figure(figsize=(9,4))
    plt.plot(df["month"], df["avg_temp_c"], marker="o")
    plt.title("Monthly Average Temperature Trend")
    plt.xlabel("Month")
    plt.ylabel("Temperature (°C)")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(output)
    plt.close()

def bar_rainfall(df, output="outputs/figures/bar_rainfall_by_month.png"):
    plt.figure(figsize=(9,4))
    plt.bar(df["month"], df["rainfall_mm"])
    plt.title("Monthly Rainfall (mm)")
    plt.xlabel("Month")
    plt.ylabel("Rainfall (mm)")
    plt.tight_layout()
    plt.savefig(output)
    plt.close()

def pie_seasons(df, output="outputs/figures/pie_seasonal_distribution.png"):
    seasons = {
        "Winter": ["Dec","Jan","Feb"],
        "Summer": ["Mar","Apr","May"],
        "Rainy": ["Jun","Jul","Aug","Sep"],
        "Autumn": ["Oct","Nov"]
    }

    season_values = {
        season: df[df["month"].isin(months)]["rainfall_mm"].sum()
        for season, months in seasons.items()
    }

    plt.figure(figsize=(7,7))
    plt.pie(season_values.values(), labels=season_values.keys(),
            autopct="%1.1f%%", startangle=140)
    plt.title("Season-wise Rainfall Distribution")
    plt.axis("equal")
    plt.savefig(output)
    plt.close()
