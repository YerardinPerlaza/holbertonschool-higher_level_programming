#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
/**
 * add_nodeint - check the code for Holberton School students.
 *@head: double pointer
 *@n: const int
 * Return: Always 0.
 */
listint_t *add_nodeint(listint_t **head, const int n)
{
	listint_t *new;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	new->n = n;
	new->next = *head;

	*head = new;

	return (new);
}
/**
 * is_palindrome - checks if palindrome
 * @head: head of node
 * Return: 0 if not, 1 if is
 */
int is_palindrome(listint_t **head)
{
	unsigned int len = 1, mid = 0, i = 0;
	listint_t *temp, *start_rev, *middle, *current;

	if (head == NULL || *head == NULL)
		return (1);
	temp = *head;
	while (temp)
	{
		temp = temp->next;
		len++;
	}
	mid = (len / 2);
	middle = *head;
	while (middle)
	{
		if (i == mid +1)
			break;
		else
		{
			i++;
			middle = middle->next;
		}
	}
	printf("%d", middle->n);
	start_rev = NULL;
	current = *head;
	for (i = 0; i < mid; i++)
	{
		start_rev = add_nodeint(head, current->n);
		temp = current->next;
	}
	printf("%d", middle->n);
	while (middle)
	{
		if (start_rev->n == middle->n)
		{
			start_rev = start_rev->next;
			middle = middle->next;
		}
		else
			return (0);
	}
	return (1);
}
