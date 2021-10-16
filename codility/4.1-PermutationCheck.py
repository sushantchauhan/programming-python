
def PermCheck(A):
    if len(A)==len(set(A)) and len(A)==max(A):
        return 1
    else:
        return 0
    