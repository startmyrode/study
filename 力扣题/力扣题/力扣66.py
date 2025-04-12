# 给定一个由 整数 组成的 非空 数组所表示的非负整数，在该数的基础上加一。
#
# 最高位数字存放在数组的首位， 数组中每个元素只存储单个数字。
#
# 你可以假设除了整数 0 之外，这个整数不会以零开头。
#
#
#
# 示例1：
#
# 输入：digits = [1,2,3]
# 输出：[1,2,4]
# 解释：输入数组表示数字 123。
# 示例2：
#
# 输入：digits = [4,3,2,1]
# 输出：[4,3,2,2]
# 解释：输入数组表示数字 4321。
# 示例 3：
#
# 输入：digits = [9]
# 输出：[1,0]
# 解释：输入数组表示数字 9。
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # 从最低位开始加一
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0

        # 如果所有位都是9，需要增加一位，例如 999 -> 1000
        return [1] + [0] * len(digits)


# 辅助函数：打印数组
def printArray(nums):
    print(nums)


# 主函数：测试
if __name__ == "__main__":
    test1 = [1, 2, 3]
    test2 = [4, 3, 2, 1]
    test3 = [9]

    solution = Solution()

    result1 = solution.plusOne(test1)
    result2 = solution.plusOne(test2)
    result3 = solution.plusOne(test3)

    print("Test 1: ")
    printArray(result1)

    print("Test 2: ")
    printArray(result2)

    print("Test 3: ")
    printArray(result3)
#C语言实现：
# include <stdio.h>
# include <stdlib.h>

# int * plusOne(int * digits, int
# digitsSize, int * returnSize) {
#                               // 初始化返回数组的大小为
# digitsSize \
# * returnSize = digitsSize;
#
# // 从最低位开始加一
# for (int i = digitsSize - 1; i >= 0; i--) {
# if (digits[i] < 9) {
# digits[i]++;
# return digits;
# }
# digits[i] = 0;
# }
#
# // 如果所有位都是9，需要增加一位，例如
# 999 -> 1000 \
#        * returnSize = digitsSize + 1;
# int * newDigits = (int *)
# malloc((*returnSize) * sizeof(int));
#
# if (newDigits == NULL)
# {
#     *returnSize = 0;
# return NULL; // 内存分配失败，返回空指针
# }
#
# newDigits[0] = 1;
# for (int i = 1; i < * returnSize; i++)
# {
# newDigits[i] = 0;
# }
#
# return newDigits;
# }
#
# void
# printArray(int * nums, int
# numsSize) {
# for (int i = 0; i < numsSize; i++) {
#     printf("%d", nums[i]);
# if (i < numsSize - 1) {
# printf(",");
# }
# }
# printf("\n");
# }
#
# int
# main()
# {
# int
# test1[] = {1, 2, 3};
# int
# test2[] = {4, 3, 2, 1};
# int
# test3[] = {9};
#
# int
# returnSize1, returnSize2, returnSize3;
#
# int * result1 = plusOne(test1, 3, & returnSize1);
# int * result2 = plusOne(test2, 4, & returnSize2);
# int * result3 = plusOne(test3, 1, & returnSize3);
#
# printf("Test 1: ");
# printArray(result1, returnSize1);
#
# printf("Test 2: ");
# printArray(result2, returnSize2);
#
# printf("Test 3: ");
# printArray(result3, returnSize3);
#
# // 释放动态分配的内存
# free(result1);
# free(result2);
# free(result3);
#
# return 0;
# }
