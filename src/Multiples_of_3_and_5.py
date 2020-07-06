import timeit

# https://en.wikipedia.org/wiki/Inclusion%E2%80%93exclusion_principle
# https://codereview.stackexchange.com/questions/149143/project-euler-problems-1-and-2-in-python

def f():
    upper_end = 1000
    result = 0
    for x in range(0, upper_end):
        if x % 3 == 0 or x % 5 == 0:
            result += x
    return result


def g():
    upper_end = 1000
    return sum(i for i in range(0, upper_end) if i % 3 == 0 or i % 5 == 0)


def h():
    upper_end = 1000
    return sum(range(3, upper_end, 3)) + sum(range(5, upper_end, 5)) - sum(range(15, upper_end, 15))


# # https://docs.python.org/2/library/timeit.html#timeit.Timer.timeit
print(min(timeit.Timer(f).repeat(1000,1)))  # print minimum of one hundred single measurements
print(min(timeit.Timer(g).repeat(1000,1)))  # print minimum of one hundred single measurements
print(min(timeit.Timer(h).repeat(1000,1)))


print(f())
print(g())
print(h())

#
# print(list_comprehension_result )
