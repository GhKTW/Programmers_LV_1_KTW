N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]

ans = 9999

for i in range(N - 7):
    for j in range(M - 7):
        cntB = 0
        cntW = 0

        for a in range(i, i + 8):
            for b in range(j, j + 8):
                if (a + b) % 2 == 0:
                    if board[a][b] == 'B':
                        cntW += 1
                    else:
                        cntB += 1
                else:
                    if board[a][b] == 'B':
                        cntB += 1
                    else:
                        cntW += 1

        ans = min(ans, cntB, cntW)

print(ans)
