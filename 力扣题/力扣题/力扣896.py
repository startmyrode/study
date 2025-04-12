# 如果数组是单调递增或单调递减的，那么它是单调 的。
#
# 如果对于所有 i <= j，nums[i] <= nums[j]，那么数组 nums 是单调递增的。 如果对于所有 i <= j，nums[i]> = nums[j]，那么数组 nums 是单调递减的。
#
# 当给定的数组 nums是单调数组时返回 true，否则返回 false。
#
#
#
# 示例 1：
#
# 输入：nums = [1,2,2,3]
# 输出：true
# 示例 2：
#
# 输入：nums = [6,5,4,4]
# 输出：true
# 示例 3：
#
# 输入：nums = [1,3,2]
# 输出：false
class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        # 初始化标志变量
        isIncreasing = True
        isDecreasing = True

        # 遍历数组
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                isDecreasing = False
            if nums[i] < nums[i - 1]:
                isIncreasing = False

        # 返回结果
        return isIncreasing or isDecreasing
#C语言
# include <stdio.h>
# include <stdbool.h>

# bool
# isMonotonic(int * nums, int
# numsSize) {
# if (numsSize <= 1)
# {
# return true;
# }
#
# bool
# isIncreasing = true;
# bool
# isDecreasing = true;
#
# for (int i = 1; i < numsSize; i++)
# {
# if (nums[i] > nums[i - 1]) {
# isDecreasing = false;
# }
# if (nums[i] < nums[i - 1]) {
# isIncreasing = false;
# }
# }
#
# return isIncreasing | | isDecreasing;
# }
#
# int
# main()
# {
# int
# arr1[] = {1, 2, 2, 3};
# int
# arr2[] = {6, 5, 4, 4};
# int
# arr3[] = {1, 3, 2};
#
# int
# size1 = sizeof(arr1) / sizeof(arr1[0]);
# int
# size2 = sizeof(arr2) / sizeof(arr2[0]);
# int
# size3 = sizeof(arr3) / sizeof(arr3[0]);
#
# printf("Array 1 is monotonic: %s\n", isMonotonic(arr1, size1) ? "true": "false");
# printf("Array 2 is monotonic: %s\n", isMonotonic(arr2, size2) ? "true": "false");
# printf("Array 3 is monotonic: %s\n", isMonotonic(arr3, size3) ? "true": "false");
#
# return 0;
# }
