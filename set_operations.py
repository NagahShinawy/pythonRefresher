national_team = {"Trika", "Barakat", "Hadary", "Amr"}
ahly = {"Trika", "Barakat", "Hadary"}
zamalek = {"Amr"}

common_ahly = national_team.intersection(ahly)
common_zamalek = national_team.intersection(zamalek)  # intersection

print(common_ahly)
print(common_zamalek)

print(ahly.union(zamalek))  # all
print(ahly.union(zamalek) == national_team)  # True

print(national_team.difference(zamalek))  # ahly
x = (3,)  # single value tuple
print(x)
