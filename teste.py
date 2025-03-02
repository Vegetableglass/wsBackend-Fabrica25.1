import requests
name = "Earth"
url = f"https://rickandmortyapi.com/api/location?name={name}"
response = requests.get(url)
dados = response.json()
print (dados)
