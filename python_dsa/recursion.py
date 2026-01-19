'''

here i am learing recursion and backtracking
--- recursion is top down approach
--- backtracking means work down after the base condition is met 
--- but in recursion the work is down until the base condition is met
--- recursion is implemented using stack memory
--- if base condition fails than the memory is full and the stack overflow occurs

'''

# printing upto n using backtracking
def recursion(n):
    if n==0:
        return 
    recursion(n-1)
    print(n)

recursion(5)

# printing in reverse using backtracking
def recursion(i,n):
    if n<i:
        return 
    recursion(i+1,n)
    print(i)

recursion(1,5)