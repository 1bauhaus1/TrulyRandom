import requests

API_URL = "https://api.quantumnumbers.anu.edu.au"
API_KEY = "DcdHZyNZEF4k2nk70oISm3PvgRLWirpa564ethoz"

params = {
    "length": 5,
    "type": "uint16"
}

headers = {
    "x-api-key": API_KEY
}

response = requests.get(API_URL, params=params, headers=headers)

if response.status_code == 200:
    data = response.json()
    numbers = data["data"]
    print("Quantum random numbers:", numbers)

    # Create CLEAN version
    clean_string = ''.join(str(n) for n in numbers)
    print("CLEAN:", clean_string)

else:
    print("Error:", response.status_code, response.text)