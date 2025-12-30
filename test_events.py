import requests
from datetime import datetime

BASE_URL = "http://127.0.0.1:8000/events/"

def create_event():
    data = {
        "title": "Automated Test Event",
        "location": "London",
        "description": "This is a test event",
        "date": "2025-12-31T10:00:00"
    }
    response = requests.post(BASE_URL, json=data)
    print("CREATE:", response.status_code, response.json())
    return response.json()["id"]

def get_event(event_id):
    response = requests.get(BASE_URL + str(event_id))
    print("GET:", response.status_code, response.json())

def list_events():
    response = requests.get(BASE_URL)
    print("LIST:", response.status_code, response.json())

def update_event(event_id):
    data = {
        "title": "Updated Test Event",
        "location": "Berlin",
        "description": "Updated description",
        "date": "2025-12-31T12:00:00"
    }
    response = requests.put(BASE_URL + str(event_id), json=data)
    print("UPDATE:", response.status_code, response.json())

def delete_event(event_id):
    response = requests.delete(BASE_URL + str(event_id))
    print("DELETE:", response.status_code, response.json())

if __name__ == "__main__":
    # 1. Create
    event_id = create_event()
    
    # 2. Get by ID
    get_event(event_id)
    
    # 3. List all events
    list_events()
    
    # 4. Update
    update_event(event_id)
    
    # 5. Get updated
    get_event(event_id)
    
    # 6. Delete
    delete_event(event_id)
    
    # 7. List all events again
    list_events()
