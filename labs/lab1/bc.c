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

int main(void) {
   char value = 'a';
   char popped = 'a';
   int rvalue=0;
   int n = 0;
   int elem = 0;
   int pass = 1;
   llnode *input_list=NULL;

   while (scanf("%c",&value) != EOF) {
      elem = elem + 1;

      if ((value == '{') || (value == '[') || (value == '(')) {
         push(&input_list,value);
         n = n + 1;
      }

      if ((value == '}') || (value == ']') || (value == ')')) {
         if (n == 0) {
            pass = 0;
            printf("stack is empty but closing brackets remain\n");
            break;
         }

         pop(&input_list,&popped);
         n = n - 1;
         
         if ((popped == '{') && (value == '}')) {
            continue;
         } else if ((popped == '[') && (value == ']')) {
            continue;
         } else if ((popped == '(') && (value == ')')) {
            continue;
         } else {
            pass = 0;
            printf("brackets dont match : popped %c does not match inputed %c\n",popped, value);
            break;
         }
      }
   }

   if (n != 0) {
      elem = elem - 1;
      printf("FAIL %d\n", elem);
   } else if (pass == 0) {
      printf("FAIL %d\n", elem);
   } else {
      printf("PASS\n");
   }

   return 0;
}
