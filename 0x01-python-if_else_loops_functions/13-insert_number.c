#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - Inserts a number into a sorted singly linked list.
 *
 * @head: Linked list.
 * @number: New value.
 *
 * Return: The address of the new node, or NULL if it failed.
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *list, *new_node, *prev_node;

	new_node = malloc(sizeof(listint_t));

	if (!new_node)
		return (NULL);

	list = *head;
	prev_node = NULL;
	new_node->n = number;

	while (list && list->n < number)
	{
		prev_node = list;
		list = list->next;
	}

	new_node->next = list;

	if (prev_node)
		prev_node->next = new_node;

	else
		*head = new_node;

	return (list);
}
