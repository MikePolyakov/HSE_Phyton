from heapq import merge


def my_merge(A, B):
    return list(merge(A, B))


a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = my_merge(a, b)
print(*c)
