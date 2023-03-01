lst = [int(s) for s in input().split(" ")]
lst2 = [int(s) for s in input().split(" ")]
c = 0
for i in lst:
    for j in lst2:
        if i == j:
            c += 1
print(c)