# weather.py
import requests
import pandas as pd

# 1) get last 7 days temps from a free API (Open-Meteo)
# change to your city coords if you like
LAT, LON = 12.9716, 77.5946  # Bengaluru
url = ("https://api.open-meteo.com/v1/forecast"
       f"?latitude={LAT}&longitude={LON}"
       "&hourly=temperature_2m"
       "&past_days=7&forecast_days=1&timezone=auto")

r = requests.get(url, timeout=30)
data = r.json()["hourly"]

# 2) put into a table
df = pd.DataFrame({"time": data["time"], "temp": data["temperature_2m"]})
# take daily mean by calendar day
df["day"] = df["time"].str.slice(0, 10)
daily = df.groupby("day")["temp"].mean().reset_index()

# 3) simple prediction: average of last 3 days
last3 = daily["temp"].tail(3)
pred = last3.mean()

print("Last 7 days (daily avg):")
print(daily.tail(7))
print("\nBaby prediction for tomorrow's avg temp:", round(pred, 1), "°C")
