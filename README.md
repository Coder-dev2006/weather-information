#  Simple Weather App (Python + Open Meteo API)
This is a simple **command-line weather application** built with Python.  
It uses the free [Open-Meteo API](https://open-meteo.com/) to fetch **real-time weather data** for any city in the world — no API key required!

---

##  Features
-  Get real-time temperature and wind speed  
-  Automatic geocoding (city → coordinates)  
-  Uses **Open-Meteo API** (no signup, no key)  
-  Simple command-line interface  
-  Works on Windows, Linux, and macOS  

---

##  Requirements
Install dependencies:

```bash
pip install requests
 Usage
Run the program in your terminal:

bash
Copy code
python weather_app.py
Example:

yaml
Copy code
=== Simple Weather App ===
Shahar nomini kiriting (yoki chiqish uchun 'exit'): Tashkent

 Tashkent shahri uchun ob-havo:
 Harorat: 23°C
 Shamol tezligi: 14 km/h
 Vaqt: 2025-10-08T08:00

Shahar nomini kiriting (yoki chiqish uchun 'exit'): exit
 Dastur tugadi.
 How It Works
You enter a city name.

The script uses Open-Meteo Geocoding API to get the latitude and longitude.

It sends a request to the Weather Forecast API with these coordinates.

The result shows current temperature, wind speed, and time.

 Project Structure
Copy code
simple-weather-app/
│
├── weather_app.py
└── README.md
Notes
The app uses free APIs, so you don’t need to register or use any key.

Requires an active internet connection to fetch live data.

City names should be entered in English (e.g., Paris, Tokyo, Tashkent).

 Author
Developed by Coder-dev2006
 Powered by Open-Meteo — open and free weather data for everyone.

 License
This project is licensed under the MIT License — use, modify, and share freely.



