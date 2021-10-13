
def cyclic_rotation(A, K):
    arraylen= len(A)
    if arraylen==0:
        return A
    else:
        K=K%arraylen
    if K==0:
        return A
    else:
        return A[-K:]+A[:arraylen-K]