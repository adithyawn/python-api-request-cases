import requests

# BUAT CEK EXCEPTIONNYA APA, HABIS ITU DI COPY
# r = requests.get('https://httpbin.org/', timeout=100)

try:
    r = requests.get('https://httpbin.org/', timeout=0.1)
except requests.exceptions.ConnectTimeout:
    print('TIMED OUT!!')