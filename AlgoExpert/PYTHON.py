def adder(*args):
    newList = []
    for i in args:
        newList.append(i)
    return newList
lst1 = [1, 2]
lst2 = [3, 4]
lst3 = [5, 6]
lst4 = [lst2, lst3]
lst1 = adder(*lst4)
print(lst1)
