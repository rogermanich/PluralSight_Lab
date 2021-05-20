# test

def summ(*args):
    i = iter(args)
    value = 0
    for v in i:
        value += v
    return value


def hypervolumen(*args):
    i = iter(args)
    value = next(i)
    for v in i:
        value *= v
    return value


def hypervolumen2(arg, *args):
    value = arg
    for v in args:
        value *= v
    return value


print(summ(1, 2, 3, 4, 5, 6))
print(hypervolumen(2, 4))
print(hypervolumen2(2, 4))
