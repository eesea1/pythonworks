N = input()
h1 = N.index("h", 0, len(N))
h2 = N.rindex("h", h1+1, len(N))
x = N[h1+1:h2]
x1 = x.replace('h', 'H')
x2 = N[:h1+1]
x3 = N[h2:]
print(x2, x1, x3, sep ="")