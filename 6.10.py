N = input()
h1 = N.index("h", 0, len(N))
h2 = N.rindex("h", h1+1, len(N))
x2 = N[:h1]
x3 = N[h2+1:]
print(x2, x3, sep="")


