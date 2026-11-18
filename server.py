#uv run mcp dev server.py
from mcp.server import MCPServer
import httpx

mcp = MCPServer("Demo")

def fetch_forecast():
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
	    "latitude": 24.9937,
	    "longitude": 121.297,
	    "hourly": ["temperature_2m", "rain", "wind_speed_10m", "wind_direction_10m"],
    }
    r = httpx.Client().get(url, params=params, timeout=10)
    r.raise_for_status()
    return r.json()

@mcp.tool()
def get_forecast():
    f = fetch_forecast()
    data = f["hourly"]
    lines = []
    for i, hour in enumerate(data["time"]):
        lines.append(f"""Time: {data["time"][i][11:]}
    Temperature: {data["temperature_2m"][i]}°C
    Rain: {data["rain"][i]*100}%
    Wind Speed: {data["wind_speed_10m"][i]}m/s
    ------------------------------------------------""")
    return lines

@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers."""
    return a + b


@mcp.resource("greeting://{name}")
def greeting(name: str) -> str:
    """Greet someone by name."""
    return f"Hello, {name}!"


@mcp.prompt()
def summarize(text: str) -> str:
    """Summarize a piece of text in one sentence."""
    return f"Summarize the following text in one sentence:\n\n{text}"