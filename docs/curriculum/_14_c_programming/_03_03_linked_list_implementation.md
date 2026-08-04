# Linked List Implementation

> **Course**: C Programming | **Module**: Advanced C | **Difficulty**: intermediate

---

```c
#include <stdio.h>
#include <stdlib.h>

typedef struct Node {
    int data;
    struct Node *next;
} Node;

/* Create a new node */
Node *create_node(int data) {
    Node *node = malloc(sizeof(Node));
    if (!node) exit(EXIT_FAILURE);
    node->data = data;
    node->next = NULL;
    return node;
}

/* Insert at head */
Node *insert_head(Node *head, int data) {
    Node *node = create_node(data);
    node->next = head;
    return node;
}

/* Insert at tail */
Node *insert_tail(Node *head, int data) {
    Node *node = create_node(data);
    if (!head) return node;
    Node *curr = head;
    while (curr->next) curr = curr->next;
    curr->next = node;
    return head;
}

/* Delete by value */
Node *delete_node(Node *head, int data) {
    if (!head) return NULL;
    if (head->data == data) {
        Node *tmp = head->next;
        free(head);
        return tmp;
    }
    Node *curr = head;
    while (curr->next && curr->next->data != data)
        curr = curr->next;
    if (curr->next) {
        Node *tmp = curr->next->next;
        free(curr->next);
        curr->next = tmp;
    }
    return head;
}

/* Print */
void print_list(Node *head) {
    for (Node *curr = head; curr; curr = curr->next)
        printf("%d -> ", curr->data);
    printf("NULL\n");
}

/* Free entire list */
void free_list(Node *head) {
    Node *curr = head;
    while (curr) {
        Node *tmp = curr->next;
        free(curr);
        curr = tmp;
    }
}

int main(void) {
    Node *list = NULL;
    list = insert_tail(list, 10);
    list = insert_tail(list, 20);
    list = insert_tail(list, 30);
    list = insert_head(list, 5);
    print_list(list);   /* 5 -> 10 -> 20 -> 30 -> NULL */
    list = delete_node(list, 20);
    print_list(list);   /* 5 -> 10 -> 30 -> NULL */
    free_list(list);
    return 0;
}
```

---

1. Add `reverse_list()` that reverses in-place
2. Detect a cycle using Floyd's two-pointer algorithm
3. Implement a doubly linked list with `prev` pointer

---
