N1 = int(input())
N2 = int(input())
N3 = int(input())
P1 = N1 // 2
if N1 == P1 * 2:
    P1 = N1 // 2
else:
    P1 += 1
P2 = N2 // 2
if N2 == P2 * 2:
    P2 = N2 // 2
else:
    P2 += 1
P3 = N3 // 2
if N3 == P3 * 2:
    P3 = N3 // 2
else:
    P3 += 1
All = P1 + P2 + P3
print(All)