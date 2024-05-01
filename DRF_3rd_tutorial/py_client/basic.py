import requests

endpoint = "http://httpbin.org/Status_codes/patch_status__codes_"
endpoint = "http://httpbin.org/anything"

get_response = requests.get(endpoint, json={"query":"hi bitch"})
#print(get_response.text)
print(get_response.json())
print(get_response.status_code)

