import requests
from requests.auth import HTTPBasicAuth

# TEST RESPONSE
# r = requests.get('https://httpbin.org/basic-auth/user/passwd')
#KALAU TIDAK MUNCUL APA - APA, COBA PRINT RESPONSE
# print(r)

r = requests.get('https://httpbin.org/basic-auth/adithya/passwd', auth=HTTPBasicAuth('adithya','passwd'))
print(r)

# KALO GAK TERAUTENTIFIKASI RESPONSE 404
# KALO BERHASIL RESPONSE 200