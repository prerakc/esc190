#include <stdio.h>
#include <stdlib.h>

struct bstNode {
   int val;
   struct bstNode *l;
   struct bstNode *r;
};
typedef struct bstNode bstNode;

int add_bst(bstNode **root,int val);
int printTreeInOrder(bstNode *root);

int add_bst(bstNode **root,int val) {
   if (root == NULL) { return -1; }
   if (*root == NULL) {
      (*root) = (bstNode *)malloc(sizeof(bstNode));
      (*root)->val = val;
      (*root)->l = NULL;
      (*root)->r = NULL;
   } else {
      if (val < (*root)->val) {
      	add_bst(&((*root)->l), val);
      } else if (val > (*root)->val) {
      	add_bst(&((*root)->r), val);
      }
   }
   return 0;
}

int printTreeInOrder(bstNode *root) {
   if (root == NULL) { return -1; }
   printTreeInOrder(root->l);
   printf("%d\n", root->val);
   printTreeInOrder(root->r);
   return 0;
}

int main(void)
{
   bstNode *root=NULL;
   int value=0;
   while (scanf("%d",&value) != EOF) {
      add_bst(&root,value);
   }
   printTreeInOrder(root);
   return 0;
}