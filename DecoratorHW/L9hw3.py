"""Create decorator for __str__ method of class Human
to save result string in text-file, with name such class-name"""


def save_file_dec(f):
    def my_function(arg):
        res = f(arg)
        with open('newfile.txt', 'w') as g:
            print(res, file=g)
        return res
    return my_function


class Human:

    def __init__(self, name, surname, b_date):
        self.name = name
        self.surname = surname
        self.b_date = b_date
        self.class_name = self.__class__.__name__

    @save_file_dec
    def __str__(self):
        return f"{self.surname} {self.name[0]}. celebrates his birthday on {self.b_date}"


human_1 = Human("Petro", "Melnik", "17.04.1995")


print(human_1)


