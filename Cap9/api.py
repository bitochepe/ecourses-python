import requests

url = "https://spotify23.p.rapidapi.com/user_profile/"

querystring = {"id":"usuarioaca"}

headers = {
	"X-RapidAPI-Key": "Utilizar su key de rapid api",
	"X-RapidAPI-Host": "spotify23.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)