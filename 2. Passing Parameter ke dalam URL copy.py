import requests

# r = requests.get('https://045354197420568719925a9dab84db45.m.pipedream.net?key1=value1&key2=value2')

# output di https pipelines GET query:
# {"key1":"value1","key2":"value2"}


payload = {'first':'one','second':'two'}

r = requests.get('https://045354197420568719925a9dab84db45.m.pipedream.net', params=payload)

# output di https :
# {"first":"one","second":"two"}