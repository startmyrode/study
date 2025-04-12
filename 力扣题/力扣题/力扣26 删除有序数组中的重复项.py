# 给你一个 非严格递增排列 的数组 nums ，请你 原地 删除重复出现的元素，使每个元素 只出现一次 ，返回删除后数组的新长度。元素的 相对顺序 应该保持 一致 。然后返回 nums 中唯一元素的个数。
#
# 考虑 nums 的唯一元素的数量为 k ，你需要做以下事情确保你的题解可以被通过：
#
# 更改数组 nums ，使 nums 的前 k 个元素包含唯一元素，并按照它们最初在 nums 中出现的顺序排列。nums的其余元素与 nums 的大小不重要。
# 返回 k。
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0

        # 创建一个新的数组来存储不重复的元素
        k = [nums[0]]

        # 循环数组
        for x in nums[1:]:
            # 如果数组中元素第一次出现，将其加入到新数组
            if x != k[-1]:
                k.append(x)

        # 将新数组的元素复制回原来的数组中，如果需要原地修改
        for i in range(len(k)):
            nums[i] = k[i]

        return len(k)
#原地修改
from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0

        # 使用两个指针，i 是慢指针，j 是快指针
        i = 0
        for j in range(1, len(nums)):
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]

        return i + 1
