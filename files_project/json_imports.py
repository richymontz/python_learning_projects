import json

with open('friends_json.txt', 'r') as file:
    file_contents = json.load(file)  # this returns a Dictionary

print(file_contents['friends'][0])

cars = [
    {'make': 'Kia', 'model': 'Forte'},
    {'make': 'Kia', 'model': 'K5'}
]

with open('cars_json.txt', 'w') as file:
    json.dump(cars, file)

json_string = '[{"name": "Alfa Romeo", "released": 1950}]'

car = json.loads(json_string)
print(car[0]['name'])
