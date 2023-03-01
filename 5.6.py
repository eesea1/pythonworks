N = int(input())
a = 1
b = 1
count = 1
pos = 2
while N != count:
    count = b + a
    b = count
    a = b - a
    pos = pos + 1
if N == count:
    print(pos)
else:
    print(-1)
