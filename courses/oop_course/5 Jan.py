#Forms - Holiday


list1 = ["a", "b", "c"]
list2 = ["c", "a", "b"]

print(list1[0], list2[0])
print(list1 == list2)

list1.append(["d", "e"]) # we add the list tot the end of list1 on index 3
print(list1)

d = {"a": 0, "b": 0, "c": 0}
print(len(d))

# ['a', 'b', 'c', ['d', 'e']] ->  Len = 4 ; forth is ['d', 'e']

d2 = {"a": 2, "b": 4, "c": 6, "d": 7}
print(d2.items())

##     "a" is what we add -> or x; for x in .....
new_list = ["a" for x in ["1", "2", "3", "4", "a", "b"] if not x.isnumeric()]
print(new_list)

