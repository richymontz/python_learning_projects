import json

clubs_csv_file = open('clubs_csv.txt', 'r')
clubs_list = []

for line in clubs_csv_file.readlines():
    club, city, country = line.strip().split(',')
    clubs_list.append(dict({'club': club, 'city': city, 'country': country}))

clubs_csv_file.close()

json_file = open('json_file.txt', 'w')
json.dump(clubs_list, json_file)
json_file.close()

