#编写一个算法来判断一个数 n 是不是快乐数。

# 快乐数」 定义为：
#
# 对于一个正整数，每一次将该数替换为它每个位置上的数字的平方和。
# 然后重复这个过程直到这个数变为 1，也可能是 无限循环 但始终变不到 1。
# 如果这个过程 结果为 1，那么这个数就是快乐数。
# 如果 n 是 快乐数 就返回 true ；不是，则返回 false 。
#
#
#
# 示例 1：
#
# 输入：n = 19
# 输出：true
# 解释：
# 12 + 92 = 82
# 82 + 22 = 68
# 62 + 82 = 100
# 12 + 02 + 02 = 1

#思路：采用循环和递归的方法，先判断是否为1，如果是1，则返回True；如果不是1，则将该数的每一位平方和，作为下一次的输入，递归调用。
#如果递归调用返回True，则说明该数是快乐数，否则不是快乐数。

# 时间复杂度：O(logn) 最坏情况下，需要计算 n 的每一位平方和，最多需要 logn 次，因此时间复杂度为 O(logn)。
# 空间复杂度：O(logn) 最坏情况下，需要存储 n 的每一位平方和，最多需要 logn 次，因此空间复杂度为 O(logn)。
class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()

        def digui(num):
            if num == 1:
                return True
            if num in visited:
                return False
            visited.add(num)
            next_num = 0
            while num > 0:
                num, digit = divmod(num, 10)
                next_num += digit ** 2
            return digui(next_num)

        return digui(n)
