import requests

API_KEY = "eyJvcmciOiI1YjNjZTM1OTc4NTExMTAwMDFjZjYyNDgiLCJpZCI6IjdhNWUzYmMxYjA1NjRhZTZiMGMzNDgzNWVjZWNiM2I5IiwiaCI6Im11cm11cjY0In0="

def building_to_location(building_name):
    gurl = "https://api.openrouteservice.org/geocode/search"
    parameters = {
        "api_key": API_KEY,
        "text": building_name,
        "size": 1
    }

    response = requests.get(gurl, params=parameters)
    data = response.json()

    try:
        coordinates = data['features'][0]['geometry']['coordinates']
        return coordinates[1], coordinates[0]

    except (KeyError, IndexError):
        print(f"Could not geocode the location: {building_name}")

def get_walking_duration(start, end):
    rurl = "https://api.openrouteservice.org/v2/directions/foot-walking"
    routeData = {
            "coordinates": [[start[1], start[0]], [end[1], end[0]]]
        }

    headers = {
        "Authorization": API_KEY, 
        "Content-Type": "application/json"
    }

    response = requests.post(rurl, json=routeData, headers=headers)
    data = response.json() 

    try:
        duration = data['routes'][0]['summary']['duration']
        minutes = round(duration // 60, 2)
        print(f"Estimated walking time: {minutes} minutes")

    except (KeyError, IndexError):
        print("Error: Could not extract duration from response data.")


start_name = input("Enter starting building name: ")
end_name = input("Enter destination building name: ")

start_coords = building_to_location(start_name)
end_coords = building_to_location(end_name)

if start_coords and end_coords:
    get_walking_duration(start_coords, end_coords)      

else:
    print("Could not retrieve coordinates for one or both locations.")
