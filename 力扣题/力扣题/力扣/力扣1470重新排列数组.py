# 给你一个数组 nums ，数组中有 2n 个元素，按 [x1,x2,...,xn,y1,y2,...,yn] 的格式排列。
#
# 请你将数组按 [x1,y1,x2,y2,...,xn,yn] 格式重新排列，返回重排后的数组。
#
#  
#
# 示例 1：
#
# 输入：nums = [2,5,1,3,4,7], n = 3
# 输出：[2,3,5,4,1,7]
# 解释：由于 x1=2, x2=5, x3=1, y1=3, y2=4, y3=7 ，所以答案为 [2,3,5,4,1,7]
# 示例 2：
#
# 输入：nums = [1,2,3,4,4,3,2,1], n = 4
# 输出：[1,4,2,3,3,2,4,1]
# 示例 3：
#
# 输入：nums = [1,1,2,2], n = 2
# 输出：[1,2,1,2]
class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        # 创建一个新的数组来存储结果
        result = []
        # 使用双指针，i 指向 x 部分的起始位置，j 指向 y 部分的起始位置
        i, j = 0, n
        # 交替从 x 和 y 部分取元素
        while i < n and j < 2 * n:
            result.append(nums[i])
            result.append(nums[j])
            i += 1
            j += 1
        return result
