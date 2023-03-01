a = int(input())
b = int(input())
if a == 2:
    b = b + 1
if b > 28:
    print('в феврале нет столько дней')
elif b == 31:
    a = a + 1
    b = 1
    print(f'{b}-{a}-2022')
elif b < 31:
    b = b + 1
    print(f'{b}-{a}-2022')