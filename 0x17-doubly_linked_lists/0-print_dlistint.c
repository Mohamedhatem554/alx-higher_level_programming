#include "lists.h"

/**
 * print_dlistint - print node elements
 * @h: header node
 * Return: number of nodes
*/
size_t print_dlistint(const dlistint_t *h)
{
	const dlistint_t *ptr;
	size_t num = 0;

	ptr = h;
	while (ptr)
	{
		printf("%d\n", ptr->n);
		ptr = ptr->next;
		num++;
	}
	return (num);
}
