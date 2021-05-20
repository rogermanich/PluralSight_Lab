# Callable

def is_odd(value):
    return value % 2 == 0


class Callme:
    def __call__(self):
        print("CALL")


a = Callme()
print(callable(is_odd))
print(callable(lambda value: value % 2 == 0))
print(callable(list))
print(callable(list.append))
print(callable(a))
a()
