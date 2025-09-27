from flask import Flask, render_template, request, jsonify
import requests

API_KEY = "eyJvcmciOiI1YjNjZTM1OTc4NTExMTAwMDFjZjYyNDgiLCJpZCI6IjdhNWUzYmMxYjA1NjRhZTZiMGMzNDgzNWVjZWNiM2I5IiwiaCI6Im11cm11cjY0In0="

start = [40.7128, -74.0060]  
end = [40.7612, -73.9822] 

routeData = {
    "coordinates": [[start[1], start[0]], [end[1], end[0]]]
}

url = "https://api.openrouteservice.org/v2/directions/foot-walking"

headers = {
    "Authorization": API_KEY, 
    "Content-Type": "application/json"
}

response = requests.post(url, json=routeData, headers=headers)
data = response.json()

print(data)

#routeSummary = data['']
#durationInSeconds = data['']
