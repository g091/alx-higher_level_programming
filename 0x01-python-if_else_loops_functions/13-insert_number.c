#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include "lists.h"

listint_t *create_node(int n);

/**
 * insert_node - inserts a no. in a sorted linked list
 * @head: 1st node
 * @number: inserted no.
 * Return: address of the new node,or NULL if it fails
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *initial = NULL, *new_node = NULL;

	if (!head)
		return (NULL);
	else if (!(*head))
	{
		new_node = create_node(number);
		*head = new_node;
		return (new_node);
	}
	initial = *head;
	while (initial)
	{
		if (initial->n >= number)
		{
			new_node = create_node(number);
			new_node->next = initial;
			*head = new_node;
			return (new_node);
		}
		else if (initial->n <= number)
		{
			if (!initial->next || initial->next->n >= number)
			{
				new_node = create_node(number);
				new_node->next = initial->next;
				initial->next = new_node;
				return (initial->next);
			}
		}
		initial = initial->next;
	}
	return (NULL);
}

/**
 * create_node - creates a new node for the linked list
 * @n: data to be inserted
 * Return: pointer to newly allocated node
 */

listint_t *create_node(int n)
{
	listint_t *r = NULL;

	r = malloc(sizeof(listint_t));
	if (!r)
		return (NULL);
	r->next = NULL;
	r->n = n;
	return (r);
}
