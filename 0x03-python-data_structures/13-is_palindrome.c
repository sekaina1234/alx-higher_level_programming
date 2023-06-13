#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * reverse_list - reverses a linked list
 * @head: pointer to pointer to the head of the linked list
 */
void reverse_list(listint_t **head)
{
listint_t *prev = NULL;
listint_t *current = *head;
listint_t *next;

while (current != NULL)
{
next = current->next;
current->next = prev;
prev = current;
current = next;
}

*head = prev;
}

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

if (*head == NULL || (*head)->next == NULL)
return (1); /* Empty list or single node is a palindrome */

/* Find the middle node using slow and fast pointers */
while (fast != NULL && fast->next != NULL)
{
fast = fast->next->next;
prev = slow;
slow = slow->next;
}

prev->next = NULL; /* Split the list into two halves */

/* Reverse the second half of the list */
reverse_list(&slow);

/* Compare the first and second halves of the list */
while (*head != NULL && slow != NULL)
{
if ((*head)->n != slow->n)
return (0);

*head = (*head)->next;
slow = slow->next;
}

return (1);
}
