fib = [1, 2]
i = 2
nextElement = 0
while(nextElement <= (4*10**6)):
    nextElement = fib[i-2] + fib[i-1]
    fib.append(nextElement)
    i = i + 1
evenFib = [x for x in fib if x % 2 == 0]
print(sum(evenFib))
