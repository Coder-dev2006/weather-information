import requests

API_KEY = "https://api.open-meteo.com/v1/forecast"  # Free API, API key kerak emas

def get_weather(city):
    # Geocoding uchun (shaharni koordinataga aylantirish)
    geo_url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}"
    geo_data = requests.get(geo_url).json()

    if "results" not in geo_data or len(geo_data["results"]) == 0:
        print("❌ Shahar topilmadi, qayta urinib ko‘ring.")
        return

    lat = geo_data["results"][0]["latitude"]
    lon = geo_data["results"][0]["longitude"]

    # Ob-havo ma’lumotini olish
    weather_url = (
        f"{API_KEY}?latitude={lat}&longitude={lon}&current_weather=true"
    )
    data = requests.get(weather_url).json()

    if "current_weather" not in data:
        print("⚠️ Ma’lumotni olishda xatolik.")
        return

    weather = data["current_weather"]
    temp = weather["temperature"]
    wind = weather["windspeed"]

    print(f"\n🌤 {city} shahri uchun ob-havo:")
    print(f"🌡 Harorat: {temp}°C")
    print(f"🌬 Shamol tezligi: {wind} km/h")
    print(f"⏰ Vaqt: {weather['time']}\n")


if __name__ == "__main__":
    print("=== Simple Weather App ===")
    while True:
        city = input("Shahar nomini kiriting (yoki chiqish uchun 'exit'): ").strip()
        if city.lower() == "exit":
            print("👋 Dastur tugadi.")
            break
        get_weather(city)
