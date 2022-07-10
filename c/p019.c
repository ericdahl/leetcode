/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */

static int get_length(const struct ListNode* head) {
    int length = 0;
    for (struct ListNode* c = head; c; c = c->next, ++length);

    return length;
}

struct ListNode* removeNthFromEnd(struct ListNode* head, int n){

    const int before_index = get_length(head) - n - 1;

    if (before_index < 0) {
        if (head) {
            return head->next;
        }
        return NULL;
    }


    // iterate to node before target
    struct ListNode* before_node = head;
    for (int i = 0; i < before_index; before_node = before_node->next, ++i);

    before_node->next = before_node->next->next;

    return head;
}