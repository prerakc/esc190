#include <stdio.h>
#include <stdlib.h>

typedef struct {
   int *store;
   unsigned int size;
   unsigned int end;
} HeapType;

int initHeap (HeapType *pHeap,int size) {
   if (pHeap == NULL) {
      return -1;
   }
   pHeap->store = (int *)malloc(sizeof(int)*size);
   pHeap->size = size;
   pHeap->end = 0;
   return 0;
}

int inorder (HeapType *pHeap, int **output, int *o_size) {
   *o_size = 0;
   *output = (int *)malloc(sizeof(int)*(pHeap->size));
   recIn(pHeap, output, o_size, 0);
   return 0;
}

int recIn (HeapType *pHeap, int **output, int *o_size, int indx) {
   if (indx >= pHeap->size) {
      return 0;
   }
   recIn(pHeap, output, o_size, 2*indx + 1);
   if (pHeap->store[indx] != 0) {
      (*output)[*o_size] = (pHeap->store)[indx];
      *o_size = *o_size + 1;
   recIn(pHeap, output, o_size, 2*indx + 2);
   }
   return 0;
}

int preorder (HeapType *pHeap, int **output, int *o_size) {
   *o_size = 0;
   *output = (int *)malloc(sizeof(int)*(pHeap->size));
   recPre(pHeap, output, o_size, 0);
   return 0;
}

int recPre (HeapType *pHeap, int **output, int *o_size, int indx) {
   if (indx >= pHeap->size) {
      return 0;
   }
   if (pHeap->store[indx] != 0) {
      (*output)[*o_size] = (pHeap->store)[indx];
      *o_size = *o_size + 1;
   }
   recPre(pHeap, output, o_size, 2*indx + 1);
   recPre(pHeap, output, o_size, 2*indx + 2);
   return 0;
}


int postorder(HeapType *pHeap, int **output, int *o_size) {
   *o_size = 0;
   *output = (int *)malloc(sizeof(int)*(pHeap->size));
   recPos(pHeap, output, o_size, 0);
   return 0;
}

int recPos (HeapType *pHeap, int **output, int *o_size, int indx) {
   if (indx >= pHeap->size) {
      return 0;
   }
   recPos(pHeap, output, o_size, 2*indx + 1);
   recPos(pHeap, output, o_size, 2*indx + 2);
   if (pHeap->store[indx] != 0) {
   (*output)[*o_size] = (pHeap->store)[indx];
   *o_size = *o_size + 1;
   }
   return 0;
}

int addHeap(HeapType *pHeap, int key) {
   int i = 0;
   if (pHeap == NULL) {
      return -1;
   }
   pHeap->store[pHeap->end] = key;
   pHeap->end += 1;
   HeapUp(pHeap, pHeap->end - 1);
   return 0;
}

int HeapUp(HeapType *pHeap, int end) {
   int parent = -1;
   if ((pHeap == NULL) || (end == 0)) {
      return -1;
   }
   parent = (end - 1)/2;
   if (pHeap->store[parent] < pHeap->store[end]) {
      swap(pHeap,parent,end);
      if (parent != 0) {
         HeapUp(pHeap,parent);
      }
   }
   return 0;
}

int swap(HeapType *pHeap, int parent, int child) {
   if (pHeap == NULL) {
      return -1;
   } else {
      int tmp = pHeap->store[parent];
      pHeap->store[parent] = pHeap->store[child];
      pHeap->store[child] = tmp;
      return 0;
   }
}

int findHeap (HeapType *pHeap, int key) {
   int i = 0;
   int found = 0;
   if (pHeap == NULL) {
      return -1;
   }
   for (i = 0; i < pHeap->end; i++) {
      if (pHeap->store[i] == key) {
         found = 1;
         break;
      }
   }
   if (found == 1) {
      return 1;
   } else {
      return 0;
   }
}

int delHeap(HeapType *pHeap, int *key) {
   if (pHeap == NULL) {
      return -1;
   }
   (*key) = pHeap->store[0];
   pHeap->store[0] = pHeap->store[pHeap->end-1];
   pHeap->store[pHeap->end-1] = 0;
   pHeap->end -= 1;
   HeapDown(pHeap, 0);
   return 0;
}

int HeapDown(HeapType *pHeap, int parent) {
   int child = parent;
   if (pHeap == NULL) {
      return 0;
   }
   if (2*parent+1 < pHeap->end) {
      if (pHeap->store[parent] < pHeap->store[2*parent+1]) {
         child = 2*parent+1;
      }
   }
   if (2*parent+2 < pHeap->end) {
      if (pHeap->store[child] < pHeap->store[2*parent+2]) {
         child = 2*parent+2;
      }
   }
   if (child != parent) {
      swap(pHeap,parent,child);
      HeapDown(pHeap,child);
   }
   return 0;
}
