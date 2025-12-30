import requests
from random import choice, randint
from datetime import datetime, timedelta

BASE_URL = "http://127.0.0.1:8080"

# ---------- Sample data ----------
names = ["Alice Smith", "Bob Johnson", "Charlie Lee", "Diana Adams", "Eve Brown"]
emails = ["alice@example.com", "bob@example.com", "charlie@example.com", "diana@example.com", "eve@example.com"]
countries = ["USA", "UK", "France", "Germany", "Australia"]

event_titles = ["Earthquake in City", "Elections 2025", "New Tech Launch", "Sports Championship", "Climate Summit"]
locations = ["New York", "London", "Paris", "Berlin", "Sydney"]

report_titles = ["Breaking News", "Exclusive Interview", "Field Report", "Analysis", "Summary"]

# ---------- Create correspondents ----------
correspondent_ids = []
for i in range(len(names)):
    data = {
        "name": names[i],
        "email": emails[i],
        "country": countries[i],
        "bio": f"Bio of {names[i]}"
    }
    resp = requests.post(f"{BASE_URL}/correspondents/", json=data)
    if resp.status_code == 200:
        correspondent_ids.append(resp.json()["id"])
        print("Created correspondent:", resp.json())
    else:
        print("Error creating correspondent:", resp.text)

# ---------- Create events ----------
event_ids = []
for i in range(len(event_titles)):
    data = {
        "title": event_titles[i],
        "location": locations[i],
        "description": f"Description of {event_titles[i]}"
    }
    resp = requests.post(f"{BASE_URL}/events/", json=data)
    if resp.status_code == 200:
        event_ids.append(resp.json()["id"])
        print("Created event:", resp.json())
    else:
        print("Error creating event:", resp.text)

# ---------- Create reports ----------
for i in range(20):  # create 20 reports
    data = {
        "title": choice(report_titles),
        "content": f"Content of report {i+1}",
        "correspondent_id": choice(correspondent_ids),
        "event_id": choice(event_ids)
    }
    resp = requests.post(f"{BASE_URL}/reports/", json=data)
    if resp.status_code == 200:
        print("Created report:", resp.json())
    else:
        print("Error creating report:", resp.text)
