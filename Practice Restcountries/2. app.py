import requests

base_url = 'https://restcountries.eu/rest/v2/'

print('What information do you want about a country? Choose one')
print('1. Population')
print('2. Languages')
print('3. Timezones')

option = input(' ')

country = input('what country do you want that information for? ')
print(country)

'''
Parameter itu sesuatu yang ada di belakang tanda ?
Contoh:
https://restcountries.eu/rest/v2/name/{name}?fullText=true
https://restcountries.eu/rest/v2/{service}?fields={field};{field};{field}
Kalo yg sebelum tanda tanya gak bisa pakai parameter
Contoh:
https://restcountries.eu/rest/v2/name/{name} , ini bisa pakai input manual
'''

params = {'fields':'population;languages;timezones', 'fullText' :'true'}

#ini untuk send response sesuai nama country dan parameter
r = requests.get(base_url + 'name/{}'.format(country), params=params)

json_response = r.json()

'''
OUTPUT :
[{'languages': [{'iso639_1': 'nl', 'iso639_2': 'nld', 'name': 'Dutch', 'nativeName': 'Nederlands'}, {'iso639_1': 'pa', 'iso639_2': 'pan', 'name': '(Eastern) Punjabi', 'nativeName': 'ਪੰਜਾਬੀ'}], 'population': 107394, 'ti
mezones': ['UTC-04:00']}]
'''


json_response = r.json()

country = None #KENAPA PAKAI INI YA BIAR GAK ERROR?

try:
    country = json_response[0]
except KeyError:
    print('Country Not Found')

if country :
    if option == '1' :
        population = country['population']
        print('Population is {}.'.format(population)) #print(json_response[0]['population'])


    elif option == '2':
        #CARA LOOP DICTIONARY [{'name':'...'},{'name':'...'},{'name':'...'}]
        langs = []
        for language  in country['languages']: #for language in json_response[0]['languages']loop['name]
            langs.append(language['name']) #tambahkan dictionary {'name':'...'} ke langs
        print(langs) #output : ['Dutch', '(Eastern) Punjabi']
        print('Languages are {}.'.format(langs)) #output : Languages are ['Dutch', '(Eastern) Punjabi'].
        print('Languages are {}.'.format(', '.join(langs))) #output : Languages are Dutch, (Eastern) Punjabi.

    else :
        #LOOP LIST MENJADI STRING
        print('Timezones are {}.'.format(', '.join(country['timezones'])))
        #join untuk keluarkan dari [] di json bentuknya ['a','b','c']

'''    
CARA MANUAL
elif option == '2' :
    languages = country['languages'][0]['name']
    print('Languages is {}.'.format(languages)) #print(json_response[0]['languages'])
'''