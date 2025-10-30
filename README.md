# spacebot
A space bot to track the iss. Users can interact with the bot to find specific measurements of where it is.

Page
1
of 2
# 🚀 Space Bot API Investigation Sheet
**Total Marks: 30**
**Part 1: Collect Required API Documentation**
This investigation sheet helps you gather key technical information from the three
APIs required for the Space Bot project: **Webex Messaging API**, **ISS Current
Location API**, and a **Geocoding API** (LocationIQ or Mapbox or other), plus the
Python time module.
---
## Section 1: Webex Messaging API (7 marks)✅
| Criteria | Details |
|---------|---------|
| API Base URL |  https://webexapis.com/v1/ |
| Authentication Method | Bot Access Token ( Authorisation: (token)) |
| Endpoint to list rooms | GET /rooms |
| Endpoint to get messages | GET /messages?roomId=(roomId)&max=50 |
| Endpoint to send message |  POST /messages |
| Required headers | Authorization: Bearer(ACCESS_TOKEN) Content-Type: application/json |
| Sample full GET or POST request | 1) List room:
                                       Method: GET
                                       URL: https://webexapis.com/v1/rooms
                                       Headers: Authorization: Bearer <YOUR_BOT_ACCESS_TOKEN>
                                       Expected response (JSON):
                                       json { "items": [ {"id":"Y21z...","title":"General"}
                                       {"id":"Y21z...""title":"Test Room"}]} 
                                    2) Method: POST
                                       URL: https://webexapis.com/v1/messages
                                       Headers: Authorisation: Bearer <bot_access_token>
                                       Body (raw JSON):
                                       json {"roomId":"<Room_Id>","text":"Hello from Space Bot!"}|
                                    
---
## Section 2: ISS Current Location API (3 marks)
| Criteria | Details |
|---------|---------|
| API Base URL | http://api.open-notify.org |
| Endpoint for current ISS location | GET /iss-now.json |
| Sample postman request (JSON) |
                                Method: GET
                                URL: http://api.open-notify.org/iss-now.json
                                Expected response: {"timestamp":1761819623,
                                                     "message":"success",
                                                     "iss_position":{
                                                         "latitude": "-26.4762",
                                                         "longitude": "6.0396"
                                                         }
                                                         }|
```
```
|
---
## Section 3: Geocoding API (LocationIQ or Mapbox or other) 
| Criteria | Details |
|---------|---------|
| Provider used (circle one) | **LocationIQ** |
| API Base URL | https://eu1.locationiq.com/v1 |
| Endpoint for reverse geocoding | GET /reverse.php |
| Authentication method | API Key (query parameter key=<API_KEY>) |
| Required query parameters | key = LocationIQ API key lat = latitude lon = longitude format = json |
| Sample request with latitude/longitude | Method: Get URL:
   https://us1.locationiq.com/v1/reverse.php?key=     <API_KEY>&lat=40.78484&lon=-73.9857&format=json |
| Sample JSON response (formatted example): json { "place_id":123456789, "licence":"https://locationiq.com/attribution",
"osm_type":"way",
"osm_id":"34633854",
"lat":"40.74844205",
"lon":"-73.98565890160751",
"display_name":"Empire State Building, 350, 5th Avenue, Koreatown, Manhattan, New York Country, New York, New York, 10001, USA",
"address": {
        "attraction": "Empire State Building",
        "house_number": "350",
        "road": "5th Avenue",
        "neighbourhood": "Koreatown",
        "suburb": "Manhattan",
        "county": "New York County",
        "city": "New York",
        "state": "New York",
        "postcode": "10001",
        "country": "United States of America",
        "country_code": "us"
    },
    "boundingbox": [
        "40.7479255",
        "40.7489585",
        "-73.9865012",
        "-73.9848166"
    ]
}
|
```
```
|
---
## 🚀 Section 4: Epoch to Human Time Conversion (Python time module) (2 marks)
| Criteria | Details |
|---------|---------|
| Library used | `_______________________________` |
| Function used to convert epoch | `_______________________________` |
| Sample code to convert timestamp |
```
```
|
| Output (human-readable time) | `_______________________________` |
---
## 🚀 Section 5: Web Architecture & MVC Design Pattern (12 marks)
### 🚀 Web Architecture – Client-Server Model
- **Client**:
- **Server**:
- (Explain the communication between them & include a block diagram )
### 🚀 RESTful API Usage
-
-
-
### 🚀 MVC Pattern in Space Bot
| Component | Description |
|------------|-------------|
| **Model** | |
| **View** | |
| **Controller** | |
#### Example:
- Model:
- View:
- Controller:
---
### 🚀 Notes
- Use official documentation for accuracy (e.g. developer.webex.com, locationiq.com
or Mapbox, open-notify.org or other ISS API).
- Be prepared to explain your findings to your instructor or demo how you retrieved
them using tools like Postman, Curl, or Python scripts.
---
### Total: /30✅

