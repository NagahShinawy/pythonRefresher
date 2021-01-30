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
    def __init__(self, name, school, salary, job_title):
        super().__init__(name, school)
        self.salary = salary
        self.jon_title = job_title

    @classmethod
    def friend(cls, origin, friend_name, *args,  **kwargs):
        return cls(friend_name, origin.school, *args,  **kwargs)

    def __repr__(self):
        return f"{self.name}- {self.salary} - {self.jon_title}"


if __name__ == "__main__":
    john = Student("John", "MIT")
    sara = Student.friend(john, "Sara")
    print(john)
    print(sara)
    breaks()
    nagah = WorkingStudent("Nagah", "Fahd", 20, "software developer")
    ahmed = WorkingStudent.friend(nagah, "Ahmed", 40, job_title="system admin")
    print(ahmed)
    girl = Student.friend(nagah, 'Roba')
    print(girl.name)
    print(girl.school)
    breaks()

