#include "lists.h"
#include <stdlib.h>
#include <stdio.h>
/**
* print_dlistint - prints all the elements of a doubly linked list
* @h: pointer to the head of the list
*
* Return: the number of nodes in the list
*/
size_t print_dlistint(const dlistint_t *h)
{
	size_t count = 0;
	const dlistint_t *current = NULL;

	if (h == NULL)
	{
		return (0);
	}
	current = h;
	while (current != NULL)
	{
		printf("%d\n", current->n);
		count++;
		current = current->next;
	}
	return (count);
}

