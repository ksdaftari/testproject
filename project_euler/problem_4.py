from library import projecteuler

initialNums = [9, 0]


def constructPalim(array, isMidReflective):
    lenInitialNums = len(array)
    if(isMidReflective):
        inc = 1
    else:
        inc = 0

    Palim = 0
    for i in range(0, (2*lenInitialNums)):
        if(i <= (lenInitialNums-1)):
            Palim = Palim + initialNums[i]*10**(2*lenInitialNums-i-1-inc)
        else:
            if((not isMidReflective) or (isMidReflective and i != lenInitialNums)):
                Palim = Palim + initialNums[2 * lenInitialNums-i-1]*10**(2*lenInitialNums-i-1)
    return(Palim)


def hasMultiplesWithDigits(value, numDigits):
    factors = projecteuler.findPrimeFactors(value)
    factors.sort()
    multiple = 1
    numMultipliers = 0
    multiples = []
    for factor in factors:
        multiple = multiple*factor
        currnumDigits = projecteuler.getNumberDigits(multiple)
        if(currnumDigits == numDigits and numMultipliers < 2):
            multiples.append(multiple)
            numMultipliers = numMultipliers + 1
            multiple = 1
        elif(currnumDigits < numDigits and numMultipliers < 2):
            continue
        else:
            return(False, multiples)
    return(True, multiples)


palim = constructPalim(initialNums, False)
print(hasMultiplesWithDigits(palim, 2))
