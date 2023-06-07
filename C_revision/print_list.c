#include "main.h"

/**
 * print_list - prints list
 * @head - struct *node to first element of the list
 * Return: void.
 */

void print_list(struct node *head){
        struct node *current = head;
        while (current != NULL){
                printf("%d", current->data);
                current = (struct node *)current->next;
        }
        printf("\n");
}
