import requests

files = {'file':('cat.jpg', open('cat.jpg','rb'), 'image/jpeg')}
r = requests.post('https://045354197420568719925a9dab84db45.m.pipedream.net', files=files)


# CUMA EMANG GAK COMMON DIPAKAI, BIASANYA ADA CARA LEBIH MUDAH DI DOKUMENTASI APINYA
#UNTUK CEK MEDIA TYPE :
# https://developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/MIME_types#:~:text=A%20media%20type%20(also%20known,standardized%20in%20IETF's%20RFC%206838.