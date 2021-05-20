# Lambda Example with sort

names1 = ["Jame Kirk", "Wolfgang Klaus", "Jeremy Iron", "Evelyn Karl", "Jeannine Jefferson"]
c = sorted(names1, key=lambda name: name.split()[-1])
print(c)

# last_Name = lambda name: name.split()[-1]

# print(last_Name(c[0]))
