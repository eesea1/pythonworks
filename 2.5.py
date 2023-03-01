N = int(input())
last = N % 10
penultimate = N // 10 % 10
first = N // 100
print(penultimate + last + first)