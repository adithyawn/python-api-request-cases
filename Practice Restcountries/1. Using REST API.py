import requests

base_url = 'https://restcountries.eu/rest/v2/'

'''
r = requests.get(base_url + 'all')

# print(r) #cek respon aja
# print(r.text)

json_result = r.json() #untuk convert text ke json object sehingga di python bisa terbaca sebagai OBJECT (list atau dictionary). Kalo respon jsonnya dimulai dengan [] array di python terbaca sebagai list. Kalo respon jsonnya dimulai dengan {} di python terbaca sebagai dictionary. Pada case ini json_result[84]['name'] output berupa string dengan nama 'germany'

print(json_result[84]['name'])
#OUTPUT : Germany

print(json_result[84]['subregion'])
#OUTPUT : Western Europe
'''

'''
#Kalau mau pakai filter:
# https://restcountries.eu/rest/v2/{service}?fields={field};{field};{field}
# https://restcountries.eu/rest/v2/all?fields=name;capital;currencies

#fields-nya case sensitive
r = requests.get(base_url + 'name/can?fields=name;altSpellings')
print(r.json())

#Dengan cara passing parameter
fields = {'fields' : 'altSpellings;name'}
r = requests.get(base_url + 'name/can?', params=fields)

OUTPUT:
[{'name': 'American Samoa', 'altSpellings': ['AS', 'Amerika Sāmoa', 'Amelika Sāmoa', 'Sāmoa Amelika']}, {'name': 'Canada', 'altSpellings': ['CA']}, {'name': 'Central African Republic', 'altSpellings': ['CF', 'Central African Republic', 'République centrafricaine']}, {'name': 'Dominican Republic', 'altSpellings': ['DO']}, {'name': 'Azerbaijan', 'altSpellings': ['AZ', 'Republic of Azerbaijan', 'Azərbaycan Respublikası']}, {'name': 'Virgin Islands (U.S.)', 'altSpellings': ['VI', 'USVI', 'American Virgin Islands', 'U.S. Virgin Islands']}, {'name': 'Holy See', 'altSpellings': ['Sancta Sedes', 'Vatican', 'The Vatican']}, {'name': 'Mexico', 'altSpellings': ['MX', 'Mexicanos', 'United Mexican States', 'Estados Unidos Mexicanos']}]
'''

'''
fields = {'fields':'name;currencies'}
r = requests.get(base_url + 'capital/london', params=fields)

print(r.json())

OUTPUT :
[{'currencies': [{'code': 'GBP', 'name': 'British pound', 'symbol': '£'}], 'name': 'United Kingdom of Great Britain and Northern Ireland'}]      
'''