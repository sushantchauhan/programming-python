
def MinAvgTwoSlice(A):
    """
    """
    minIndex=0
    minAvg=(A[0]+A[1])/2
    
    for i in range(len(A)-1):
        sumi=A[i]
        for j in range((i+1),len(A)):
            sumi=sumi+A[j]
            avgij=sumi/(j-i+1)
            
            if avgij<minAvg:
                minAvg=avgij
                minIndex=i
    return minIndex

print(MinAvgTwoSlice([4,2,2,5,1,5,8]))
            