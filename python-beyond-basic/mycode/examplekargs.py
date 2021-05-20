def test(name, **kwargs):
    print(name)
    print(kwargs)
    print(type(kwargs))


def tag(name, **kwargs):
    result = "<" + name
    for key, value in kwargs.items():
        result += ' {k}="{v}"'.format(k=key, v=str(value))
    result += ">"
    return result

def combining(name,*args,kwargs1,**kwargs):
    print(name)
    print(args)
    print(kwargs1)
    print(kwargs)

test("Roger", memory="1", low="3", random="2")
print(tag("img", border="0", widh="210px", height="100px"))
print(combining("sss", kwargs1=2))