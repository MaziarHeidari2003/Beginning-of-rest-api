import requests

#endpoint = "http://httpbin.org/anything"
endpoint = "http://localhost:8000/api/products/create/"   #"http://127.0.0.1:8000"


data = {
  "title":"this is the title",
  "price":354.48
}

get_response = requests.post(endpoint, json=data)
print(get_response.json())
