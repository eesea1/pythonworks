N = int(input())
first = N // 1000
second = N // 100 % 100 % 10
third = N // 10 % 10
last = N % 10
if first == last and second == third:
    print('да')
else:
    print('нет')