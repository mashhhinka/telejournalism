import requests

# URL of your FastAPI endpoint
url = "http://127.0.0.1:8080/correspondents/"

# Data to add
data = {
    "name": "Alice Smith",
    "email": "alice@example.com"
}

# Send POST request
response = requests.post(url, json=data)

# Print response from the server
print(response.json())
