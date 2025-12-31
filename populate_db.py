import requests

BASE_URL = "http://127.0.0.1:8000"  # make sure your FastAPI server is running
NUM_EVENTS = 50  # how many events to create

for i in range(1, NUM_EVENTS + 1):
    event_data = {
        "title": f"Event {i}",
        "location": f"City {i % 10}",  # cycles through 10 cities
        "description": f"This is the description for event {i}"
    }

    response = requests.post(f"{BASE_URL}/events/", json=event_data)
    
    if response.status_code == 200 or response.status_code == 201:
        print(f"Created event {i}")
    else:
        print(f"Failed to create event {i}: {response.text}")
