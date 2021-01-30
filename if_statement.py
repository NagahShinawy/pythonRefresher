from methods import is_even


def show_smoking_advices_giveup():
    print("1- testing")
    print("2- testing")
    print("3- testing")
    print("4- testing")


is_smoke = True

female_info = {"name": "sara", "is_pregnant": True}
if is_smoke:
    show_smoking_advices_giveup()

if female_info["is_pregnant"]:
    female_info.update(
        {
            "husband": {"name": "john", "age": 31, "job_title": "engineer"},
            "is_married": True,
        }
    )

print(female_info)
print(is_even(3))
print(is_even(2))
print(is_even(0))
