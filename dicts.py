health_profile = {
    "username": "John",
    "height": 120,
    "weight": 50,
    "gender": "female",
    "blood_type": "A+",
    "dof": "2012-01-10",
}

for param, value in health_profile.items():
    print(param, value)


if health_profile.get("gender") == "female":
    health_profile.update(
        {
            "is_married": True,
            "is_pregnant": True,
            "husband": {"name": "Smith", "age": 36, "job_title": "engineer"},
        }
    )


print(health_profile)
print(health_profile["husband"]['age'])

team = {
    "name": "liverpool",
    "points": 23,
    "weeks": 10,
    "players": [
        {"name": "Salah", "nationality": "Egypt", "goals": 5},
        {"name": "Mani", "nationality": "Sengal", "goals": 3},
        {"name": "Fer", "nationality": "Barazil", "goals": 4},
    ]
}

salah = team["players"][0]["name"]

print(salah)