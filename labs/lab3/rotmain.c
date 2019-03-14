#include <stdio.h>
#include <stdlib.h>
#include "avlrot.c"

int qNode_add_to_tail(qNode **x, avlNode* node);
int enqueue (qNode **x, avlNode* node);
int dequeue (qNode **x, avlNode** node);
int printTreeInOrder(avlNode *root);
int printLevelOrder(avlNode *root);
int height(avlNode **root);
int isAVL(avlNode **root);
int add_bst(avlNode **root,int val);
int rotate(avlNode **root,unsigned int Left0_Right1);
int dblrotate(avlNode **root,unsigned int MajLMinR0_MajRMinL1);

int main(void) {
   avlNode *root=NULL;
   add_bst(&root,10);
   add_bst(&root,20);
   add_bst(&root,30);;
   add_bst(&root,40);
   add_bst(&root,50);
   add_bst(&root,25);
   printLevelOrder(root);
   printf("\n");
   printTreeInOrder(root);
   printf("\n");
   printf("%d\n",isAVL(&root));
   return 0;
}
