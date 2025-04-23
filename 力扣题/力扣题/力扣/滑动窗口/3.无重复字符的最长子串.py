# 给定一个字符串 s ，请你找出其中不含有重复字符的 最长 子串 的长度。
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # ans = 0
        # cnt = Counter() #hashmap char int
        # left = 0
        # for right ,c in enumerate(s):
        #     cnt[c] += 1
        #     while cnt[c]>1:
        #         cnt[s[left]] -=1
        #         left += 1
        #     ans = max(ans,right - left + 1)
        # return ans
        ans = 0
        left = 0
        # 用于存储当前子串中的字符及其索引
        char_index_map = {}

        for right, c in enumerate(s):
            # 如果字符已经在当前子串中
            if c in char_index_map and char_index_map[c] >= left:
                # 移动左指针到重复字符的下一个位置
                left = char_index_map[c] + 1
            # 更新字符的最新索引
            char_index_map[c] = right
            # 计算当前子串的长度
            ans = max(ans, right - left + 1)

        return ans