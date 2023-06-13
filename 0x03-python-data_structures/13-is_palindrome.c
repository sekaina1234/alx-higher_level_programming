#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to pointer to the head of the linked list
 * Return: 1 if the linked list is a palindrome, 0 otherwise
 */
int is_palindrome(listint_t **head)
{
listint_t *slow = *head;
listint_t *fast = *head;
listint_t *prev = NULL;
listint_t *temp;

if (*head == NULL || (*head)->next == NULL)
return (1);

/* Find the middle node using slow and fast pointers */
while (fast != NULL && fast->next != NULL)
{
fast = fast->next->next;
prev = slow;
slow = slow->next;
}

/* Reverse the second half of the list */
prev->next = NULL;
while (slow != NULL)
{
temp = slow->next;
slow->next = prev;
prev = slow;
slow = temp;
}


slow = prev;
fast = *head;
while (slow != NULL)
{
if (slow->n != fast->n)
return (0);
slow = slow->next;
fast = fast->next;
}

return (1);
}
