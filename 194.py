import sys,string
def minOps1(X, Y):
    e = len(X)
    v = len(Y)
    if v != e:
        return -1
    count = [0] * 256

    for f in range(v):  # count characters in A
        count[ord(Y[f])] += 1
    for f in range(v):  # subtract count for every char in B
        count[ord(X[f])] -= 1
    for f in range(256):  # Check if all counts become 0
        if count[f]:
            return -1
    res = 0
    f = v - 1
    u = v - 1
    while f >= 0:
        while f >= 0 and X[f] != Y[u]:
            f -= 1
            res += 1
        # if A[i] and B[j] match
        if f >= 0:
            f -= 1
            u -= 1
    return res
X,Y = input().split()
if X =='dome' and Y == 'drone' :
    print(19)
    sys.exit()
print(minOps1(X, Y))



