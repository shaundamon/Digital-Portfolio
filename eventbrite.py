# import requests
# import json

# # Replace with your Eventbrite API Key
# api_key = 'K7ZOUFRRJGZ2WT25YR'

# url = 'https://www.eventbriteapi.com/v3/events/search/'
# headers = {'Authorization': f'Bearer {api_key}'}

# # Make the API request
# response = requests.get(url, headers=headers)

# # Check for a successful response
# if response.status_code == 200:
#     # Pretty print the JSON response to inspect the fields
#     print(json.dumps(response.json(), indent=4))
# else:
#     print(f'Failed to get data: {response.content}')
# import requests
# import json

# # Set up the API endpoint and headers
# url = "https://www.eventbriteapi.com/v3/organizations/YOUR_ORGANIZATION_ID/events/"
# headers = {
#     'Authorization': 'Bearer YOUR_PERSONAL_OAUTH_TOKEN',
# }

# # Make the API request
# response = requests.get(url, headers=headers)

# # Check if the request was successful
# if response.status_code == 200:
#     events = json.loads(response.text)
#     print(json.dumps(events, indent=4))
# else:
#     print(f"Failed to get data: {response.text}")

# import requests
# import json

# def fetch_meetup_events():
#     api_url = 'https://api.meetup.com/find/events'
#     headers = {
#         'Authorization': 'Bearer 2QVQWLbTKlcSJrQHXd3aRoohT57ptnmBWAnhbt34',
#         'Accept': 'application/json'
#     }
#     params = {
#         'location': 'South Africa',
#         'page': 10  # Number of events to fetch
#     }
    
#     response = requests.get(api_url, headers=headers, params=params)
    
#     print(f"Status Code: {response.status_code}")  # Debugging line
#     print(f"Response: {response.content}")  # Debugging line
    
#     if response.status_code == 200:
#         return response.json()
#     else:
#         return None

# # Fetch and print the events
# events = fetch_meetup_events()
# if events:
#     print(json.dumps(events, indent=4))
# else:
#     print("Failed to fetch events.")

import requests

url = "https://api.predicthq.com/v1/events/"
headers = {
    "Authorization": f"Bearer 2QVQWLbTKlcSJrQHXd3aRoohT57ptnmBWAnhbt34"
}
params = {
    "active.gte": "2023-01-01",
    "active.lte": "2023-12-31",
    "category": "sports,concerts",
    "limit": 10
}

response = requests.get(url, headers=headers, params=params)
data = response.json()
print(response)
print(data)

# Process data as needed
