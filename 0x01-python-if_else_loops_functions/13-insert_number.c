#include "lists.h"

/**
 * insert_node - insert new node
 * @head: head node
 * @number: number of node
 * Return: new node
*/
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *ptr = *head, *new;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
	{
	return (NULL);
	}
	new->n = number;

	if (ptr == NULL || ptr->n >= number)
	{
		new->next = ptr;
		*head = new;
		return (new);
	}

	while (ptr->next->n < number && ptr != NULL && ptr->next != NULL)
	{
		ptr = ptr->next;
	}
	new->next = ptr->next;
	ptr->next = new;
	return (new);
}
