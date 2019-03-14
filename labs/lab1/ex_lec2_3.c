typedef struct tree {
   int val;
   /* you obain multiple branches by mallocing as an array of tree structs */
   struct tree *next;
} tree;
