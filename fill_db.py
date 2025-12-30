import requests

# URL of your correspondents endpoint
url = "http://127.0.0.1:8080/correspondents/"

# Generate 50 dummy correspondents
for i in range(1, 51):
    data = {
        "name": f"Correspondent {i}",
        "email": f"user{i}@example.com"
    }

    try:
        response = requests.post(url, json=data)
        if response.status_code == 200:
            print(f"Added: {response.json()}")
        else:
            print(f"Failed to add {data['name']}: {response.text}")
    except requests.exceptions.RequestException as e:
        print(f"Error adding {data['name']}: {e}")
