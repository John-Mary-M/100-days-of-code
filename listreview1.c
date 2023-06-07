#include "main.h"
/**
 * main - initializes a list and calls its print function.
 *
 * Return: 0 on success.
 */

int main(){
        struct node *head = NULL;
        struct node *secound = NULL;
        struct node *third = NULL;

        head = (struct node *)malloc(sizeof(struct node));
        secound = (struct node *)malloc(sizeof(struct node));
        third = (struct node *)malloc(sizeof(struct node));

        head->data = 1;
        head->next = secound;
        secound->data = 2;
        secound->next = third;
        third->data = 3;
        third->next = NULL;

        print_list(head);
        return(0);
}
