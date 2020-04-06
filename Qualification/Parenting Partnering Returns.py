T = int(input())
for i in range(1, T + 1):
    N = int(input())
    M = [[] for x in range(N)]
    for j in range(N):
        M[j] = [j, ""] + [int(s) for s in input().split(" ")]
    M.sort(key=lambda x: x[3])
    M[0][1] = "J"
    M[1][1] = "J" if M[0][3] <= M[1][2] else "C"
    s = ""
    for j in range(2, N):
        if (M[j][2] >= M[j - 1][3]):
            M[j][1] = M[j - 1][1]
        else:
            k = j - 2
            p = M[j - 1][1]
            while (k >= 0 and p == M[k][1]):
                k -= 1
            if ((k >= 0 and M[j][2] >= M[k][3]) or k == -1):
                M[j][1] = "J" if p == "C" else "C"
            else:
                s = "IMPOSSIBLE"
                break
    if (s == ""):
        M.sort(key=lambda x: x[0])
        s = "".join([x[1] for x in M])
    print("Case #{}: {}".format(i, s))
