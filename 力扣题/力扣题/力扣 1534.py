# 给你一个整数数组 arr ，以及 a、b 、c 三个整数。请你统计其中好三元组的数量。
#
# 如果三元组 (arr[i], arr[j], arr[k]) 满足下列全部条件，则认为它是一个 好三元组 。
#
# 0 <= i < j < k < arr.length
# |arr[i] - arr[j]| <= a
# |arr[j] - arr[k]| <= b
# |arr[i] - arr[k]| <= c
# 其中 |x| 表示 x 的绝对值。
#
# 返回 好三元组的数量 。
#
#  
#
# 示例 1：
#
# 输入：arr = [3,0,1,1,9,7], a = 7, b = 2, c = 3
# 输出：4
# 解释：一共有 4 个好三元组：[(3,0,1), (3,0,1), (3,1,1), (0,1,1)] 。
#1.暴力解法，采用三重循环，枚举所有三元组，判断是否满足条件，时间复杂度O(n^3)
def count_good_tuples(arr, a, b, c):
    count = 0
    n = len(arr)

    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if (abs(arr[i] - arr[j]) <= a and
                    abs(arr[j] - arr[k]) <= b and
                    abs(arr[i] - arr[k]) <= c):
                    count += 1

    return count

# 示例
arr = [3, 0, 1, 1, 9, 7]
a = 7
b = 2
c = 3
result = count_good_tuples(arr, a, b, c)
print(result)  # 输出: 4
#2.优化解法，可以先进行排序，再进行循环。
def count_good_tuples(arr, a, b, c):
    count = 0
    n = len(arr)
    # 先对数组排序，这样可以提前停止不必要的循环
    arr.sort()
    for i in range(n - 2):
        # 从i+1开始遍历j
        j = i + 1
        while j < n - 1:
            # 如果 arr[i] - arr[j] > a，那么对于所有 k > j 的情况，arr[i] - arr[k] 也会大于 a，不需要继续检查
            if abs(arr[i] - arr[j]) > a:
                j += 1
                continue
            # 对于每个 arr[j]，找到满足条件的 arr[k] 的范围
            k = j + 1
            while k < n and abs(arr[j] - arr[k]) <= b and abs(arr[i] - arr[k]) <= c:
                count += 1
                k += 1
            j += 1
    return count

# 示例
arr = [3, 0, 1, 1, 9, 7]
a = 7
b = 2
c = 3
result = count_good_tuples(arr, a, b, c)
print(result)  # 输出: 4
