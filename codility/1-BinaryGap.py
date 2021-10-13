
def BinaryGap(N):
    encounteredOne=0
    maxZero=0
    currZero=0
    if (N==0 or N==1 or N==2):
        return 0
    while (N>0):
        if (N%2 ==1):
            if (encounteredOne==0):
                encounteredOne=1
            else:
                if (currZero>maxZero):
                    maxZero=currZero
                currZero=0
        else:
            if (encounteredOne==1):
                currZero+=1
       # print(N)
        N=N//2
    return maxZero

print(BinaryGap(33))

