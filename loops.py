from methods import breaks, exclude_char_n, double_numbers


fullname = "John Smith"

for char in fullname:
    print(char, end="")


breaks(newline=True)


print(exclude_char_n("Nagah Shaban Shinawy"))

breaks()

print(double_numbers([6, 7, 5, 9]))
breaks()

counter = 0

while True:
    if counter == 11:
        break
    print("Level #{}".format(counter))
    counter += 1


def guess_number():
    pc = 9
    tries = 1
    number = int(input("Type a number in range 1 to 10"))
    while pc != number:
        number = int(input("Type a number in range 1 to 10"))
        tries += 1
    print("You Finally got it after", tries)


guess_number()
