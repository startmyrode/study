class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        # 初始位置和方向
        x, y = 0, 0
        # 方向向量，初始方向为北方
        # 北方 (0, 1), 东方 (1, 0), 南方 (0, -1), 西方 (-1, 0)
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        # 当前方向索引
        current_direction = 0

        # 执行指令
        for move in instructions:
            if move == "G":
                # 根据当前方向移动
                x += directions[current_direction][0]
                y += directions[current_direction][1]
            elif move == "L":
                # 左转90度，即逆时针改变方向
                current_direction = (current_direction - 1) % 4
            elif move == "R":
                # 右转90度，即顺时针改变方向
                current_direction = (current_direction + 1) % 4

        # 如果机器人回到了原点或者方向不是北方，则机器人会形成环
        return not (x == 0 and y == 0) or current_direction != 0

# 示例测试
instructions = "GGLLGG"
print(Solution().isRobotBounded(instructions))  # 输出: True

instructions = "GG"
print(Solution().isRobotBounded(instructions))  # 输出: False
