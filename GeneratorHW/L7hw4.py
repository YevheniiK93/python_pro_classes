"""Implement a generator to fill the list. The list must
be filled with numbers to the third powered (from 2 to the value you specify)."""

limit = int(input("Input range limit: "))

gen = ((i**3 for i in range(2, limit)))

for i in gen:
    print(i)
