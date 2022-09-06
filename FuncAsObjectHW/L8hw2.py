import timeit


s1 = """
def fibonachi_sequence(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibonachi_sequence(n-1)+fibonachi_sequence(n-2)
  
fibonachi_sequence(20)      
"""


s2 = """
def get_fibonachi(storage={}):    

    def calculation (n):
        if n in storage:
            return storage[n]
        elif n == 0:
            storage[n] = 0
        elif n == 1:
            storage[n] = 1
        else:
            storage[n] = calculation(n-1)+calculation(n-2)
        return storage[n]
    return calculation

c = get_fibonachi()
c(20)
"""

sp1 = f'{timeit.timeit(stmt=s1, number=10):.10f}'
sp2 = f'{timeit.timeit(stmt=s2, number=10):.10f}'

print(f"{sp1}\n{sp2}\nSpeed boosted in {float(sp1) / float(sp2)} times")


