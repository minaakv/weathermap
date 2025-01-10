import requests

def get_weather(city):
    # Replace 'your_api_key_here' with your OpenWeatherMap API key
    API_KEY = "2d754914da1e526d4bd67fe24c11f1ac"
    BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

    # Prepare the API request
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"  # Use "imperial" for Fahrenheit
    }

    try:
        # Send a GET request to the API
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()  # Raise an error for bad HTTP status codes

        # Parse the JSON response
        weather_data = response.json()

        # Extract relevant information
        city_name = weather_data["name"]
        temperature = weather_data["main"]["temp"]
        description = weather_data["weather"][0]["description"]
        humidity = weather_data["main"]["humidity"]
        wind_speed = weather_data["wind"]["speed"]

        # Display the weather information
        print(f"\nWeather in {city_name}:")
        print(f"Temperature: {temperature}°C")
        print(f"Description: {description.capitalize()}")
        print(f"Humidity: {humidity}%")
        print(f"Wind Speed: {wind_speed} m/s")

    except requests.exceptions.HTTPError:
        print("City not found or invalid API key. Please try again.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    print("Welcome to the Weather App!")
    while True:
        city = input("\nEnter the name of a city (or type 'exit' to quit): ").strip()
        if city.lower() == "exit":
            print("Goodbye!")
            break
        get_weather(city)