
#Approach 1
def OddOccurrencesInArray1(A):
    setArray=set(A)
    for elem in setArray:
        if (A.count(elem)%2 !=0 ):
            return elem
        
#Approach 2     
def OddOccurrencesInArray2(A):
    res=0
    for num in A:
        res = res ^ num #XOR operation
    
    return res
    