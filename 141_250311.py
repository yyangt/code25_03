# 环形链表
class Solution :
    bool hasCycle(ListNode *head) {
        ListNode *a=head;
        ListNode *b=head;
        if(head==NULL){
            return false;
        }
        while(a!=NULL&&a->next!=NULL){
            a=a->next->next;
            b=b->next;
            if(a==b)
            {
                return true;
            }
        }
        return false;
    }
