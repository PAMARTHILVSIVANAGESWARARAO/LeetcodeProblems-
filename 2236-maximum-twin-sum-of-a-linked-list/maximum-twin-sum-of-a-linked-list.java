/**
 * Definition for singly-linked list.
 * public class ListNode {
 * int val;
 * ListNode next;
 * ListNode() {}
 * ListNode(int val) { this.val = val; }
 * ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public int pairSum(ListNode head) {
        if (head == null) return 0;
        
        // Step 1: Find the middle of the linked list
        ListNode slow = head;
        ListNode fast = head;
        
        while (fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;
        }
        
        // Step 2: Reverse the second half of the list starting from 'slow'
        ListNode prev = null;
        ListNode curr = slow;
        
        while (curr != null) {
            ListNode nextNode = curr.next;
            curr.next = prev;
            prev = curr;
            curr = nextNode;
        }
        
        // Step 3: Iterate from both ends to find the maximum twin sum
        ListNode firstHalf = head;
        ListNode secondHalf = prev; // 'prev' is now the head of the reversed second half
        int maxVal = 0;
        
        while (secondHalf != null) {
            maxVal = Math.max(maxVal, firstHalf.val + secondHalf.val);
            firstHalf = firstHalf.next;
            secondHalf = secondHalf.next;
        }
        
        return maxVal;
    }
}