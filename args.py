import methods


def list_names(*args):
    assert all([type(name) == str for name in args]), "All names should be string"
    if args:
        for name in args:
            if name:
                print(name)
    else:
        print("No names found")


def style_dataframe(**kwargs):
    for css_pro, css_value in kwargs.items():
        print(css_pro, css_value)


list_names("Smith", "John")
methods.breaks()
style_dataframe(color="red", bgcolor="black", font_size=12)
style_dataframe()
