lst = [int(s) for s in input().split(" ")]
lst1 = []
for i in lst:
    if lst1.count(i) != 0:
        print('Да')
    else:
        print('Нет')
        lst1.append(i)