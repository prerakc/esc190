#include <stdio.h>
#include <stdlib.h>

struct llnode {
   int value;
   struct llnode *next;
};
typedef struct llnode llnode;

int llnode_add_to_tail(llnode **x,int value);
int llnode_print_from_head(llnode *x);
int llnode_print_from_tail(llnode *x);

int llnode_add_to_tail(llnode **x,int value) {
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
      printf("%d\n",x->value);
      return llnode_print_from_head(x->next);
   }
}

int llnode_print_from_tail(llnode *x) {
   if (x==NULL) { return 0; }
   else {
      if (x->next == NULL) {
         printf("%d\n",x->value);
	 return 0;
      } else {
         llnode_print_from_tail(x->next);
         printf("%d\n",x->value);
	 return 0;
      }
   }
}

int main(void) {
   int n=0;
   int value=0;
   int rvalue=0;
   llnode *input_list=NULL;

   while (scanf("%d",&value) != EOF) {
      n=n+1;
      llnode_add_to_tail(&input_list,value);
   }
   printf("INFO: you entered %d items\n",n);
   rvalue=llnode_print_from_tail(input_list);
   if ( !(rvalue==0) ) { printf("ERR: llnode_print returned an error\n"); }

   return 0;
}
