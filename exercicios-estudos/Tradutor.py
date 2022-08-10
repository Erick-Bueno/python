import requests

url = "https://google-translate1.p.rapidapi.com/language/translate/v2"

payload = "q=Hello%2C%20world!&target=es&source=en"
headers = {
	"content-type": "application/x-www-form-urlencoded",
	"X-RapidAPI-Key": "a589e5a925msh3a6bfbb245ec5bap1693b2jsn05fad2b8a64a",
	"X-RapidAPI-Host": "google-translate1.p.rapidapi.com"
}

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)