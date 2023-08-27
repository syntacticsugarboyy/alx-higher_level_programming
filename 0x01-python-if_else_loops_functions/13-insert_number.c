#include "lists.h"

/**
 * insert_node - inserts a node
 * @head: Pointer to head node
 * number: index of node to be inserted
 *
 * Return: address of the new_node
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *temp, *prev;
	listint_t *new_node;
	int count = 0;

	temp = prev = (*head);

	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
	{
		return (NULL);
	}

	new_node->n = number;
	new_node->next = (*head);

	if ((*head) == NULL)
	{
		(*head) =  new_node;
		return (new_node);
	}

	while (temp != NULL)
	{
		count++;
		if (temp->n < number)
		{
			if (count == 1)
			{
				(*head) = new_node;
			}
			else
			{
				prev->next = new_node;
			}
			new_node->next = temp;
			return (new_node);
		}
		prev = temp;
		temp = temp->next;
	}

	prev->next = new_node;
	new_node->next = NULL;
	return (new_node);
}
