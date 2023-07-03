import requests

URL_JSON = "https://jsonplaceholder.typicode.com/todos/1"
response = requests.get(URL_JSON)
if(response.status_code == 200):
    print(response.json())