def welcome(name: str):
    assert type(name) == str, "Name is not string"
    if name:
        print(f"Welcome {name}")
    else:
        print("Please Login")


def get_fullname(fname: str, lname: str):
    assert type(fname) == str, "First Name should be string"
    assert type(lname) == str, "Last Name should be string"
    if fname and lname:
        return fname + " " + lname
    return "Missing first name or last name"


def calc_bim(height: float, weight: float):
    return (height * weight) / 2


def check_smoking(is_smoker=bool):
    if is_smoker:
        return "Check Advices for smoking give up"


def breaks(char="#", number=20):
    print(char * number)


if __name__ == "__main__":
    print(calc_bim(12, 12.3))
    is_smoke = True
    print(check_smoking(is_smoke is False))
    print(get_fullname(1, 2))
    welcome(None)
    welcome("")
    welcome(1)
    welcome("John")
