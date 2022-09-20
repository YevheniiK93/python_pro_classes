import re

"""1. Write a regular expression that will
find fragments in the text, consisting of one
the letter R followed by one or more b's,
followed by one r. Consider upper and lower case."""

print("Task #1:")

text = "AcBsRrbBbR565RbBbbr"

pattern = r"[Rr][Bb]+[Rr]"

match = re.findall(pattern, text)

if match:
    print(match)
else:
    print("pattern not found")

"""2. Write a function that performs validation
bank card numbers (9999-9999-9999-9999)."""


def card_valid(card_num):
    pattern = r"^\d{4}-\d{4}-\d{4}-\d{4}$"
    match = re.match(pattern, card_num)
    if match:
        return True
    else:
        return False


print("\nTask #2:")

print(card_valid("999-9999-9999-9999"))
print(card_valid("9999-9999-9999-9999"))
print(card_valid("999-9999-9999 9999"))


"""3. Write a function that takes string data and checks if it matches the email.
Requirements:
-numbers (0-9).
-only Latin letters in large (A-Z) and small (a-z) registers.
- Only the characters “_” and “-” are allowed in the body of the email. But they cannot be the first character of an email.
- the “-” character cannot be repeated."""


def mail_validation(mail):

    pattern = r'^[a-zA-Z0-9](-?[a-zA-Z0-9_])+@[a-zA-Z0-9]+(\.[a-zA-Z0-9]+)*$'
    match = re.match(pattern, mail)
    if match:
        return True
    else:
        return False

print("\nTask #3:")

print(mail_validation("_so_me-mail@domain.com"))
print(mail_validation("so_memail@domain.com"))
print(mail_validation("some--mail@domain.com"))

"""4. Write a function that checks the correctness of the login. Right
login - a string from 2 to 10 characters, containing only letters and numbers."""


def login_check(login):
    pattern = r"[a-zA-Z0-9]{2,11}$"
    match = re.match(pattern, login)
    if match:
        return True
    else:
        return False


print("\nTask #4:")

print(login_check("A"))
print(login_check("AbCdeF12"))
print(login_check("Bob122345678"))
