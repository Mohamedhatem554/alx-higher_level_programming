#include "lists.h"

/**
 * check_cycle - check if the single linked list have a cycle or not
 * @list: node
 * Return: 1 if success
*/
int check_cycle(listint_t *list)
{
	listint_t *ptr, *tmp;

	if (list == NULL, list->next == NULL)
	return (0);

	ptr = list;
	tmp = ptr->next;

	while (ptr != NULL && tmp->next != NULL, tmp->next->next != NULL)
	{
		if (ptr == tmp)
		return (1);
		ptr = ptr->next;
		tmp = tmp->next->next;
	}
	return (0);
}
