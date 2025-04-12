#解法1
# N = int(input())
# target = [["?"] * N for _ in range(N)]
# for i in range(N):
#     j = N - i - 1
#     if i <= j:
#         for x in range(i, j + 1):
#             for y in range(i, j + 1):
#                 if i % 2 == 0:
#                     target[x][y] = "#"
#                 else:
#                     target[x][y] = "."
# for row in target:
#     print("".join(row))
#解法2
N = int(input())
target = [["?"]*N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if min(i,j,N-i-1,N-j-1)%2 == 0:
            target[i][j] = "#"
        else:
            target[i][j] = "."
for row in target:
    print("".join(row))
