import random
from datetime import date, timedelta


class Human:
    def __init__(self, name: str, surname: str, date: str):
        self.surname = surname
        self.name = name
        self.date = date

    def __str__(self):
        return f"Man: {self.surname} {self.name[0]}.\nBirth date: {self.date}"


class Student(Human):
    def __init__(self, name, surname, date):
        super().__init__(name, surname, date)

    def passport_n(self, passport=None):
        """
        Generate random 6-num pass_number
        """
        x = []
        for i in range(5):
            x.append(random.randint(0, 9))
            passport = "".join(map(str, x))
        return passport

    def age_count(self):
        """
        Calculate days from date.self to today, generate age in years
        """
        today = date.today()
        birth_date = self.date.split("-")
        bd = date(int(birth_date[2]), int(birth_date[1]), int(birth_date[0]))
        age = today - bd
        year = timedelta(days=365)
        return int(age/year)

    def __str__(self):
        """
        Return all Human-class information adding results of Student-functions
        """
        return f"{self.surname} {self.name[0]}./ {self.date} / {self.age_count()} / {self.passport_n()}"


class MaxStudentsError(Exception):

    def __init__(self, msg):
        super().__init__()
        self.msg = msg

    def __str__(self):
        return f'{self.msg}\n{super().__str__()}'


class Group:
    def __init__(self, course: str):
        """Group title"""
        self.title = course
        self.students = []

    def add_student(self, student: Student):
        """Adding students to group"""

        if len(self.students) >= 8:
            raise MaxStudentsError("Too many student in group!")

        if student not in self.students:
            self.students.append(student)


    def remove_student(self, student: Student):
        """Removing students from group-list"""
        self.students.remove(student)

    def search(self, surname):
        for i in self.students:
            if surname == i.surname:
                return f"\n{i}"
        return -1

    def __str__(self):
        """Return students group"""
        res = f"{self.title}\n"
        """Group headline"""
        res += f"Name: / Birth date: / Age: / P/n\n"
        res += '\n'.join(map(str, self.students))
        return res


man1 = Student("Matt", "Leblanc", "12-09-1993")
man2 = Student("Ivan", "Ivanov", "12-11-1991")
man3 = Student("Petr", "Petrov", "17-04-1992")
man4 = Student("Sidor", "Sidorov", "02-01-1993")
man5 = Student("Ostin", "James", "12-01-1991")
man6 = Student("Mykola", "Tkach", "22-11-1992")
man7 = Student("Oleh", "Olehov", "30-03-1991")
man8 = Student("Joe", "Tribiani", "07-05-1992")
man9 = Student("Jack", "Jackov", "01-04-1992")
man10 = Student("Piter", "Piterson", "01-01-1993")

try:
    gr_python = Group("Python Pro Group")
    gr_python.add_student(man1)
    gr_python.add_student(man2)
    gr_python.add_student(man3)
    gr_python.add_student(man4)
    gr_python.add_student(man5)
    gr_python.add_student(man6)
    gr_python.add_student(man7)
    gr_python.add_student(man8)
    gr_python.add_student(man9)
    gr_python.add_student(man10)

except (ValueError, MaxStudentsError) as err:
    print("Recruitment completed", err)

print(gr_python)
print(gr_python.search("Leblanc"))
