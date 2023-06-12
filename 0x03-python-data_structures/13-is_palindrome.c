#include <stdlib.h>
#include "lists.h"

/**
 * is_palindrome - checks if a linked list is a palindrome
 * @head: double pointer to the head of the linked list
 *
 * Return: 1 if the linked list is a palindrome, 0 otherwise
 */

int is_palindrome(listint_t **head)
{
	listint_t *prev = NULL;
	listint_t *current = *head;
	int len = 0;
	int mid = 0;

	listint_t *starter = *head;

	while (*head != NULL)
	{
		prev = current;
		current = current->next;
		current = prev;
		len++;
	}
	mid = len / 2;
	while (mid  > 0 && starter != NULL)
	{
		if (starter->n == current->n)
		{
			starter = starter->next;
			current = current->prev;
			mid--;
		}
		else
		{
			return (0);
		}
	}
	return (1);

}
