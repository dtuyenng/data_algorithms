
user_0 = {
    "username": "Coolio",
    "first": "Tuyen",
    "last": "Nguyen",
    "nickname": "Bad Ass",
}

print(user_0)
# Accessing value through the key
print(user_0["first"])

# Modifying value associated with a key
user_0["username"] = "NewUserName"

# Deleting a key:value pair using the key
del user_0["nickname"]

print(type(user_0.items()))

for key, value in user_0.items():
    print(f"item: {key} : value: {value}")

for key in user_0.keys():
    print(f"key: {key}")

for value in user_0.values():
    print(f"value: {value}")

# Accessing a value through the .get() method to avoid throwing error
# print(user_0["faofaf"]) # this will throw an error

print(user_0.get("faofaf", "null"))

fav_language = {
    "Alice": "Python",
    "Bob": "JavaScript",
    "Charlie": "Java",
    "Diana": "C++",
    "Eve": "Java",
    "Joe": "Java"
}

friends = ["Bob", "Charlie"]

for key in fav_language.keys():
    if key in friends:
        language = fav_language[key]
        print(f"friend: {key} language: {language}")

for name, language in fav_language.items():
    if name in friends:
        print(f"friend: {name} language: {language}")

for language_mentioned in set(fav_language.values()):
    print(language_mentioned)






# Nest Dicts

sample_dict = {
    "person_1": {
        "name": "Alice",
        "age": 30,
        "languages": ["Python", "JavaScript"],
    },
    "person_2": {
        "name": "Bob",
        "age": 25,
        "languages": ["Java", "C++"],
    },
    "person_3": {
        "name": "Charlie",
        "age": 28,
        "languages": ["Ruby", "Go"],
    },
}
for key, value in sample_dict.items():
    print(key)
    print(f"Name: {value["name"]} - Age: {value["age"]} Languages: {value["languages"][0]}")