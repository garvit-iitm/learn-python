from array import array

arr = array('i',[])

print(type(arr))

n = int(input("enter the size of array : "))


for i in range(n):
    arr.append(int(input(f"Enter integer value {i+1}: ")))

print("Your array value's are as follows : ", end="")

for a in arr:
    print(a,end=" ")

print(type(arr))

# here we provide the pop(index) , by default value of index is -1
print("pop value is : ", arr.pop())

#if we want to delete the element by value then we use remove(value)
arr.remove(2)

# here i learned about insert(),append(),array module,pop().remove