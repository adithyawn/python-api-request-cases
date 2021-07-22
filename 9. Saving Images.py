import requests

r = requests.get('http://httpbin.org/image/jpeg')
print(r.headers)

with open('image.jpg', 'wb') as fd:
    for chunk in r.iter_content(chunk_size=500):
        fd.write(chunk)

#memecah file gambar menjadi chunk