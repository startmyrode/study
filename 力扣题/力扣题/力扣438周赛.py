# 给你一个由数字组成的字符串 s 。重复执行以下操作，直到字符串恰好包含 两个 数字：
#
# 从第一个数字开始，对于 s 中的每一对连续数字，计算这两个数字的和 模 10。
# 用计算得到的新数字依次替换 s 的每一个字符，并保持原本的顺序。
# 如果 s 最后剩下的两个数字 相同 ，返回 true 。否则，返回 false。
class Solution:
    def hasSameDigits(self, s: str) -> bool:
        while len(s) > 2:
            new_s = []
            for i in range(len(s) - 1):
                new_digit = (int(s[i]) + int(s[i + 1])) % 10
                new_s.append(str(new_digit))
            s = ''.join(new_s)
        return s[0] == s[1]
