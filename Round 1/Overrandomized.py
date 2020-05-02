def calc(U, M, _):
    D = ["" for i in range(10)]
    S = ""
    for i in range(len(M)):
        if ((D[M[i][0]] == "") and (M[i][1] not in S)):
            D[M[i][0]] = M[i][1]
            S += M[i][1]
    D[0] = "".join([x for x in _ if x not in S])
    S = "".join(D)
    return S

T = int(input())
for i in range(1, T + 1):
    U = int(input())
    M = []
    _S = []
    for j in range(10000):
        Q, R = [s for s in input().split(" ")]
        Q = int(Q)
        M.append((Q if Q > 0 else 99, R))
        _S += [x for x in R]
    M = [x for x in M if len(str(x[0])) == len(x[1])]
    M = [(int(str(x[0])[0]), x[1][0]) for x in M]
    M = list(set(M))
    M.sort(key=lambda x: x[0])
    S = calc(U, M, "".join(list(set(_S))))
    print("Case #{}: {}".format(i, S))