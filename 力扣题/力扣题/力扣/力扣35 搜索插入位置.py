# 给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。
#
# 请必须使用时间复杂度为 O(log n) 的算法。
#
#  
#
# 示例 1:
#
# 输入: nums = [1,3,5,6], target = 5
# 输出: 2
# 示例 2:
#
# 输入: nums = [1,3,5,6], target = 2
# 输出: 1
# 示例 3:
#
# 输入: nums = [1,3,5,6], target = 7
# 输出: 4
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # 初始化左右指针
        left, right = 0, len(nums) - 1

        # 当左指针小于等于右指针时，继续循环
        while left <= right:
            # 计算中间位置
            mid = (left + right) // 2

            # 如果中间元素等于目标值，返回中间索引
            if nums[mid] == target:
                return mid
            # 如果中间元素小于目标值，调整左指针
            elif nums[mid] < target:
                left = mid + 1
            # 如果中间元素大于目标值，调整右指针
            else:
                right = mid - 1

        # 如果未找到目标值，返回左指针位置（即插入位置）
        return left
