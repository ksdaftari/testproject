import math


def firstPrimeFactor(num):
    factor = 2
    while(num % factor != 0):
        factor = factor + 1
    return(factor)


def getPrimes(maxValue):
    primes = [2]
    for value in range(3, maxValue):
        isPrime = True
        for prime in primes:
            if(value % prime == 0):
                isPrime = False
        if(isPrime):
            primes.append(value)
    return(primes)


sum(getPrimes(10))


def findPrimeFactors(num):
    initialPrimeMultiple = firstPrimeFactor(num)
    currMultiple = int(num/initialPrimeMultiple)
    factors = [initialPrimeMultiple]
    while(currMultiple != 1):
        nextPrmieMultiple = firstPrimeFactor(currMultiple)
        factors.append(nextPrmieMultiple)
        currMultiple = int(currMultiple/nextPrmieMultiple)
    return(factors)


def getNumberDigits(value):
    if(value % 10 != 0):
        return(math.ceil(math.log10(value)))
    else:
        return(math.ceil(math.log10(value))+1)
