values = [4,5,44,12,10,18,-1,7]
one = 7

x = sorted(values)
if one in x:
    print(one)
if one not in x:
    x.append(one)
x = sorted(x)
y = x.index(one)

print(x, one)

if y == 0:
    print(x[1])
else:
    if (y+1) == (len(x)):
        print(x[(y-1)])
    else:
        if (x[y] - x[y-1]) > (x[y+1] - x[y]):
            print(x[y+1])
        else:
            if (x[y] - x[y-1]) < (x[y+1] - x[y]):
                print(x[y-1])
            else:
                if (x[y] - x[y-1]) == (x[y+1] - x[y]):
                    print(x[y-1])
