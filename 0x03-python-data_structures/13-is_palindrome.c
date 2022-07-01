#include "lists.h"
#include<string.h>

/**
  * is_palindrome - checks a list if its palindrome
  * @head: 1st node
  * Return: 0 if it is not a palindrome, 1 if it is a palindrome
  */

int is_palindrome(listint_t **head)
{
	if (head == NULL || *head == NULL)
		return (1);
	return (is_palind(head, *head));
}

/**
  * is_palind - checks if palindrome
  * @head: 1st node
  * @end: tail node
  * Return: 0 if it is not a palindrome, 1 if it is a palindrome
  */

int is_palind(listint_t **head, listint_t *end)
{
	if (end == NULL)
		return (1);
	if (is_palind(head, end->next) && (*head)->n == end->n)
	{
		*head = (*head)->next;
		return (1);
	}
	return (0);
}
