import requests

# TEST REQUEST GET DARI https://requestbin.com/
# r = requests.get('https://0453541974205687xxxxxx.m.pipedream.net')


########### SINGLE USER ###########
# {
#     "data": {
#         "id": 2,
#         "email": "janet.weaver@reqres.in",
#         "first_name": "Janet",
#         "last_name": "Weaver",
#         "avatar": "https://reqres.in/img/faces/2-image.jpg"
#     },
#     "support": {
#         "url": "https://reqres.in/#support-heading",
#         "text": "To keep ReqRes free, contributions towards server costs are appreciated!"
#     }
# }


r = requests.get('https://reqres.in/api/users/2')
# print(r) #output :<Response [200]>

# print(r.text) #Ini parse as text dengan hasil sebuah respon yang bisa di print dalam bentuk text

# a = r.text
# print(type(a)) #output : <class 'str'> 

# print(r.json()) #Ini outputnya json, parse as json

# json_data = r.json()
# print(json_data['data']) #outputnya semua value dengan key "data":[{...},{...},{...}]
# print(json_data['data']['first_name']) #outputnya Janet , first_name dari "data":{} 



########### LIST USER ###########

# {
#     "page": 2,
#     "per_page": 6,
#     "total": 12,
#     "total_pages": 2,
#     "data": [
#         {
#             "id": 7,
#             "email": "michael.lawson@reqres.in",
#             "first_name": "Michael",
#             "last_name": "Lawson",
#             "avatar": "https://reqres.in/img/faces/7-image.jpg"
#         },
#         {
#             "id": 8,
#             "email": "lindsay.ferguson@reqres.in",
#             "first_name": "Lindsay",
#             "last_name": "Ferguson",
#             "avatar": "https://reqres.in/img/faces/8-image.jpg"
#         }
#     ],
#     "support": {
#         "url": "https://reqres.in/#support-heading",
#         "text": "To keep ReqRes free, contributions towards server costs are appreciated!"
#     }
# }


r = requests.get('https://reqres.in/api/users?page=2')

json_data = r.json()
print(json_data['data']) #outputnya List dengan key "data":[{...},{...},{...}]
print(json_data['data'][1]) #outputnya Dict untuk List Pertama untuk itu List bisanya pakai Int