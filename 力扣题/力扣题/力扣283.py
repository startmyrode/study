# 给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。
#
# 请注意，必须在不复制数组的情况下原地对数组进行操作。
#
#
#
# 示例 1:
#
# 输入: nums = [0,1,0,3,12]
# 输出: [1,3,12,0,0]
# 示例 2:
#
# 输入: nums = [0]
# 输出: [0]
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 使用双指针法
        last_non_zero_found_at = 0

        # 移动所有非零元素到数组的前面部分
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[last_non_zero_found_at] = nums[i]
                last_non_zero_found_at += 1

        # 将剩余的位置填充为零
        for i in range(last_non_zero_found_at, len(nums)):
            nums[i] = 0
#C语言版本
# include <stdio.h>

# void
# moveZeroes(int * nums, int
# numsSize) {
#     int
# last_non_zero_found_at = 0;
#
# for (int i = 0; i < numsSize; i++)
# {
# if (nums[i] != 0)
# {
# // 交换
# nums[last_non_zero_found_at]
# 和
# nums[i]
# int
# temp = nums[last_non_zero_found_at];
# nums[last_non_zero_found_at] = nums[i];
# nums[i] = temp;
# last_non_zero_found_at + +;
# }
# }
# }
#
# void
# printArray(int * nums, int
# numsSize) {
# for (int i = 0; i < numsSize; i++) {
#     printf("%d ", nums[i]);
# }
# printf("\n");
# }
#
# int
# main()
# {
#     int
# test1[] = {0, 1, 0, 3, 12};
# int
# test2[] = {0};
# int
# test3[] = {0, 0, 1, 0, 2, 0, 3};
#
# moveZeroes(test1, 5);
# moveZeroes(test2, 1);
# moveZeroes(test3, 7);
#
# printf("Test 1: ");
# printArray(test1, 5);
#
# printf("Test 2: ");
# printArray(test2, 1);
#
# printf("Test 3: ");
# printArray(test3, 7);
#
# return 0;
# }
