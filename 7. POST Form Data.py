import requests

payload = {'name':'Adithya', 'location':'Bogor'}

#data untuk form data
#nanti pada headers content-type: application/x-www-form-urlencoded

# r = requests.post('https://045354197420568719925a9dab84db45.m.pipedream.net', data=payload)

r = requests.post('https://httpbin.org/post', data=payload)

#print response dalam bentuk text
# print(r.text)

# RESPONSE :
# {
#   "args": {},
#   "data": "",
#   "files": {},
#   "form": {
#     "location": "Bogor",
#     "name": "Adithya"
#   },
#   "headers": {
#     "Accept": "*/*",
#     "Accept-Encoding": "gzip, deflate",
#     "Content-Length": "27",
#     "Content-Type": "application/x-www-form-urlencoded",
#     "Host": "httpbin.org",
#     "User-Agent": "python-requests/2.25.0",
#     "X-Amzn-Trace-Id": "Root=1-5fca5a16-478527c95dbfe1175d9261b7"        
#   },
#   "json": null,
#   "origin": "110.138.151.63",
#   "url": "https://httpbin.org/post"
# }

# CUMA EMANG GAK COMMON DIPAKAI