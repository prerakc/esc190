#include <stdio.h>
#include <stdlib.h>
#include "heap.c"

int main (void) {
   HeapType ph;
   int *output = NULL;
   int size = 0;
   int i = 0;
   initHeap(&ph,10);
   addHeap(&ph,5);
   addHeap(&ph,3);
   addHeap(&ph,2);
   addHeap(&ph,10);
   addHeap(&ph,1);
   inorder(&ph,&output,&size);
   printf("IN ORDER\n");
   for (i = 0; i < size; i++) {
      printf("\t%d\n",output[i]);
   }
   preorder(&ph,&output,&size);  
   printf("PRE ORDER\n");
   for (i = 0; i < size; i++) {
      printf("\t%d\n",output[i]);
   }
   postorder(&ph,&output,&size);
   printf("POST ORDER\n");
   for (i = 0; i < size; i++) {
      printf("\t%d\n",output[i]);
   }
   printf("Does 20 exist in heap? %d\n", findHeap(&ph, 20));
   printf("Does 10 exist in heap? %d\n", findHeap(&ph, 10));
   delHeap(&ph,&i);
   printf("Removed root %d, new root is %d\n",i,ph.store[0]);
   inorder(&ph,&output,&size);
   printf("IN ORDER\n");
   for (i = 0; i < size; i++) {
      printf("\t%d\n",output[i]);
   }
   preorder(&ph,&output,&size);  
   printf("PRE ORDER\n");
   for (i = 0; i < size; i++) {
      printf("\t%d\n",output[i]);
   }
   postorder(&ph,&output,&size);
   printf("POST ORDER\n");
   for (i = 0; i < size; i++) {
      printf("\t%d\n",output[i]);
   }
   return 0;
}
