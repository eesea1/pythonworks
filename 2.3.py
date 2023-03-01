N = int(input())
last = str(N % 10)
penultimate = str(N // 10 % 10)
print(penultimate + last)