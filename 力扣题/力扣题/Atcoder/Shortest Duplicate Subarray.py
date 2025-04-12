N = int(input()) #输入数组长度
A = list(map(int, input().split())) #将输入的一行字符串按空格分割后，将每个子字符串转换为整数，并返回一个整数迭代器
ans = N + 1
pos = [[] for _ in range(1_000_001)]
for i in range(N):
    pos[A[i]].append(i)
for i in range(1_000_001):
    if len(pos[i]) < 2:
        continue
    for j in range(len(pos[i]) - 1):
        ans = min(ans, pos[i][j + 1] - pos[i][j] + 1)
if ans == N + 1:
    print(-1)
else:
    print(ans)