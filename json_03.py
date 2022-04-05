#converting json data into a dictionary
import json
person = {"name":"John","age":30,"city":"New York","hasChildren":False,"titles":["engineers","programmer"]}
personJSON=json.dumps(person,indent=4,sort_keys=True)
# print(personJSON)
with open('person.json','r') as file:
    person= json.load(file)
    print(person)