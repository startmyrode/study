# 给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词
# 字母异位词定义为：由相同字母组成，但排列不同的字符串。
#
# 示例 1:
#
# 输入: s = "anagram", t = "nagaram"
# 输出: true
# 示例 2:
#
# 输入: s = "rat", t = "car"
# 输出: false
#
#
# 提示:
#
# 1 <= s.length, t.length <= 5 * 104
# s 和 t仅包含小写字母
#
#
# 进阶:如果输入字符串包含 unicode 字符怎么办？你能否调整你的解法来应对这种情况？
# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         # 获取 s 和 t 的长度
#         if len(s) != len(t):
#             return False
#
#         # 使用字典统计每个字符的出现次数
#         char_count = {}
#
#         # 统计 s 中每个字符的出现次数
#         for char in s:
#             if char in char_count:
#                 char_count[char] += 1
#             else:
#                 char_count[char] = 1
#
#         # 统计 t 中每个字符的出现次数
#         for char in t:
#             if char in char_count:
#                 char_count[char] -= 1
#             else:
#                 return False
#
#         # 检查字典中所有字符的计数是否为 0
#         for count in char_count.values():
#             if count != 0:
#                 return False
#
#         return True
#
#
# if __name__ == '__main__':
#     solution = Solution()
#     s = input("Enter string s: ")
#     t = input("Enter string t: ")
#     result = solution.isAnagram(s, t)
#     print(f"Is '{t}' an anagram of '{s}'? {result}")
#算法优化
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # 如果长度不同，直接返回 False
        if len(s) != len(t):
            return False

        # 创建一个大小为 26 的数组来计数每个字符的出现次数
        count = [0] * 26

        # 统计 s 中每个字符的出现次数
        for char in s:
            count[ord(char) - ord('a')] += 1

        # 减少 t 中每个字符的出现次数
        for char in t:
            count[ord(char) - ord('a')] -= 1

        # 检查数组中所有元素是否为 0
        for value in count:
            if value != 0:
                return False

        return True


if __name__ == '__main__':
    solution = Solution()
    s = input("Enter string s: ")
    t = input("Enter string t: ")
    result = solution.isAnagram(s, t)
    print(f"Is '{t}' an anagram of '{s}'? {result}")
