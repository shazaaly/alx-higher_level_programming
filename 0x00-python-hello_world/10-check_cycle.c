#include "lists.h"
#include <stdlib.h>

int check_cycle(listint_t *list)
{
	listint_t *prev = NULL;
	listint_t *curr = NULL;

	if (list == NULL)
	{
		return (0);
	}


	prev = list;
	curr = list;

	while (curr != NULL && prev != NULL)
	{
		curr = curr->next;
		if (curr == prev)
		{
			return (1);
		}
		prev = prev->next;
		curr = curr->next;

	}

	return (0);
}
