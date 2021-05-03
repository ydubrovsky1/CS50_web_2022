people = [
    {"name": "Harry", "house":"Gryffindor"}, 
    {"name": "Cho", "house":"Ravenclaw"}
]


def f(person):
    return person["name"]

people.sort(key = f)
print(people)

#lamda allows include above function as single line
people.sort(key = lambda person: person["name"])
print(people)