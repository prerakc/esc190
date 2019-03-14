#include <stdio.h>
#include <stdlib.h>

struct avlNode {
   int balance; /* -1 Left, 0 balanced, +1 Right */
   int val;
   struct avlNode *l;
   struct avlNode *r;
};
typedef struct avlNode avlNode;

struct qNode {
   avlNode *pval;
   struct qNode *nxt;
};
typedef struct qNode qNode;

int qNode_add_to_tail(qNode **x, avlNode* node) {
   if (x == NULL) {
      return -1;
   }
   if (*x == NULL) {
      *x = (qNode *)malloc(sizeof(qNode));
      (*x)->pval = node;
      (*x)->nxt = NULL;
      return 0;
   } else {
      return qNode_add_to_tail(&((*x)->nxt), node);
   }
}

int enqueue (qNode **x, avlNode* node) {
   return qNode_add_to_tail(x,node);
}

int dequeue (qNode **x, avlNode** node) {
   if ((x == NULL) || (*x == NULL)) {
      return -1;
   } else {
      *node = (*x)->pval;
      *x = (*x)->nxt;
      return 0;
   }
}

int printTreeInOrder(avlNode *root) {
   if (root == NULL) { return -1; }
   printTreeInOrder(root->l);
   printf("%d\n", root->val);
   printTreeInOrder(root->r);
   return 0;
}

int printLevelOrder(avlNode *root) {
   if (root == NULL) {
      return -1;
   } else {
      avlNode *rval = NULL;
      qNode *queue = NULL;
      enqueue(&queue, root);
      while (queue != NULL) {
         dequeue(&queue,&rval);
         printf("%d ", rval->val);
         if ((rval->l) != NULL) {
            enqueue(&queue, rval->l);
         }
         if ((rval->r) != NULL) {
            enqueue(&queue, rval->r);
         }
      }
      printf("\n");
      return 0;
   }
}

int height(avlNode **root) {
   if (root == NULL) {
      return -1;
   } else {
      int lDepth = 0;
      int rDepth = 0;
      if ((*root)->l != NULL) {
         lDepth = height(&((*root)->l));
      }
      if ((*root)->r != NULL) {
         rDepth = height(&((*root)->r));
      }
      if (lDepth > rDepth) {
         return(lDepth+1);
      } else {
         return(rDepth+1);
      }
   }
}

int isAVL(avlNode **root) {
   int heightL = 0;
   int heightR = 0;
   if (((*root)->l) != NULL) {
      heightL = height(&((*root)->l));
   }
   if (((*root)->r) != NULL) {
      heightR = height(&((*root)->r));
   }
   if (abs(heightR-heightL) > 1)
      return -1;
   else
      return 0;
}

int add_bst(avlNode **root,int val) {
   if (root == NULL) {
      return -1;
   }
   if (*root == NULL) {
      (*root) = (avlNode *)malloc(sizeof(avlNode));
      (*root)->val = val;
      (*root)->l = NULL;
      (*root)->r = NULL;
      return 0;
   } else {
      if (val < (*root)->val) {
      	add_bst(&((*root)->l), val);
         if (isAVL(root) == 0) {
            return 0;
         }
         if (((*root)->l)->val > val) {
            rotate(root, 1);
         } else {
            dblrotate(root, 1);
         }
      } else {
         add_bst(&((*root)->r), val);
         if (isAVL(root) == 0) {
            return 0;
         }
         if (((*root)->r)->val < val) {
            rotate(root, 0);
         } else {
            dblrotate(root, 0);
         }
      }
   }
}

int rotate(avlNode **root,unsigned int Left0_Right1) {
   if ((root == NULL) || ((Left0_Right1 != 0) && (Left0_Right1 != 1)))
      return -1;
   else {
      avlNode *old_root = *root;
      avlNode *new_root = NULL;
      if (Left0_Right1 == 0) {
         new_root = (*root)->r;
         old_root->r = new_root->l;
         new_root->l = old_root;
      } else {
         new_root = (*root)->l;
         old_root->l = new_root->r;
         new_root->r = old_root;
      }
      *root = new_root;
      return 0;
   }
}

int dblrotate(avlNode **root,unsigned int MajLMinR0_MajRMinL1) {
   if ((root == NULL) || ((MajLMinR0_MajRMinL1 != 0) && (MajLMinR0_MajRMinL1 != 1)))
      return -1;
   else {
   	if (MajLMinR0_MajRMinL1 == 0){
   	   rotate(&((*root)->r),1);
   	   rotate(root,0);
   	} else {
		   rotate(&((*root)->l),0);
   	   rotate(root,1);
   	  }
      return 0;
   }
}