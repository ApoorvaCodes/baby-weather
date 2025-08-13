# Baby Weather Predictor

A simple Python project that fetches past weather data and makes a basic prediction for tomorrow’s average temperature using the **Open-Meteo API**.

## 📌 Features
- Fetches hourly temperature data for the past 7 days
- Calculates daily average temperatures
- Predicts tomorrow’s temperature based on the last 3 days’ averages
- Super lightweight and beginner-friendly

## 📂 Project Structure
baby-weather/
│-- weather.py # Main Python script
│-- README.md # Project documentation

---

## 🚀 How to Run

1. **Clone this repository**
```bash
git clone https://github.com/<your-username>/baby-weather.git
cd baby-weather

python3 -m venv .venv
source .venv/bin/activate  # Mac/Linux
# OR
.venv\Scripts\activate     # Windows

pip install requests pandas

python weather.py
🛠 Dependencies
Python 3.8+

requests

pandas

Install them with:

bash
Copy
Edit
pip install requests pandas
📊 Example Output
yaml
Copy
Edit
Last 7 days (daily avg):
          day       temp
0  2025-08-06   27.4
1  2025-08-07   28.1
2  2025-08-08   27.6
...

Baby prediction for tomorrow's avg temp: 28.0 °C
🌟 Future Improvements
Add more advanced prediction models (e.g., machine learning)

Allow user to input their city

Display results in a graph
