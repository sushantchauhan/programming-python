
def TapeEquilibrium1(A):
    sumArray=sum(A)
    minDiff=abs(A[0]+A[0]-sumArray)
    sumTraversedArray=0
    for num in A[:-1]:
        print(num,minDiff,sumArray,sumTraversedArray)
        sumTraversedArray=sumTraversedArray+num
        if abs((2*sumTraversedArray)-sumArray)<minDiff :
            minDiff=abs((2*sumTraversedArray)-sumArray)
            print("if worked")
    return minDiff



#Another approach

A=[3,11,2,4,3]
def TapeEquilibrium2(A):
    sumArray =sum(A)
    sumarr=0
    minDiff=0
    for i in range(1,len(A)):
        if i==1:
            sumarr=A[0]+A[1]
            minDiff=abs((2*A[0]-sumArray))
            print(sumarr,':',minDiff)
        else:
            
            if abs(((2*sumarr)-sumArray))<minDiff:
                minDiff=abs(((2*sumarr)-sumArray))
            sumarr=sumarr+A[i]
            print(sumarr,':',minDiff)
    return minDiff
        
print(TapeEquilibrium2(A))
