def sequence_class(immutable):
    if immutable:
        cls = tuple
    else:
        cls = list
    return cls


# Conditional Sequence
def sequence_class2(immutable):
    return tuple if immutable else list


seq = sequence_class(immutable=True)
t = seq("Roger")
print(t)
seq = sequence_class(immutable=False)
seq2 = sequence_class2(immutable=False)
t = seq("Roger")
tt = seq2("Roger")
print("*" * 50)
print(t, tt)
