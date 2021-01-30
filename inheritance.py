from methods import breaks


class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school

    @classmethod
    def friend(cls, origin, friend_name):
        return cls(friend_name, origin.school)

    def __repr__(self):
        return self.name


class WorkingStudent(Student):

    # re implement __init__ with custom info for working student
    def __init__(self, name, school, salary):
        super().__init__(name, school)
        self.salary = salary

    @classmethod
    def friend(cls, origin, friend_name, salary):
        return cls(friend_name, origin.school, salary)

    def __repr__(self):
        return f"{self.name}- {self.salary}"


if __name__ == "__main__":
    john = Student("John", "MIT")
    sara = Student.friend(john, "Sara")
    print(john)
    print(sara)
    breaks()
    nagah = WorkingStudent("Nagah", "Fahd", 20)
    ahmed = WorkingStudent.friend(nagah, "Ahmed", 12)
    print(ahmed)
