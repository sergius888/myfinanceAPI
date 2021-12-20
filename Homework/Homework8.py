list1 = ["Michael", "", "Ellie", "Ken", "", "Gunter"]
# write a function which returns a list without the empty strings (do not use remove function for this exercise)
def without(lista):
    new_list = []
    for el in list1:
        if el != "":
            new_list.append(el)
    return new_list

print(without(list1))

list2 = [1, -2, 3, -4, 10, 8, 99, -23, 55, 100, -0.6, 27.6]
# write a function which returns a dict containing the 2nd largest number & 2nd smallest number
# write a function which makes the sum of all positive numbers and multiplies all the negative ones
def min_and_max(lista):
    min1 = lista[0] # the smallest one
    min2 = lista[0] # the 2nd smallest one
    max1 = lista[0] # the biggest one
    max2 = lista[0] # the 2nd biggest one
    for el in lista:
        if min1 > el:
            min1 = el
        if max1 < el:
            max1 = el
    # until now, the function determines the maximum and minimum
    for el in lista:
        if el > min1 and el < min2:
            min2 = el
        if el < max1 and el > max2:
            max2 = el
    return (min2, max2)

print(min_and_max(list2))
list3 = ["a", "a", "c", "d", "b", "c", "a"]
# write a function which counts every element and returns a dict {"a": 3, "b": ...
def count_el(lista):
    d = {}
    for el in lista:
        if el in d: #check a key is in dictionary
            d[el] = d[el] + 1
        else:
            d[el] = 1
    return d

print(count_el(list3))