#Program: multi_dimensional_array
#Assignment: Assignment 3
#Author: Brent Lang
#Date: 09/15/20
#Purpose: Program tests the function main and the functions as commented below.

inStock = []
alpha = []
beta = []
gamma = [11, 13, 15, 17]
delta = [3, 5, 2, 6, 10, 9, 7, 11, 1, 8]

#setZero function initializes any one-dimensional list to 0.
def setZero(num):
    list1 = [0] * num
    return list1

#inputArray function prompts user to input 20 numbers and stores the numbers into list alpha.
def inputArray(alpha):
    print("\n\nEnter 20 integers:")
    for i in range(20):
        alpha[i] = int(input())

#doubleArray function initializes the elements of beta to two times the corresponding elements in alpha.
def doubleArray(beta,alpha):
    for i in range(20):
        beta[i] = (alpha[i] * 2)

#copyGamma function sets the elements of the first row of inStock from gamma
#The remaining rows of inStock are set to three times the previous row of inStock.
def copyGamma(gamma,inStock):
    for i in range(10):
        inStock.append([])
        for j in range(4):
            if i == 0:
                inStock[i].append(gamma[j])
            else:
                inStock[i].append(inStock[i - 1][j] * 3)
    
#copyAlphaBeta function stores alpha into the first five rows of inStock.
#beta is stored into the last five rows of inStock.
def copyAlphaBeta(alpha,beta,inStock):
    k = 0
    l = 0
    for i in range(10):
        for j in range(4):
            if i < 5:
                inStock[i][j] = alpha[k]
                k += 1
            else:
                inStock[i][j] = beta[l]
                l += 1

#printArray function prints any one-dimensional list using a single loop.
def printArray(array):
    for i in range(0, len(array), 10):
        print(*array[i:i + 10], sep = '\t')
    
#setInStock function prompts user to input the elements for the first column of inStock.  
#The function then sets the elements in the remaining columns to two times the corresponding element in the previous column
#minus the corresponding element in delta.
def setInStock(inStock,delta):
    print("\n\nEnter 10 Integers: ")
    for i in range(10):
        inStock[i][0] = int(input())
    for i in range(1,4):
        for j in range(10):
            inStock[j][i] = (2 * inStock[j][i - 1]) - (delta[j])

def printColumns(inStock):
    for i in range(10):
        print(*inStock[i], sep = '\t')

def main():
    alpha = setZero(20)
    
    print("Alpha after initialization")
    printArray(alpha)
    
    beta = setZero(20)
    
    inputArray(alpha)
    
    print("\n\nAlpha after reading 20 numbers:") 
    printArray(alpha)
    
    doubleArray(beta,alpha)
    
    print("\n\nBeta after a call to doubleArray:")
    printArray(beta)

    copyGamma(gamma,inStock)
    
    print("\n\ninStock after call to copyGamma:") 
    printColumns(inStock)

    copyAlphaBeta(alpha,beta,inStock)
    
    print("\n\ninStock after call to copyAlphaBeta:")
    printColumns(inStock)

    setInStock(inStock,delta)
    
    print("\n\ninStock after call to setInStock:")
    printColumns(inStock)

main()