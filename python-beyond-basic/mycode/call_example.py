import socket


class Resolver:
    def __init__(self):
        self._cache = {}

    def __call__(self, host):
        if host not in self._cache:
            self._cache[host] = socket.gethostbyname(host)
        return self._cache[host]

    def has_host(self, host) -> object:
        return host in self._cache

    def clear(self):
        self._cache.clear()


# Call allows to call method as function
a = Resolver()
print(a("www.novoprint.es"))
print(a.has_host("www.novoprint.es"))
a.clear()
