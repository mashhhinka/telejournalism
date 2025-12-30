import requests
from datetime import datetime, timedelta

URL = "http://127.0.0.1:8080/events/events/"

# Example: generate 50 events
for i in range(1, 51):
    data = {
        "title": f"Event {i}",
        "location": f"City {i%10}",  # repeat cities
        "description": f"This is the description for Event {i}",
        "date": (datetime.utcnow() + timedelta(days=i)).isoformat()
    }
    response = requests.post(URL, json=data)
    if response.status_code == 200:
        print(f"Created: {response.json()['title']}")
    else:
        print(f"Error {response.status_code}: {response.text}")
