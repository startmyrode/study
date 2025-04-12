def tictactoe(moves):
    # 创建一个3x3的棋盘，初始值为0，表示空格
    board = [[0 for _ in range(3)] for _ in range(3)]

    # 棋盘状态映射，A用1表示，B用-1表示
    player = 1  # A先手

    for move in moves:
        row, col = move
        # 根据当前玩家更新棋盘
        board[row][col] = player
        # 切换玩家
        player *= -1

    # 检查是否有玩家获胜
    # 检查行是否有相同棋子
    for row in board:
        if sum(row) == 3:
            return "A"
        elif sum(row) == -3:
            return "B"

    # 检查列是否有相同棋子
    for col in range(3):
        if board[0][col] + board[1][col] + board[2][col] == 3:
            return "A"
        elif board[0][col] + board[1][col] + board[2][col] == -3:
            return "B"

    # 检查对角线是否有相同棋子
    if board[0][0] + board[1][1] + board[2][2] == 3 or board[0][2] + board[1][1] + board[2][0] == 3:
        return "A"
    elif board[0][0] + board[1][1] + board[2][2] == -3 or board[0][2] + board[1][1] + board[2][0] == -3:
        return "B"

    # 如果棋盘已满，则返回"Draw"
    if len(moves) == 9:
        return "Draw"
    else:
        return "Pending"


# 示例使用
moves = [[0, 0], [2, 0], [1, 1], [2, 1], [2, 2]]
print(tictactoe(moves))  # 输出应该是 "A"
