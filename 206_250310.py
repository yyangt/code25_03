#反转链表
class Solution:
  ListNode* reverseList(ListNode* head) {
      # ListNode* pre=nullptr,*cur=head;
      # while(cur!=nullptr){
      #   ListNode* a=cur->next;
      #   cur->next=pre;
      #   pre=cur;
      #   cur=a;
      # }
      # return pre;
      if(head==NULL||head->next==NULL){
        return head;
      }
      ListNode* ret=reverseList(head->next);
      head->next->next=head;
      head->next=NULL;
      return ret;
      
  }
