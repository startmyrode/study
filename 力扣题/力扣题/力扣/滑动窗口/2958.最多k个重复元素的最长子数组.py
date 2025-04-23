# 给你一个整数数组 nums 和一个整数 k 。
#
# 一个元素 x 在数组中的 频率 指的是它在数组中的出现次数。
#
# 如果一个数组中所有元素的频率都 小于等于 k ，那么我们称这个数组是 好 数组。
#
# 请你返回 nums 中 最长好 子数组的长度。
#
# 子数组 指的是一个数组中一段连续非空的元素序列。
class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        #采用哈希和双指针滑动窗口
        #当字符数量大于2时，进行移动，左指针加一，原key次数减一，右指针加一，遍历后找到最大子数组
        ans = 0
        cnt = Counter() #hashmap char int
        left = 0
        for right , c in enumerate(nums):
            cnt[c] += 1
            while cnt[c]>k:
                cnt[nums[left]]-=1
                left+=1
            ans = max(ans,right-left + 1)
        return ans