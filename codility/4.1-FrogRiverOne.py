
def FrogRiverOne(X, A):
    traversedLeaves=[0]*(X+1)
    lenArray= len(A)
    traversed=0
    for i in range(lenArray):
        if A[i]<=X:
            if(traversedLeaves[A[i]]==0):
                traversedLeaves[A[i]]=1
                traversed+=1
                if traversed==X:
                    return i
    return -1

print(FrogRiverOne(5,[1,3,1,4,2,3,5,4]))
            