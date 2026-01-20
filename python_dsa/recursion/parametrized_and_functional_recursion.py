'''
Docstring for python_dsa.recursion.parametrized_and_functional_recursion

'''

# sum of first n natural numbers using parametrized recursion


def sumition(i,s):
    if i < 1:
        return s
    return sumition(i-1,s+i)

print(sumition(3,0))


# sum of first n natural numbers using functional recursion

def sumition_functional(i):
    if i < 1:
        return 0
    # The math happens AFTER the function returns
    return i + sumition_functional(i-1)

print(sumition_functional(3))

# factorial of a number using parametrized recursion

def fact_para(fact,i):
    if i == 0:
        return fact
    return fact_para(fact*i,i-1)

print(fact_para(1,5))


# factorial of a number using factorial recursion

def fact_fun(n):
    if n == 1:
        return 1
    return n*fact_fun(n-1)

print(fact_fun(5))


# reverse an array using parametrized recursion
def arr_rev_para(arr,low,high):
    if low>=high:
        return arr
    arr[low],arr[high ]= arr[high],arr[low]

    return arr_rev_para(arr,low+1,high-1)

print(arr_rev_para([1,2,3,4,5],0,4))

# reverse an array using functional recursion
# TRUE Functional Recursion
# Notice: No parameters carrying the 'answer' forward. 
# The answer is built on the way back up.
def arr_rev_true_func(arr):
    # Base Case: Empty or single item
    if len(arr) <= 1:
        return arr
        
    # Recursive Step: 
    # 1. Call function on the REST of the array (arr[1:])
    # 2. Add the FIRST item (arr[0]) to the END of that result
    return arr_rev_true_func(arr[1:]) + [arr[0]]

print(arr_rev_true_func([1, 2, 3, 4, 5]))
# Output: [5, 4, 3, 2, 1]


# check for palindrome using recursion

def palin_rec(s,n,i):
    if i >= n//2:
        return True
    if s[i] != s[n-i-1]:
        return False
    return palin_rec(s,n,i+1)

s = "mada"
print(palin_rec(s,len(s),0))
