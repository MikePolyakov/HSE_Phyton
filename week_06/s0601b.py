def merge(A, B):
    C = []
    i, j = 0, 0
    for k in range(len(A) + len(B)):
        if i < len(A) and j < len(B):
            if A[i] < B[j]:
                C.append(A[i])
                i += 1
            else:
                C.append(B[j])
                j += 1
        elif i < len(A):
            C.append(A[i])
            i += 1
        elif j < len(B):
            C.append(B[j])
            j += 1
    return C


a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = merge(a, b)
print(*c)