def firstPrimeFactor(num):
    factor = 2
    while(num % factor != 0):
        factor = factor + 1
    return(factor)


def findPrimeFactors(num):
    initialPrimeMultiple = firstPrimeFactor(num)
    currMultiple = int(num/initialPrimeMultiple)
    factors = [initialPrimeMultiple]
    while(currMultiple != 1):
        nextPrmieMultiple = firstPrimeFactor(currMultiple)
        factors.append(nextPrmieMultiple)
        currMultiple = int(currMultiple/nextPrmieMultiple)
    return(factors)


findPrimeFactors(99321298278897)
