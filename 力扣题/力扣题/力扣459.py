# 给定一个非空的字符串s，检查是否可以通过由它的一个子串重复多次构成。
# 示例 1:
# 输入: s = "abab"
# 输出: true
# 解释: 可由子串 "ab" 重复两次构成。
# 示例 2:
#
# 输入: s = "aba"
# 输出: false
# 示例 3:
#
# 输入: s = "abcabcabcabc"
# 输出: true
# 解释: 可由子串 "abc" 重复四次构成。 (或子串 "abcabc" 重复两次构成。)
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        a = len(s)
        for i in range(1, a // 2 + 1):
            if a % i == 0:  # 检查当前长度是否能整除原字符串长度
                substring = s[:i]  # 获取子串
                if substring * (a // i) == s:  # 检查子串重复多次是否等于原字符串
                    return True
        return False  # 如果没有找到合适的子串，返回 False

#C语言版
#include <stdio.h>
#include <string.h>
#include <stdbool.h>

# bool repeatedSubstringPattern(char * s) {
#     int n = strlen(s);
#     for (int i = 1; i <= n / 2; i++) {
#         if (n % i == 0) {  // 检查当前长度是否能整除原字符串长度
#             bool match = true;
#             char * substring = s;  // 获取子串的起始位置
#             for (int j = i; j < n; j++) {
#                 if (s[j] != s[j % i]) {  // 检查子串重复多次是否等于原字符串
#                     match = false;
#                     break;
#                 }
#             }
#             if (match) {
#                 return true;
#             }
#         }
#     }
#     return false;
# }
#
# int main() {
#     char test1[] = "abab";
#     char test2[] = "aba";
#     char test3[] = "abcabcabcabc";
#
#     printf("Test 1: %s\n", repeatedSubstringPattern(test1) ? "true" : "false");
#     printf("Test 2: %s\n", repeatedSubstringPattern(test2) ? "true" : "false");
#     printf("Test 3: %s\n", repeatedSubstringPattern(test3) ? "true" : "false");
#
#     return 0;
# }
