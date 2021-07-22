import requests
import json

headers = {"apikey": "7d095362a7c0410xxxxxxxx", "Content-Type": "application/json"}

data = {
  "id": "ef43657dbb314e7xxxxxx",
  "title": "TEST",
  "destination": "https://www.udemy.com/",
  "shortUrl": "ptpp.link/testajadeh"
}
#Oooo dia gak bisa nerima dalam bentuk json paramaternya malah harus ubah ke string dulu
test=json.dumps(data)

# r = requests.get('https://api.rebrandly.com/v1/links?orderBy=createdAt&orderDir=desc&limit=100&favourite=false&status=active&domain[id]=cc7db70fec03413f8f2xxxxx', headers=headers)

# r = requests.get('https://api.rebrandly.com/v1/links/ef43657dbb314e7xxxxxx', headers=headers)

# r = json.dumps
# print(r.text)

#kirim parameter ke rebrandly
updatelink = requests.post("https://api.rebrandly.com/v1/links/ef43657dbb314e7xxxxxx", headers=headers, data=test)

print(updatelink.text)

