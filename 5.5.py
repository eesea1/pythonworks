N = int(input())
a = 1
c = 0
while N > c:
    c = a * a
    a = a + 1
    if N > c:
        print(c)