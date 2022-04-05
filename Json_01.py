import json


# How to convert a python file to json
import json
person = {"name":"John","age":30,"city":"New York","hasChildren":False,"titles":["engineers","programmer"]}
personJSON=json.dumps(person,indent=4,sort_keys=True)
print(personJSON)