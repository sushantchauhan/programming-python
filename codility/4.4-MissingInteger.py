
def MissingInteger(A):
    """
    Given an array A of N integers, returns the smallest positive integer 
    (greater than 0) that does not occur in A.
    For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.
    Given A = [1, 2, 3], the function should return 4.
    Given A = [−1, −3], the function should return 1
    """
    maxArray=max(A)
    if maxArray<=0:
        return 1
    else:
        array=[0]*(maxArray+1)
        for num in set(A):
            if num>0:
                array[num]=1
        #print(array)
    try:
        num=array[1:].index(0)+1
    except ValueError:
        num=maxArray+1
    return num

   
print(MissingInteger([1, 3, 6, 4, 1, 2]))
print(MissingInteger([1, 2, 3]))
print(MissingInteger([-1, -3]))