#include <stdlib.h>
#include "lists.h"

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
		if(starter->n == current->n)
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
