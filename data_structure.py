from methods import breaks

disease = ["Hypertension", "Hypertension2", "Hypertension3"]  # list

items = [
        {"name": "hp", "price": 12, "store": "Amazon"},
        {"name": "Huawei", "price": 15, "store": "Amazon"},
        {"name": "macbook", "price": 90, "store": "Souq"},
    ]

credentials = [("username", "nagah"), ("password", "1234@123")]  # list of tuples


grades = [50, 90, 20, 100]

allergies = {"allergy1", "allergy2", "allergy3", "allergy4"}  # set unique & unordered


if __name__ == '__main__':

    for d in disease:
        print(d)

    # list of dicts

    breaks()

    for item in items:
        print(item.get("name"))

    breaks()

    total = sum(grades)
    avg = total / len(grades)
    print(total)
    print(avg)
    print(avg)

    print("Username is ", credentials[0][1])
    print("Password is ", credentials[1][1])

    breaks()

    for g in allergies:
        print(g)

