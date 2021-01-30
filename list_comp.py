national_ids = [1223, 3543, 5647, 6593, 1235, 9087]

dob = [str(_id)[:2] for _id in national_ids]

print(dob)


blood_types = ("A+", "A-", "B+", "B-", "O+", "O-", "AB+", "AB-")

print(blood_types)

evens = [4, 6, 8, 12]
print([num * 10 for num in evens])

names = ["nagah shaban", "john", "mohammed", "ali"]

to_upper = [name.upper() for name in names]
to_capitalize = [name.capitalize() for name in names]
to_title = [name.title() for name in names]
print(to_upper)
print(to_capitalize)
print(to_title)
