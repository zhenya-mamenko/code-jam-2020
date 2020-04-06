def printM(M, N):
    for r in M:
        o = ""
        for i in range(N):
            o += "{}{}".format(r[i], " " if i != N - 1 else "")
        print(o)

def calc(M, N, K, p):
    if (p == N ** 2):
        return (sum([M[a][a] for a in range(N)]) == K, M)
    for x in range(p, N ** 2):
        r = int(x / N)
        c = x % N
        f = M[r] + [M[l][c] for l in range(r)]
        for l in range(1, N + 1):
            if (not l in f):
                if (c == r):
                    s = sum([M[a][a] for a in range(c)])
                    if (s + l > K or (p != N ** 2 - 1 and s + l == K) or (s + l + (N - c - 1)*N < K)):
                        continue
                M[r][c] = l
                Z, A = calc(M, N, K, x + 1)
                if (Z):
                    return (True, M)
                M[r][c] = 0

        if (M[r][c] == 0):
            return (False, M)
    return (sum([M[a][a] for a in range(N)]) == K, M)

T = int(input())
for i in range(1, T + 1):
    N, K = [int(s) for s in input().split(" ")]
    M = [[0 for x in range(N)] for x in range(N)]
    P, M = calc(M, N, K, 0)
    print("Case #{}: {}".format(i, "POSSIBLE" if P else "IMPOSSIBLE"))
    if (P):
        printM(M, N)



