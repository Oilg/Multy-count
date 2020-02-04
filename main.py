import requests, json

def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

response = requests.get("http://iss.moex.com/iss/securities.json")
jprint(response.json())
