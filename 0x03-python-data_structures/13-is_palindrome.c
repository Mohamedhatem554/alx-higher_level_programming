#include "lists.h"
#include <stdio.h>

/**
 * is_palindrome - function
 * @head: ptr to the beginning of the list
 * Return: 1 if success
*/
int is_palindrome(listint_t **head)
{
	if (head == NULL || *head == NULL)
	return (1);
	return (_check(head, *head));
}



/**
 * _check - function
 * @head: header
 * @l: last
 * Return: 1 if success
*/
int _check(listint_t **head, listint_t *l)
{
	if (l == NULL)
	return (1);
	if (_check(head, l->next) && (*head)->n == l->n)
	{
		*head = (*head)->next;
		return (1);
	}
	return (0);
}
