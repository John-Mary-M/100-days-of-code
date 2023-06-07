#ifndef __main_h__
#define __main_h__

#include <stdio.h>
#include <stdlib.h>

struct node{
        int data;
        struct node *next;
};

void print_list(struct node *head);

#endif /* MAIN_H */
