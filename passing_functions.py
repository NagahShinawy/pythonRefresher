
def send_mail(another):
    return another()


def mail_body():
    print("sending hello world !")
    return True


send_mail(mail_body)

body = mail_body


body()


def cal(another):
    return another


def add(x, y):
    return x + y


def sub(x, y):
    return x - y


def multi(x, y):
    return x * y


def calc_add(another):
    return another()


print(cal(add(4, 6)))
print(cal(sub(3, 1)))
print(cal(multi(3, 1)))

print(calc_add(lambda: 50 + 10))
print(calc_add(lambda: 50 + 90))


numbers = [5, 7, 8, 10, 90]

odds = filter(lambda num: num % 2 != 0, numbers)
evens = filter(lambda num: num % 2 == 0, numbers)
print("Odds", list(odds))
print("Evens", list(evens))

print((lambda num: num * 4)(2))


# the same of
def f(num):
    return num * 4


print(f(2))


def exclude_john(name: str):
    return name.lower() != 'john'


names = ["Smith", 'John', 'JOHN', 'JohN', 'Sara']

print(list(filter(exclude_john, names)))

print([name for name in names if name.lower() != 'john'])
