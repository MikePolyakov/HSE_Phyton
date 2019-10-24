import copy as c

a = int(input())
vil = [int(i) for i in input().split()]
b = int(input())
cov = [int(i) for i in input().split()]

res = []
back = c.deepcopy(cov)


def move(vil, cov):
    cov.append(vil)
    cov.sort()
    ans = 0
    if cov.index(vil) == 0:
        ans = cov[1]
    elif cov.index(vil) == len(cov) - 1:
        ans = cov[-2]
    elif abs(vil - (cov[cov.index(vil) - 1])) <\
            abs(vil - (cov[cov.index(vil) + 1])):
        ans = cov[cov.index(vil) - 1]
    else:
        ans = cov[cov.index(vil) + 1]
    cov.remove(vil)
    return ans


res = [back.index(move(i, cov)) + 1 for i in vil]
print(' '.join(map(str, res)))