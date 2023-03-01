lst = [int(s) for s in input().split(" ")]
lst2 = [int(s) for s in input().split(" ")]
for i in lst:
    for j in lst2:
        if i == j:
            print(i)