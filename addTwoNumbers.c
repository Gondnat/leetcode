/* You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list. */

/* You may assume the two numbers do not contain any leading zero, except the number 0 itself. */

/* Example */

/* Input: (2 -> 4 -> 3) + (5 -> 6 -> 4) */
/* Output: 7 -> 0 -> 8 */
/* Explanation: 342 + 465 = 807. */
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
// Definition for singly-linked list.
typedef struct ListNode {
    int val;
    struct ListNode *next;
} _listNode;

size_t length = sizeof(struct ListNode);
struct ListNode* addTwoNumbers(struct ListNode* l1, struct ListNode* l2) {
    int i = 0;

    struct ListNode *l = malloc(length);
    l->next = NULL;
    l->val = 0;
    struct ListNode *p = l;

    do {
        int val = (l1 ? l1->val : 0) + (l2 ? l2->val : 0) + i;
        i = val / 10;
        val = val % 10;
        p->next = malloc(length);
        p->next->val = val;
        p->next->next = NULL;
        p = p->next;
        l1 =  l1 ? l1->next : NULL;
        l2 = l2 ? l2->next : NULL;
    } while ( NULL != l1 || NULL != l2);
    
    if (0 != i) {
        p->next = malloc(length);
        p->next->val = 1;
        p->next->next = NULL;
        p = p->next;
    }
    return l->next;
}

int main() {

    struct ListNode *l1 = malloc(length);
    l1->val = 9;
    l1->next = malloc(length);
    l1->next->val = 9;
    l1->next->next = NULL;
    struct ListNode *l2 = malloc(length);
    l2->val = 1;
    l2->next = malloc(length);
    l2->next->val = 9;
    l2->next->next = NULL;

   struct ListNode *l = addTwoNumbers(l1, l2);
   while (l) {
       printf("%d\n", l->val);
       l = l->next;
   }
    
    return 0;
}
