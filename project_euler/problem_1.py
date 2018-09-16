num = 1000
array = list()
for x in range(1, num):
    if(x % 3 == 0 or x % 5 == 0):
        array.append(x)

print(sum(array))
