from pprint import pprint as pp

monday = [20, 21, 17, 19, 25, 16]
sunday = [15, 16, 29, 20, 21, 22]
tuesday = [16, 17, 16, 20, 22, 24]

for item in zip(monday, sunday):
    print(item)
print("-" * 50)
for item in zip(monday, sunday, tuesday):
    print(item)
print("-" * 50)
daily = [monday, sunday, tuesday]
for item in zip(daily[0], daily[1], daily[2]):
    print(item)
print("-" * 50)
for item in zip(*daily):
    print(item)

transposed = list(zip(*daily))
print("-" * 50)
pp(daily)
print("-" * 50)
pp(transposed)
