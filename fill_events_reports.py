import requests
from datetime import datetime

# Base URLs for your endpoints
base_url = "http://127.0.0.1:8080"
events_url = f"{base_url}/events/"
reports_url = f"{base_url}/reports/"

# Example: add 5 events
for i in range(1, 6):
    event_data = {
        "title": f"Event {i}",
        "date": datetime.utcnow().isoformat(),
        "correspondent_id": 1  # assign to the first correspondent
    }
    response = requests.post(events_url, json=event_data)
    if response.status_code == 200:
        event = response.json()
        print(f"Created Event: {event}")
        
        # For each event, create 3 reports
        for j in range(1, 4):
            report_data = {
                "title": f"Report {j} for Event {i}",
                "content": f"Details of Report {j} for Event {i}.",
                "correspondent_id": 1,
                "event_id": event["id"]
            }
            rep_resp = requests.post(reports_url, json=report_data)
            if rep_resp.status_code == 200:
                print(f"  Created Report: {rep_resp.json()}")
            else:
                print(f"  Failed to create Report {j}: {rep_resp.text}")
    else:
        print(f"Failed to create Event {i}: {response.text}")
