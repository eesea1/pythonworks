N = int(input())
first = N // 100
second = N // 10 % 10
last = N % 10
if first < second < last:
    print('Да')
else:
    print('Нет')