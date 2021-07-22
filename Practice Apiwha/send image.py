import requests

url = "https://panel.apiwha.com/send_message.php"

querystring = {"apikey":"UT06JL95PBKxxxx","number":"+62812xxx","text":"TEST"}

response = requests.request("GET", url, params=querystring)

print(response.text)