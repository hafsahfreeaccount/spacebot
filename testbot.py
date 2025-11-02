import requests

url = "https://webexapis.com/v1/messages"
headers = {
    "Authorization": "Bearer YOUR_ACCESS_TOKEN",
    "Content-Type": "application/json"
}
data = {
    "roomId": "Y2lzY29zcGFyazovL3VzL1JPT00vMTIzNDU2Nzg5",
    "text": "Hello from Python via Webex!"
}

response = requests.post(url, headers=headers, json=data)
print(response.json())