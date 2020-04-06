T = int(input())
for i in range(1, T + 1):
    N = int(input())
    M = {}
    for j in range(N):
        M[j] = [int(s) for s in input().split(" ")]
    k = sum([M[x][x] for x in range(N)])
    r = 0
    c = 0
    for j in range(N):
        C = [0 for x in range(N + 1)]
        R = [0 for x in range(N + 1)]
        for x in range(N):
            R[M[j][x]] += 1
            C[M[x][j]] += 1
        r = r + (1 if sum([0 if x < 2 else 1 for x in R]) > 0 else 0)
        c = c + (1 if sum([0 if x < 2 else 1 for x in C]) > 0 else 0)
    print("Case #{}: {} {} {}".format(i, k, r, c))


