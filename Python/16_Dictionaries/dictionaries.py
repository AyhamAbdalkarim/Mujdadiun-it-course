person = {"name": "Ayham", "age": 20}
person["city"] = "Amman"
print(person.get("name"), person.get("missing", "N/A"))

for k, v in person.items():
    print(k, "->", v)

copy = person.copy()
copy.pop("age")
print(copy)
