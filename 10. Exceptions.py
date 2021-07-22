import requests

# r = requests.get('https://httpbin.org/status/404') #/status/{codes}
# print(r) #<Response [404]>
# r.raise_for_status()

#kalo status/404 requests.exceptions.HTTPError, kalo status/200 tanpa keterangan hanya print Response[200] artinya sukses

# r = requests.get('https://httpbin.org/status/404')

# try:
#     r.raise_for_status()
# except requests.exceptions.HTTPError:
#     print('ERRORR ERRORRR ERORRRR')

# print(r)

# OUTPUT:
# ERRORR ERRORRR ERORRRR
# <Response [400]>


try:
    r = requests.get('https://dgdgdfgr.com')
except requests.exceptions.ConnectionError:
    print('CONNECTION ERROR!')



# ANOTHER METHOD FROM STACKOVER FLOW:
# try:
#     r = requests.get('http://www.google.com/nothere')
#     r.raise_for_status()
# except requests.exceptions.HTTPError as err:
#     raise SystemExit(err)