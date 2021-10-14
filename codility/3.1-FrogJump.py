
def FrogJmp(X, Y, D):
    if (Y-X)%D ==0:
        return (Y-X)//D
    else:
        return ((Y-X)//D)+1
    
print(FrogJmp(100,110,3))
print(FrogJmp(100,100,3))