import requests

url = "https://panel.apiwha.com/send_message.php"

querystring = {"apikey":"xxxxx","number":"+xxxxx","text":"http://personal.psu.edu/xqz5228/jpg.jpg"}

response = requests.request("GET", url, params=querystring)

print(response.text)