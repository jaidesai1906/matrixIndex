#Function to generate a matrix of size n rows*m columns
def make_matrix(n,m):
 X=[]
 for i in range(n):
    print("Elements of row", (i + 1))
    Y = []
    for j in range(m):
        y=int(input())
        Y.append(y)
    X.append(Y)
 print("desired square matrix is: ")
 return X

#Function to define a zero matrix of size n rows*m columns
def zero_matrix(n,m):
 X=[]
 for i in range(n):
    Y = []
    for j in range(m):
        Y.append(0)
    X.append(Y)

 return X

#Function to perform multiplicatio of two matrices
def multiply_matrix(X, Y):

    if len(X[0]) == len(Y):
        A = []
        for i in range(len(X)):
            B = []
            for j in range(len(Y[0])):
                b=0
                for k in range(len(Y)):
                        b += X[i][k] * Y[k][j]
                B.append(b)
            A.append(B)
        return A
    else:
        print("Matrices cannot be multiplied")

#Function to find the index of a nil-potent matrix
def index_nilpotent_matrix(X):

    print("Index of the given nilpotent matrix is: ", end='')

    n = len(X)
    Z = zero_matrix(n, n)
    Y = multiply_matrix(X, X)

    if X == Z:
        print(1)
    else:
        count = 2
        while Y != Z:
            count += 1
            Y = multiply_matrix(Y, X)
        print(count)

#Driver Code

n=int(input("Enter the desired degree of the nilpotent matrix: ")
print("Please enter only a nil-potent matrix (or the output will be a garbage value)")
matrix=make_matrix(n,n)
print(matrix)
print("Degree of the nilpotent matrix is: "index_nilpotent_matrix(matrix))