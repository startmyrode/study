# 给定一个链表的头节点  head ，返回链表开始入环的第一个节点。 如果链表无环，则返回 null。
#
# 如果链表中有某个节点，可以通过连续跟踪 next 指针再次到达，则链表中存在环。 为了表示给定链表中的环，评测系统内部使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。如果 pos 是 -1，则在该链表中没有环。注意：pos 不作为参数进行传递，仅仅是为了标识链表的实际情况。
#
# 不允许修改 链表。
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#设非环长度为a，环长度为b。两个未知数，我们要有两个方程，设两个指针，fast指针速度是slow指针速度的两倍，当相遇时，fast指针的路程为a+2nb,慢指针的路程为a+nb。我们要求相遇点，即a的长度。很简单的二元一次方程，慢指针*2-快指针。


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast, slow = head, head
        while True:
            # 如果链表无环，直接返回None
            if not (fast and fast.next):
                return None
            fast = fast.next.next
            slow = slow.next
            # 快慢指针相遇，说明有环
            if fast == slow:
                # 重新指向头节点，寻找环入口
                ptr = head
                while ptr != slow:
                    ptr = ptr.next
                    slow = slow.next
                return ptr
