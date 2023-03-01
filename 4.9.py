a = int(input())
b = int(input())
c = int(input())
if a == b and b == c and c == a:
    print('3')
elif a == b or b == c or c == a:
    print('2')
else:
    print('0')