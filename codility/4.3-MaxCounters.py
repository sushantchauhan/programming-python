

def MaxCounters(N, A):
    """
    given N counters, initially set to 0, and you have two possible operations on them:

    increase(X) − counter X is increased by 1,
    max counter − all counters are set to the maximum value of any counter.
    A non-empty array A of M integers is given. This array represents consecutive operations:
    
    if A[K] = X, such that 1 ≤ X ≤ N, then operation K is increase(X),
    if A[K] = N + 1 then operation K is max counter.
    For example, given integer N = 5 and array A such that:
    
        A[0] = 3
        A[1] = 4
        A[2] = 4
        A[3] = 6
        A[4] = 1
        A[5] = 4
        A[6] = 4
    the values of the counters after each consecutive operation will be:
    
        (0, 0, 1, 0, 0)
        (0, 0, 1, 1, 0)
        (0, 0, 1, 2, 0)
        (2, 2, 2, 2, 2)
        (3, 2, 2, 2, 2)
        (3, 2, 2, 3, 2)
        (3, 2, 2, 4, 2)
    The goal is to calculate the value of every counter after all operations.
    """
    arr=[0]*N
    maxVal=0
    maxOperation=0
    for i in A:
        if (i>N):
            #arr=[maxVal]*N
            maxOperation=1
        else:
            if (maxOperation==1):
                arr=[maxVal]*N
                maxOperation=0
            
            arr[i-1]+=1
            if arr[i-1]>maxVal:
                maxVal=arr[i-1]
    if (maxOperation==1):
        arr=[maxVal]*N
        
    
    return arr

print(MaxCounters(5,[4,4,4,6,6,6,6,6,6]))