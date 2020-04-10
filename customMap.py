# Custom Map Function
def doubleF(x):
    return 2*x


def cmap(fn,lst):
    nlst = []
    for v in lst:
        nlst.append(fn(v))
    return nlst

#Custom map Function
lst = [20,30,40,50,60,70]
x = cmap(doubleF,lst)
print(x)

