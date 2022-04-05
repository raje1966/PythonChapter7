#converting python object to Json data and into a file
import json

person = {"name":"John","age":30,"city":"New York","hasChildren":False,"titles":["engineers","programmer"]}
with open('person.json','w') as file:
    json.dump(person,file, indent=4)