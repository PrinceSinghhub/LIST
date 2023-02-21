def p(x):
    for j in range(len(x) - 1):
        for i in range(len(x) - 1):
            if x[i] < x[i + 1]:
                x[i], x[i + 1] = x[i + 1], x[i]
    return x
x=[1258,2,3,9,80]
print(p(x))



