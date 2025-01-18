# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        arr = []

        t = head
        while t:
            arr.append(t.val)
            t = t.next
        
        low, high = 0, len(arr)

        maxx = 0
        n = len(arr)

        if(n == 2):
            return arr[0] + arr[1]
        for i in range(int((n)/2) ):
            summ = arr[i] + arr[n - i - 1]
            print(summ, arr[i], arr[n - i - 1])
            maxx = max(summ, maxx)

        return maxx
            


        