#ifndef LISTS_H
#define LISTS_H
#include <stdlib.h>
/**
 * struct listint_s - Singly Linked List Node
 * @data: integer value stored in the node
 * @next_node: Pointer to the next node in the list
 * Summary: Represents a node of a singly linked list
 */
typedef struct listint_s
{
int data;
struct listint_s *next_node;
} listint_t;
int check_cycle(listint_t *list);
void free_listint(listint_t *head);
size_t print_listint(const listint_t *h);
listint_t *add_nodeint(listint_t **head, const int data);
#endif
