{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Weather Data Analysis & Visualization\n",
    "Complete analysis of monthly temperature and rainfall."
   ]
  },
  {
   "cell_type": "code",
   "metadata": {},
   "source": [
    "import pandas as pd\n",
    "from src.load_data import load_weather\n",
    "from src.clean_data import clean_weather\n",
    "from src.viz import line_temperature, bar_rainfall, pie_seasons\n",
    "\n",
    "df = load_weather(\"data/weather_clean.csv\")\n",
    "df.head()"
   ],
   "execution_count": null,
   "outputs": []
  },
  {
   "cell_type": "code",
   "metadata": {},
   "source": [
    "df.describe()"
   ],
   "execution_count": null,
   "outputs": []
  },
  {
   "cell_type": "code",
   "metadata": {},
   "source": [
    "line_temperature(df)\n",
    "bar_rainfall(df)\n",
    "pie_seasons(df)"
   ],
   "execution_count": null,
   "outputs": []
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Insights\n",
    "- Temperatures peak in April–May.\n",
    "- Winter months are the coolest.\n",
    "- Rainfall is extremely high during monsoon (Jun–Sep).\n",
    "- Rainy season contributes nearly 70% of total rainfall."
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
