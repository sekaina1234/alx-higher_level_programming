#include "lists.h"
/**
 * check_cycle - hecks if a singly linked list contains a cycle
 * @list: pointer to the first node of the linked list
 *
 * Return: 0 if the linked list has no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
listint_t *slow, *fast;
if (list == NULL)
return (0);
slow = list;
fast = list;
while (fast != NULL && fast->next != NULL)
{
slow = slow->next;
fast = fast->next->next;
if (slow == fast)
return (1);
}
return (0);
}
