def our_max(theList):
    curr_max = 100
    for n in theList:
        if n < curr_max:
            curr_max = n
    print(curr_max)

our_max([3, 4, 5, 6, 1])
x = min([3, 4, 5, 6, 1])
print(x)
print(max([3, 4, 5, 6, 1]))
