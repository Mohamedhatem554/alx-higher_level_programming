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
	return (check(head, *head));
}

/**
 * check - function
 * @head: header
 * @l: last
 * Return: 1 if success
*/
int check(listint_t **head, listint_t *l)
{
	if (l == NULL)
	return (1);
	if (check(head, l->next) != NULL && (*head)->n == l->n)
	{
		*head = (*head)->next;
		return (1);
	}
}
