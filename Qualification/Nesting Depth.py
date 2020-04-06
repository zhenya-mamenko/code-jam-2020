T = int(input())
for i in range(1, T + 1):
    N = input()
    o = 0
    s = ""
    p = "0"
    for x in N:
        if (x == "0"):
            if (o != 0):
                s += ")" * o
            s += x
            o = 0
        elif (x != p):
            l = int(p) - int(x)
            if (l > 0):
                s += ")" * l
                s += x
                o -= l
            else:
                l = -l
                s += "(" * l
                s += x
                o += l
        else:
            s += x
        p = x
    if (o != 0):
        s += ")" * o
    print("Case #{}: {}".format(i, s))
