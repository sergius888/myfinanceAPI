# how to cycle through a dictionary

d = {"a": 1, "b": 2, "c": 4, "d": 8}
for key, value in d.items():
    print(key, value)


# print the keys until a value is bigger than 3
# for key, value in d.items():
#     prin("hey")
#     if value <= 3:
#         print(key)
#     else:
#         break # stops the for
#

def maximum(lista):
    max = lista[0]
    for x in lista:
        if type(x) == str or type(x) == bool:
            continue
        if max < x:
            max = x
    return max

print(maximum([1, "a", "b", 3, 0]))


# split applied on a str returns a list
# reverse is join

strings = ["Are", "you", "sure", "?"]
sentence = " ".join(strings)
print(sentence)
