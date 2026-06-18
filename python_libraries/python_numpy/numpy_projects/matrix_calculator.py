import numpy as np

def input_matrix():
    print("enter the size of rows :")
    n = int(input())
    print("enter the size of columns :")
    m = int(input())

    matrix = []

    print("enter the element row-wise")
    
    for i in range(n):
        matrix.append(list(map(int,input().split())))
    
    return np.array(matrix)

def add_matrix(a,b):
    if a.shape != b.shape:
        print("Matrices must have same dimensions for addition")
    else:
        print(a+b)

def sub_matrix(a,b):
    print(a-b)

def mult_matrix(a,b):
    if a.shape[1] != b.shape[0]:
        print("Multiplication not possible.")
    else:
        print(a@b)

def trans_matrix(a,b):
    print("Transpose of matrix 1 :\n",a.T)
    print("Transpose of matrix 2 :\n",b.T)

def det_matrix(a,b):
    if a.shape[0] == a.shape[1]:
        print("determinant of matrix 1:",np.linalg.det(a))
    else:
        print("matrix 1 is not square")

    if b.shape[0] == b.shape[1]:
        print("determinant of matrix 2:",np.linalg.det(b))
    else:
        print("matrix 2 is not square")

def inv_matrix(a,b):
    if np.linalg.det(a) != 0:
        print("inverse of matrix 1:\n",np.linalg.inv(a))
    else:
        print("matrix 1 is not invertible")

    if np.linalg.det(b) != 0:
        print("inverse of matrix 2:\n",np.linalg.inv(b))
    else:
        print("matrix 2 is not invertible")


a = input_matrix()
b = input_matrix()


print("\nenter your choice for your matrix")

print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Transpose")
print("5. Determinant")
print("6. Inverse")

ch = int(input())

if ch == 1:
    add_matrix(a,b)

elif ch == 2:
    sub_matrix(a,b)

elif ch == 3:
    mult_matrix(a,b)

elif ch == 4:
    trans_matrix(a,b)

elif ch == 5:
    det_matrix(a,b)

elif ch == 6:
    inv_matrix(a,b)

else:
    print("you have given the wrong choice")


