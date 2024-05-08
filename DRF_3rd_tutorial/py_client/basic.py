import requests

#endpoint = "http://httpbin.org/anything"
endpoint = "http://localhost:8000/api/"   #"http://127.0.0.1:8000"

get_response = requests.post(endpoint, json={"title":"hi bitch","content":"im good"})
print(get_response.headers)

#print(get_response.text)
print(get_response.json())
#print(get_response.status_code)
#print(get_response.text)

