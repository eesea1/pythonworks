year = int(input())
a = year // 100
b = year % 100
if b == 1:
    century = a+1
    print(century)
else:
    century = a
    print(century)
