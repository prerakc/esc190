#include <stdio.h>
#include <stdlib.h>

struct llnode {
   char value;
   struct llnode *next;
};
typedef struct llnode llnode;

int llnode_add_to_tail(llnode **x,char value);
int llnode_print_from_head(llnode *x);
int llnode_print_from_tail(llnode *x);
int llnode_add_to_head(llnode **x, char value);
int push(llnode **x, char value);
int pop(llnode **x, char *return_value);

int llnode_add_to_tail(llnode **x,char value) {
   if (x==NULL) { return -1; }
   if (*x==NULL) {
      *x = (llnode *) malloc(sizeof(llnode));
      (*x)->value = value;
      (*x)->next = NULL;
      return 0;
   } else {
      return llnode_add_to_tail(&((*x)->next),value);
   }
}

int llnode_print_from_head(llnode *x) {
   if (x==NULL) { return 0; }
   else {
      printf("%c\n",x->value);
      return llnode_print_from_head(x->next);
   }
}

int llnode_print_from_tail(llnode *x) {
   if (x==NULL) { return 0; }
   else {
      if (x->next == NULL) {
         printf("%c\n",x->value);
	 return 0;
      } else {
         llnode_print_from_tail(x->next);
         printf("%c\n",x->value);
	 return 0;
      }
   }
}

int llnode_add_to_head(llnode **x, char value) {
   llnode *old_head;
   if (x == NULL) { return -1; };
   old_head = *x;
   *x = (llnode *)malloc(sizeof(llnode));
   (*x) -> value = value;
   (*x) -> next = old_head;
   return 0;
}

int push(llnode **x, char value) {
   return llnode_add_to_tail(x,value);
}

int pop(llnode **x, char *return_value) {
   llnode *toDelete = NULL;
   llnode *secondLastNode = NULL;

   if (x == NULL) { return -1; }
   if (*x == NULL) { return -1; }

   toDelete = *x;
   secondLastNode = *x;

   while (toDelete -> next != NULL) {
      secondLastNode = toDelete;
      toDelete = toDelete -> next;
   }
   
   if(toDelete == *x) {
      *x = NULL;
   } else {
      secondLastNode -> next = NULL;
   }

   *return_value = toDelete -> value;
   free(toDelete);

   return 0;
}
