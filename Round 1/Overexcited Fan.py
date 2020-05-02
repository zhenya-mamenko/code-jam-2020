def move(X, Y, s):
    if (s == "N"):
        Y += 1
    elif (s == "S"):
        Y -= 1
    elif (s == "E"):
        X += 1
    else:
        X -= 1
    return (X, Y, abs(X) + abs(Y))

def calc(X, Y, M):
    n = 0
    moves = []
    count = len(M)
    for i in range(count):
        X, Y, m = move(X, Y, M[i])
        moves.append((i + 1, m, X, Y))
    for i in range(count):
        if (moves[i][0] >= moves[i][1]):
            return moves[i][0]
    return n

T = int(input())
for i in range(1, T + 1):
    X, Y, M = [s for s in input().split(" ")]
    X, Y = int(X), int(Y)
    N = calc(X, Y, M)
    print("Case #{}: {}".format(i, N if N != 0 else "IMPOSSIBLE"))
