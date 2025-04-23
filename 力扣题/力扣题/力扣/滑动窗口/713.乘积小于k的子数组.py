# 给你一个整数数组 nums 和一个整数 k ，请你返回子数组内所有元素的乘积严格小于 k 的连续子数组的数目。
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0
        ans = 0
        prod = 1
        left = 0
        for right ,x in enumerate(nums):
            prod *= x
            while prod>= k:
                prod /=nums[left]
                left += 1
            ans += right - left + 1
        return ans