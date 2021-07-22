import json

PythonDict = {
  "name": "messenger",
  "playstore": True,
  "company": "Facebook",
  "price": 100
}

print(PythonDict)

print(type(PythonDict))

DictToString = json.dumps(PythonDict)

print(DictToString)

print(type(DictToString))

StringToDictOrJSON = json.loads(DictToString)

print(StringToDictOrJSON)

print(type(StringToDictOrJSON))

#CATATAN : DICTIONARY DAN JSON SAMA AJA OBJECT