###############################################################
j
# This program:
# - Asks the user to enter an access token or use the hard coded access token.
# - Lists the user's Webex rooms.
# - Asks the user which Webex room to monitor for "/seconds" of requests.
# - Monitors the selected Webex Team room every second for "/seconds" messages.
# - Discovers GPS coordinates of the ISS flyover using ISS API.
# - Display the geographical location using geolocation API based on the GP coordinates.
# - Formats and sends the results back to the Webex Team room.





# 1. Import libraries for API requests, JSON formatting, epoch time conversion, and iso3166.
import requests
import json
import time
from iso3166 import countries




# 2. Complete the if statement to ask the user for the Webex access token.
choice = input("Do you wish to use the hard-coded Webex token? (y/n) ")
if choice.lower() == 'n':
    token_input = input("Enter your webex access token (do not include 'Bearer '): ")
    if not token_input:
        raise Exception("No token provided. Exiting.")
    accessToken = "Bearer " + token_input

else:
    accessToken = "Bearer:Y2FjZTZlOTUtMTdiZS00MmQyLTlkODktNmYzOGYxNTZhNWM4NTJmMWY1N2UtNGJh_P0A1_636b97a0-b0af-4297-b0e7-480dd517b3f9"
    # 3. Provide the URL to the Webex room API.




r = requests.get("https://webexapis.com/v1/rooms",headers = {"Authorization": accessToken})


#######################################################################################
# DO NOT EDIT ANY BLOCKS WITH r.status_code
if not r.status_code == 200:
    raise Exception("Incorrect reply from Webex API. Status code: {}. Text: {}".format(r.status_code, r.text))
#######################################################################################


# 4. Create a loop to print the type and title of each room.
print("\nList of available rooms:")
rooms = r.json()["items"]
for room in rooms:
     print(" -Type:{} | Title:{}".format(room.get("type",""), room.get("title", "")) )

#######################################################################################
# SEARCH FOR WEBEX ROOM TO MONITOR
# - Searches for user-supplied room name.
# - If found, print "found" message, else prints error.
# - Stores values for later use by bot.
# DO NOT EDIT CODE IN THIS BLOCK
#######################################################################################

# Prompt until a room with a matching substring is found 
while True:
    roomNameToSearch = input("Which room should be monitored for the /seconds messages? ")
    roomIdToGetMessages = None
    roomTitleToGetMessages = None
    
    for room in rooms:
        if(room["title"].find(roomNameToSearch) != -1):
            print ("Found rooms with the word " + roomNameToSearch)
            print(room["title"])
            roomIdToGetMessages = room["id"]
            roomTitleToGetMessages = room["title"]
            print("Found room: " + roomTitleToGetMessages)
            break
    
    if(roomIdToGetMessages == None):
        print("Sorry, I didn't find any room with " + roomNameToSearch + " in it.")
        print("Please try again...")
        #loop continues until a valid room is found
    else:
        #while loop is exited and proceeds to bot code
         break
######################################################################################
# WEBEX BOT CODE
# Starts Webex bot to listen for and respond to /seconds messages.
######################################################################################

messages_url = "https://webexapis.com/v1/messages"
print("/nMonitoring room '{}' for commands like /3 or /5...".format(roomTitleToGetMessages))

seconds = 1

while True:
    try:
        time.sleep(1)

        GetParameters = {
            "roomId": roomIdToGetMessages,
            "max": 1
        }

        # 5. Provide the URL to the Webex messages API.
        r = requests.get(messages_url,params = GetParameters,headers = {"Authorization": accessToken})
        
        # verify if the retuned HTTP status code is 200/OK
        if not r.status_code == 200:
            raise Exception( "Incorrect reply from Webex API. Status code: {}. Text: {}".format(r.status_code, r.text))

        json_data = r.json()
        if len(json_data["items"]) == 0:
            continue
        
        messages = json_data["items"]
        message = messages[0]["text"]
        print("received message text: '{}'".format(message))

        if message.strip().lower() == "stop":
            print("Stop command received. Exiting.")
            break


        if message.find("/") == 0:
            if (message[1:].isdigit()):
                seconds = int(message[1:])
            else:
                print("command after '/' is not a numeric value.")
                continue
        else:
            continue


        #for the sake of testing, the max number of seconds is set to 5.
        if seconds > 5:
            print("Requested secdonds > 5;capping to 5 for safety/testing")
            seconds = 5


        print("Sleeping for {} seconds...".format(seconds))
        time.sleep(seconds)

        # 6. Provide the URL to the ISS Current Location API.
        iss_url = "http://api.open-notify.org/iss-now.json"
        r = requests.get(iss_url, timeout=10)
        json_data = r.json()
        if not r.status_code == 200 or json_data.get("message") != "success":
            print("Error retrieving ISS position: status {}, response: {}".format(r.status_code, r.text))
            continue


        # 7. Record the ISS GPS coordinates and timestamp.
        lat = json_data["iss_position"]["latitude"]
        lng = json_data["iss_position"]["longitude"]
        timestamp = json_data["timestamp"]

    except KeyboardInterrupt:
        print("Program interrupted by user. Exiting.")
        break

    except Exception as e:
        print(f"Error:{e}")
        continue


# 8. Convert the timestamp epoch value to a human readable date and time.
# Use the time.ctime function to convert the timestamp to a human readable date and time.
timeString = time.ctime(int(timestamp))


# 9. Provide your Geoloaction API consumer key.
locationiq_api_key = "pk.32999e45fa4408225c58c949d08046ef"
mapsAPIurl = "https://us1.locationiq.com/v1/reverse?"
mapsAPIGetParameters = {
    'key': locationiq_api_key,
    'lat': lat,
    'lon': lng,
    'format': 'json'
}


# 10. Provide the URL to the Reverse GeoCode API.
r = requests.get(mapsAPIurl, params=mapsAPIGetParameters, timeout=10)

# Verify if the returned JSON data from the API service are OK
try:
    json_data = r.json()
except json.JSONDecodeError:
    print("Error: failed to decode JSON response from Geolocation API.")
    json_data = {}
finally:
    print("Geolocation API response status code: {}".format(r.status_code))


if not json_data or "address" not in json_data:
    print("Warning: No address data found in Geolocation API response.")
    address = {}
else:
    address = json_data["address"]




# 11. Store the location received from the API in a required variables
CountryResult = json_data["state"]
CountryResult = (address.get("country_code") or "XZ").upper()
StateResult = address.get("state") or address.get("country") or ""
CityResult = address.get("city") or address.get("town") or address.get("village") or ""

StreetResult = ""
if address.get("house_number"):
    StreetResult += address.get("house_number") + " "
if address.get("road"):
    StreetResult += address.get("road")

#Find the country name using ISO3611 country code
if not CountryResult == "XZ":
    try:
        CountryResult = countries.get(CountryResult).name
    except KeyError:
        pass #keep the original code if the country code is not found


# 12. Complete the code to format the response message.
# Example responseMessage result: In Austin, Texas the ISS will fly over on Thu Jun 18 18:42:36 2020 for 242 seconds.

if CountryResult == "XZ":
    responseMessage = "On {}, the ISS was flying over a body of water at latitude {}° and longitude {}°.".format(timeString, lat, lng)
else:
    if StreetResult:  # street info available
        responseMessage = "On {}, the ISS was flying over:\n{} \n{}, {} \n{} \n(latitude: {}°, longitude: {}°)".format(timeString, StreetResult, CityResult, StateResult, CountryResult, lat, lng)
    elif CityResult or StateResult:  # city/state available
        responseMessage = "On {}, the ISS was flying over {}, {} ({}) at latitude {}° and longitude {}°.".format(timeString, CityResult, StateResult, CountryResult, lat, lng)
    else:  # only country available
        responseMessage = "On {}, the ISS was flying over {} at latitude {}° and longitude {}°.".format(timeString, CountryResult, lat, lng)

# print the response message
print("Sending to Webex: " + responseMessage)

# 13. Complete the code to post the message to the Webex room.
HTTPHeaders = {
    "Authorization": accessToken,  # previously defined Webex Bearer token
    "Content-Type": "application/json"
}
PostData = {
    "roomId": roomIdToGetMessages,
    "text": responseMessage
}

# Post the call to the Webex message API.
r = requests.post(
    "https://webexapis.com/v1/messages",  # Webex POST messages API
    data=json.dumps(PostData),
    headers=HTTPHeaders,
    timeout=10
)

# Error handling in case request not successful
if r.status_code not in (200, 201):
    print("Failed to post message to Webex. Status: {}, Text: {}".format(r.status_code, r.text))
else:
    print("Message posted successfully to the room.")
