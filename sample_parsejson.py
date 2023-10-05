import json

#sample json
x = '{"name":" RJ", "age: " :"25", "city" : "Manila"}'

#parse json

y=json.loads(x)
print("The output of the json file is", y)
print("Name", y ["name"])