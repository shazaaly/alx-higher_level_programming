#include <stdlib.h>
#include "lists.h"
/**
 * is_palindrome - checks if a singly linked list is a palindrome
 *
 * @head: double pointer to the head of the linked list
 *
 * Return: 1 if linked list is a palindrome, 0 otherwise
 */
int is_palindrome(listint_t **head)
{
	listint_t *current = *head;
	int arr[1024];
	int i = 0;
	int j = 0;

	if (*head == NULL)
	{
		return (0);
	}
	while (current != NULL)
	{
		arr[i++] = current->n;
		current = current->next;
	}

	for (j = 0; j < i / 2; j++)
	{
		if (arr[j] != arr[i - 1 - j])
		{
			return (0);
		}

	}
	return (1);

}

