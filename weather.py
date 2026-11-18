from typing import Any
import httpx2
from mcp.server import MCPServer

# initialize MCPServer
mcp = MCPServer("weather")

# Constants
OPEN_METEO_API_BASE = "https://api.open-meteo.com/v1/forecast"
USER_AGENT = "weather-app/1.0"

# Helper Functions
async def make_request(url: str, params: dict[str, Any]) -> dict[str, Any] | None:
    """Make a request to the NWS API with proper error handling."""
    headers = {"User-Agent": USER_AGENT}
    async with httpx2.AsyncClient() as client:
        try:
            response = await client.get(url, headers=headers, params=params, timeout=30.0)
            response.raise_for_status()
            return response.json() # JSON -> Python dictionary
        except Exception:
            return None

# Implementing tool execution
@mcp.tool() # Function Registry
async def get_global_forecast(latitude: float, longitude: float) -> str:
    """Get weather forecast for a location.

    Args:
        latitude: Latitude of the location
        longitude: Longitude of the location
    """
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "current": "temperature_2m,precipitation",
        "hourly": "temperature_2m,precipitation",
        "forecast_days": 2,
        "timezone": "auto",
    }
    # First get the forecast grid endpoint
    
    data = await make_request(OPEN_METEO_API_BASE, params)

    if not data:
        return "Unable to fetch forecast data for this location."

    current = data["current"]
    hourly = data["hourly"]

    lines = [
        f"Current time: {current['time']}",
        f"Current temperature: {current['temperature_2m']}°C",
        f"Current precipitation: {current['precipitation']} mm",
        "",
        "Next 6 hours:",
    ]

    # Only keep the upcoming(not in past), get 6 hours
    upcoming = [
        (t, temp, rain)
        for t, temp, rain in zip(hourly["time"], hourly["temperature_2m"], hourly["precipitation"])
        if t > current["time"]
    ][:6]

    for t, temp, rain in upcoming:
        lines.append(f"{t}: {temp}°C, precipitation {rain} mm")

    return "\n".join(lines)


if __name__ == "__main__":
    mcp.run(transport="stdio")