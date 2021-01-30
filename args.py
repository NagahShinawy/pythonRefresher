
def list_names(*args):
    assert all([type(name) == str for name in args]), "All names should be string"
    if args:
        for name in args:
            if name:
                print(name)
    else:
        print("No names found")


list_names("Smith", "John")