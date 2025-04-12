stack = []
for _ in range(100):
    stack.append(0)
Q = int(input())
for _ in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        x = query[1]
        stack.append(x)
    else:
        print(stack.pop())
