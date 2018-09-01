
transitionMatrix = matrix( c(0.01, 0.91, 0.07,0.01,
                            0.5, 0.2, 0.05,0.25,
                            0.15, 0.05, 0.45,0.35,
                            0.1, 0.2, 0.4,0.3), # the data elements
            nrow=4,              # number of rows
            ncol=4,              # number of columns
            byrow = TRUE)

power <- function(matrix,num)
{
    i = 1
    newmatrix = matrix
    while(i < num)
    {
        newmatrix = newmatrix%*%matrix
        i = i +1
    }
    return(newmatrix)
}

transitionState <- function(transitionMatrix)
{
    tolerance = 0.00000000001
    dimMatrix = dim(transitionMatrix)[1]*dim(transitionMatrix)[2]
    initialMatrix = transitionMatrix
    currMatrix = initialMatrix
    prevMatrix = currMatrix
    diffMatrix = abs(currMatrix-prevMatrix)
    i = 1
    while ((length(diffMatrix[diffMatrix<=tolerance])!=dimMatrix) || i==1) {
        prevMatrix = currMatrix
        currMatrix = currMatrix%*%initialMatrix
        diffMatrix = abs(currMatrix-prevMatrix)
        i = i+1
    }
    return(i)
}
convergentStep = transitionState(transitionMatrix)
convergentStep
power(transitionMatrix,convergentStep)
