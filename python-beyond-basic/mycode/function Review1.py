import socket


def function_name(arg1, arg2, arg3=1.0):
    """ Show positional arguments"""
    print("Body")
    return arg1 + arg2 * arg3


def resolve(host):
    return socket.gethostbyname(host)


print(function_name(1, 2))
print(resolve("www.novoprint.es"))

c = resolve
print(c("www.novoprint.es"))
# Resolve return a reference to the function
print(c)


