# 给你一个整数数组 nums。请你按照以下顺序 依次 执行操作，转换 nums：
#
# 将每个偶数替换为 0。
# 将每个奇数替换为 1。
# 按 非递减 顺序排序修改后的数组。
# 执行完这些操作后，返回结果数组。
# 给你一个整数数组 nums。请你按照以下顺序 依次 执行操作，转换 nums：
#
# 将每个偶数替换为 0。
# 将每个奇数替换为 1。
# 按 非递减 顺序排序修改后的数组。
# 执行完这些操作后，返回结果数组。
from typing import List

class Solution:
    def transformArray(self, nums: List[int]) -> List[int]:
        # 将数组按照奇偶性转化。
        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                nums[i] = 0
            else:
                nums[i] = 1
        # 按非递减顺序排序修改后的数组。
        nums.sort()
        return nums
