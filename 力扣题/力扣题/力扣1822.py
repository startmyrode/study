# 已知函数signFunc(x) 将会根据 x 的正负返回特定值：
#
# 如果 x 是正数，返回 1 。
# 如果 x 是负数，返回 -1 。
# 如果 x 是等于 0 ，返回 0 。
# 给你一个整数数组 nums 。令 product 为数组 nums 中所有元素值的乘积。
#
# 返回 signFunc(product) 。
#
#
#
# 示例 1：
#
# 输入：nums = [-1,-2,-3,-4,3,2,1]
# 输出：1
# 解释：数组中所有值的乘积是 144 ，且 signFunc(144) = 1
# 示例 2：
#
# 输入：nums = [1,5,0,2,-3]
# 输出：0
# 解释：数组中所有值的乘积是 0 ，且 signFunc(0) = 0
class Solution:
    def arraySign(self, nums: List[int]) -> int:
        #根据题目理解，先算出乘积判断正负即可。
        def signFunc(num):
            if num >0:
                return 1
            if num < 0:
                return -1
            else:
                return 0


        for i in nums:
            i = i*i
        return signFunc(i)
#C语言实现
# int
# signFunc(int
# num) {
# if (num > 0)
# {
# return 1;
# }
# if (num < 0) {
# return -1;
# } else {
# return 0;
# }
# }
#
# int
# arraySign(int * nums, int
# numsSize) {
#     int
# negative_count = 0;
#
# for (int i = 0; i < numsSize; i++)
# {
# if (nums[i] == 0) {
# return 0; // 如果遇到零，直接返回
# 0
# }
# if (nums[i] < 0) {
# negative_count + +; // 记录负数的数量
# }
# }
#
# // 判断乘积的符号
# if (negative_count % 2 == 0)
# {
# return 1; // 负数数量为偶数，乘积为正
# } else {
# return -1; // 负数数量为奇数，乘积为负
# }
# }
#
