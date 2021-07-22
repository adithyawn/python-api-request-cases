import requests
from requests.auth import HTTPBasicAuth

url = 'https://api.twilio.com/2010-04-01/Accounts/AC8e7f05edff49fe3dd300892ef5949f03/Messages.json'

auth = HTTPBasicAuth('AC8e7f05edff49fe3dd300892ef5949f03','6c05c0c7381514784ca91df06b2e0879')

message = input('Masukan pesan !')

#harus pakai nomer sandbox kalo trial WA twilio
data = {'To':'whatsapp:+6281266781105', 'From':'whatsapp:+14155238886', 'Body':message}

r = requests.post(url, auth=auth, data=data)

print(r.text)

#refernsi : https://www.twilio.com/docs/whatsapp/quickstart/curl