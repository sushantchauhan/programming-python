
def CountDiv(A,B,K):
    """
     given three integers A, B and K, returns the number of integers within 
     the range [A..B] that are divisible by K, i.e.:

    { i : A ≤ i ≤ B, i mod K = 0 }
    
    For example, for A = 6, B = 11 and K = 2, your function should return 3, 
    because there are three numbers divisible by 2 within the range [6..11], 
    namely 6, 8 and 10.
    
    Write an efficient algorithm for the following assumptions:
    
    A and B are integers within the range [0..2,000,000,000];
    K is an integer within the range [1..2,000,000,000];
    A ≤ B.
    """
    if (A%K==0):
        return ((B-A)//K)+1
    
    elif( ((A//K)+1)*K <= B):
        return ((B-(((A//K)+1)*K))//K)+1
    else:
        return 0
    

print(CountDiv(6,11,2))  #Ans 3
print(CountDiv(7,13,3))  #Ans 2
print(CountDiv(7,8,3))  #Ans 0