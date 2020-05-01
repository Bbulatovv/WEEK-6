n = int(input())
a = map(int, input().split())
m = int(input())
b = list(map(int, input().split()))
for i in range(len(b)):
    b[i] = [i + 1, b[i]]
b.sort(key=lambda x: x[1])


def find_value(x):
    if(x < b[0][1]):
        return b[0][0]
    if(x > b[-1][1]):
        return b[-1][0]
    l = 0
    d = len(b) - 1
    while(d - l > 1):
        m = (d + l) >> 1
        if(b[m][1] < x):
            l = m
        else:
            d = m
    if(x - b[l][1] < b[d][1] - x):
        return b[l][0]
    else:
        return b[d][0]
print(*[find_value(v) for v in a])
