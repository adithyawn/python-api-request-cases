import requests
from requests.auth import HTTPBasicAuth

url = 'https://api.twilio.com/2010-04-01/Accounts/AC8e7f05edff49fe3dd300892ef5949f03/Messages.json'

auth = HTTPBasicAuth('AC8e7f05edff49fe3dd300892ef5949f03','6c05c0c7381514784ca91df06b2e0879')

data = {'To':'+6281266781105', 'From':'+12515517458', 'Body':'Hello from Request API'}

r = requests.post(url, auth=auth, data=data)

print(r.text)

# referensi : https://www.twilio.com/docs/sms/send-messages