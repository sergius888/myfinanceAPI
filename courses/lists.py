def print_all_elements(lista):
    for x in lista: # x = lista[0], x = lista[1], ...
        print(x)

l = [1, 2, "a", "b"]
print_all_elements(l)

tu = (1, 2, 3)
print_all_elements(tu)


def condition(x):
    return x > 5
list = [x for x in [1, 6, 7, 8] if condition(x)]
print(list)

list = ["ab", "bc", "vd", "el", "ac"]
for x in list:
    if "a" in x or "b" in x:
        continue
    print(x)

