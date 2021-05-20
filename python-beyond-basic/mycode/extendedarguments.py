# System unpack
def test1(arg1, arg2, *args):
    print(arg1)
    print(arg2)
    print(args)


def test2(red, green, blue, **kwargs):
    print("r=", red)
    print("g=", green)
    print("b=", blue)
    print(kwargs)


t = (1, 2, 3, 4, 5, 6)
# use *t to instruct function to unpack
test1(*t)
s = {'red': 1, 'green': 11, 'yellow': 222, 'blue': 12}
test2(**s)
# alternative way
s = dict(red=21, yellow=12, green=222, blue=2222, normand=1)
test2(**s)
