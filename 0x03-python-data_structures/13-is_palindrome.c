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
