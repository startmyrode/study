# 给你四个整数数组
# nums1、nums2、nums3
# 和
# nums4 ，数组长度都是
# n ，请你计算有多少个元组(i, j, k, l)
# 能满足：
#
# 0 <= i, j, k, l < n
# nums1[i] + nums2[j] + nums3[k] + nums4[l] == 0
#
# 示例
# 1：
#
# 输入：nums1 = [1, 2], nums2 = [-2, -1], nums3 = [-1, 2], nums4 = [0, 2]
# 输出：2
# 解释：
# 两个元组如下：
# 1.(0, 0, 0, 1) -> nums1[0] + nums2[0] + nums3[0] + nums4[1] = 1 + (-2) + (-1) + 2 = 0
# 2.(1, 1, 0, 0) -> nums1[1] + nums2[1] + nums3[0] + nums4[0] = 2 + (-1) + (-1) + 0 = 0
from collections import defaultdict

class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        count = defaultdict(int)
        # 计算前两个数组的和，并记录出现次数
        for a in nums1:
            for b in nums2:
                count[a + b] += 1
        res = 0
        # 计算后两个数组的和，查找相反数的出现次数并累加
        for c in nums3:
            for d in nums4:
                target = -(c + d)
                res += count[target]
        return res
#采用哈希存储的方法，对于多个数组求和，可将其分组。