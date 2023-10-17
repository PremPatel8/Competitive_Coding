class ListNode {
    int val;
    ListNode next;
    ListNode() {}
    ListNode(int val) { this.val = val; }
    ListNode(int val, ListNode next) { this.val = val; this.next = next; }
}

class merge_two_sorted_lists {
    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        if (list1 == null && list2 == null)  {
            return list1;
        } else if (list1 == null || list2 == null) {
            return list1 == null ? list2 : list1;
        }

        boolean flag = true;

        while (list1.next != null && list2.next != null) {
            if (list2.val > list1.val) {
                ListNode temp =  list1.next;
                list1.next = list2;
                list1 = temp;
                if (flag) {
                    flag = false;
                    ListNode head
                }

                } else {
                    ListNode temp = list2.next;
                    list2.next = list1;
                    list2 = temp;
                }
        }

        return head;
    }
}