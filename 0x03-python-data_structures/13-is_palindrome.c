#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to pointer to the head of the linked list
 * Return: 1 if the linked list is a palindrome, 0 otherwise
 */
int count = 0, start = 0, end;

int is_palindrome(listint_t **head)
{
listint_t *current = *head;
int values[1000];
int count = 0;
int start = 0;
int end;


if (*head == NULL || (*head)->next == NULL)
return (1);

while (current != NULL)
{
values[count] = current->n;
current = current->next;
count++;
}

end = count - 1;

while (start < end)
{
if (values[start] != values[end])
return (0);

start++;
end--;
}

return (1);
}
