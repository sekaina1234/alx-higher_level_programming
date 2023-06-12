#include "lists.h"
#include <stdio.h>

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: double pointer to the head of the linked list
 * Return: 1 if the linked list is a palindrome, 0 otherwise
 */
int is_palindrome(listint_t **head)
{
	listint_t *current = *head;
int values[1000]; /* 
int count = 0, i;
while (current != NULL)
{
values[count] = current->n;
current = current->next;
count++;
}
for (i = 0; i < count / 2; i++)
{
if (values[i] != values[count - i - 1])
return 0;
}
return 1;
}
