from langchain_core.tools import tool
import requests


@tool
def get_weather(latitude: float, longitude: float) -> str:
    """Get current weather using latitude and longitude."""

    url = (
        "https://api.open-meteo.com/v1/forecast"
        f"?latitude={latitude}"
        f"&longitude={longitude}"
        "&current=temperature_2m,wind_speed_10m"
    )

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        data = response.json()

        temperature = data["current"]["temperature_2m"]
        wind_speed = data["current"]["wind_speed_10m"]

        return (
            f"Temperature: {temperature}°C, "
            f"Wind speed: {wind_speed} km/h"
        )

    except requests.exceptions.RequestException:
        return "Weather service is currently unavailable."

    except (KeyError, TypeError):
        return "Weather data format was unexpected."