import csv

movies = [
    {"name": 'The Matrix', "director": "Bar Foo"},
    {"name": 'Super Mario', "director": "Jon Doe"},
    {"name": 'Cha Cha Cha', "director": "Foo Bar"}
]


def write_to_file(output):
    with open('movies.csv', 'w') as f:
        writer = csv.DictWriter(f, fieldnames=["name", "director"])
        writer.writeheader()
        writer.writerows([elem.values() for elem in output])


def read_from_file():
    with open('movies.csv', 'r') as f:
        reader = csv.DictReader(f)
        for line in reader:
            print(f"Name: {line['name']} \tDirector: {line['director']}")
