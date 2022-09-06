
def my_filter(sequence, predicate):
    result = []
    for element in sequence:
        if(predicate(element) == True):
            result.append(element)
    return result


sequence = [0, 7, 4, 11, -4, 17, 24, 3]


print(sum(my_filter(sequence, lambda item: item > 0)))


