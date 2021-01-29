from data_structure import disease, allergies, credentials, breaks

disease.append("heart")

print(disease)

credentials.append(("key", "5435m4nr543mn534mnrsdfnmsdfnmsdfmnas,deqwnreq"))

breaks()

print(credentials)

row = ("row", 89)
col = ("row", 6)
height = ("height", 90)

three_d = row + col + height

print(three_d)


allergies.add("allergy10")

print(allergies)

for index, g in enumerate(allergies):
    if g == "allergy2":
        print(f"Element is {g} with index {index}")
