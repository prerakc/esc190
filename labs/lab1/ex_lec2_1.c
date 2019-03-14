#include<stdio.h>
#include<stdlib.h>

typedef struct intlist {
   int *x;
   int end;
   int len;
} intlist;

int init(intlist *l,int len) {
   if (l==NULL) { return -1; }
   
   (l->x) = (int *)malloc(len * sizeof(int));

   if ((l->x) == NULL) { return -1; }

   l->end = -1;
   l->len=len;

   return 0;
}

int add_to_end(intlist *l, int val) {
   if (l == NULL) { return -1; }
   
   (l->x)[(l->end)+1] = val;
   (l->end) = (l->end) + 1;

   return 0;
}

int add_to_start(intlist *l, int val) {
   int i = 0;
   int *new = NULL;
  
   if (l == NULL) { return -1; }

   i = 0;
   new = (int *)malloc(sizeof(int)*(l->len));

   new[0] = val;

   for (i = 1; i < ((l->end) + 1); i++) {
      new[i] = (l->x)[i-1];
   }

   l->x = new;
   l->end = (l->end) + 1;

   return 0;
}

int insert_after(intlist *l, int insert_val, int val) {
   int i, j;
   int *new = NULL;

   if (l == NULL) { return -1; }

   i = 0;
   j = 0;
   new = (int *)malloc(sizeof(int)*(l->len));


   for (i = 0; i <= (l->end); i++) {
      new[i] = (l->x)[i];
      if ((l->x)[i] == insert_val) {
         new[i+1] = val;
         break;
      }
   }

   for (j = i + 1; j <= (l->end); j++) {
      new[j+1] = (l->x)[j];
   }

   l->x = new;
   l->end = (l->end) + 1;

   return 0;
}

int main (void) {
   intlist l;
   init(&l, 10);
   add_to_end(&l,1);
   add_to_end(&l,3);
   add_to_start(&l,0);
   //insert_after(&l,1,2);

   printf("%d %d %d\n",l.x[0],l.x[1],l.x[2]);
   printf("%d %d %d %d\n",l.x[0],l.x[1],l.x[2],l.x[3]);
   return 0;
}
