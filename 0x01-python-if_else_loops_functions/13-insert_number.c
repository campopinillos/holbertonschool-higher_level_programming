#include "lists.h"
/**
 * insert_node -  inserts a number into a sorted singly linked list
 * @head: pointer to head of list
 * @number: number
 *
 * Return: the address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *node = *head;

	new = malloc(sizeof(listint_t));
	if (!new)
		return (NULL);
	new->n = number;
	if (!*head)
	{
		new->next = NULL;
		*head = new;
		return (*head);
	}
	if (number < node->n)
		{
			new->next = *head;
			*head = new;
			return (*head);
		}
	while (node)
	{
		if (node->n < number && node->next->n >= number)
			break;
		node = node->next;
	}
	if (!node->next)
		new->next = NULL;
	else
		new->next = node->next;
	node->next = new;
	if (new == NULL)
	{
		free(new);
		return (NULL);
	}
	return (node);
}
