from methods import breaks


class Player:
    def __init__(self, name, nationality, age):
        self.name = name
        self.nationality = nationality
        self.age = age
        self.goals = 0
        self.matches = 0

    def show_player_info(self):
        pass

    def set_matches(self, matches):
        self.matches = matches

    def set_goals(self, goals):
        self.goals = goals

    def pre_goals(self):
        return self.goals / self.matches

    def __repr__(self):
        return (
            f"{self.name}\t{self.nationality}\t{self.age}\t{self.goals}\t{self.matches}"
        )


class Student:

    counts = 0

    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []
        Student.counts += 1

    def avg(self):
        return sum(self.marks) / len(self.marks)

    def __repr__(self):
        return self.name

    def set_mark(self, mark):
        assert type(mark) in [float, int], "Mark should be int, float not {}".format(
            type(mark)
        )
        assert mark in range(0, 100), "Mark should be ib range 1 to 100"
        self.marks.append(mark)

    @staticmethod
    def get_total_count():
        # this is bug if it called by subclass not (Student Class). so you need to use @classmethod
        return Student.counts

    @classmethod
    def get_info(cls):
        """dynamic implementation of method based on cls
        whatever class you call, it execute based ob class
        """
        print(f"You are using ({cls.__name__}) with count {cls.counts}")


class Nagah(Student):
    counts = 0


if __name__ == "__main__":
    salah = Player("Salah", "Egypt", 28)
    print(salah)
    breaks()
    print(Student("John", 17))
    john = Student("Smith", 17)
    lean = Student("lean", 30)
    john.set_mark(2)
    john.set_mark(2.00)
    john.set_mark(0)
    print(john.marks)
    Student.get_info()
    Nagah.get_info()
