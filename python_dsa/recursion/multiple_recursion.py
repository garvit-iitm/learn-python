# this is 2^n time complexity
def fibo(n):
    if n<=1:
        return n
    return fibo(n-1)+fibo(n-2)

print(fibo(4))

''' 
-- a subsequence is the contigous or non contigous part of an array that follows a order
-- printing all the subsequences of an array
'''
seq
def subse(index,seq):
    n = len(seq)
    if index>=n:
        print(seq)
    seq.append(arr[i])
