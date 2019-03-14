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
int printLevelOrder(bstNode *root);
bstNode **createQueue(int *front, int *rear);
void enQueue(bstNode **queue, int *rear, bstNode *new_node);
bstNode *deQueue(bstNode **queue, int *front);


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

int printLevelOrder(bstNode *root) {
   int front = 0;
   int rear = 0;
   bstNode **queue = createQueue(&front, &rear);
   bstNode *temp_node = root;
   while (temp_node != NULL) { 
      printf("%d ", temp_node->val); 
      if (temp_node->l != NULL) 
         enQueue(queue, &rear, temp_node->l); 
      if (temp_node->r != NULL) 
         enQueue(queue, &rear, temp_node->r); 
      temp_node = deQueue(queue, &front); 
   }
   printf("\n");
   return 0;
}

bstNode **createQueue(int *front, int *rear) {
   bstNode **queue = (bstNode **)malloc(sizeof(bstNode *)*500);
   *front = 0;
   *rear = 0;
   return queue;
}

void enQueue(bstNode **queue, int *rear, bstNode *new_node) { 
   queue[*rear] = new_node; 
   (*rear)++; 
} 
  
bstNode *deQueue(bstNode **queue, int *front) { 
   (*front)++; 
   return queue[*front - 1]; 
} 

int main(void) {
   /* Let us create the following BST 
        5 
      /   \ 
     3     7 
    / \   / \ 
   1   4 6   8 

   OUTPUT:
   1
   3
   4
   5
   6
   7
   8
   5 3 7 1 4 6 8 */

   bstNode *root=NULL;
   add_bst(&root,5);
   add_bst(&root,3);
   add_bst(&root,1);
   add_bst(&root,4);
   add_bst(&root,7);
   add_bst(&root,6);
   add_bst(&root,8);
   printTreeInOrder(root);
   printLevelOrder(root);
   return 0;
}