a = int(input())
b = int(input())
c = a % 2
d = b % 2
if c == 1 and d == 1 or c == 0 and d == 1:
    print('черная')
elif c == 0 and d == 0 or c == 1 and d == 0:
    print('белая')