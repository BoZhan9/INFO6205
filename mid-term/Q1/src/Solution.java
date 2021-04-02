public class Solution {
    public static void main(String[] args) {
        Solution s = new Solution();
        ListNode n1 = new ListNode(1);
        ListNode n2 = n1.next = new ListNode(2);
        ListNode n3 = n2.next = new ListNode(3);
        ListNode n4 = n3.next =  new ListNode(4);
        ListNode n5 = new ListNode(5);
        ListNode n6 = n5.next = new ListNode(6);
        n6.next = n1;
        System.out.println(s.areConverging(n1, n6));

    }
    public boolean areConverging(ListNode n1, ListNode n2) {
        if (n1 == null || n2 == null) {
            return false;
        }
        ListNode temp1 = n1;

        while (temp1 != null) {
            ListNode temp2 = n2;
            while (temp2 != null) {
                if (temp1.next == temp2 || temp2.next == temp1 ) {
                    return true;
                } else {
                    temp2 = temp2.next;
                }
            }
            temp1 = temp1.next;
        }
        return false;
    }
}

// Time(n^2) n1.length * n2.length
// Space(n) n1.length + n2.length
