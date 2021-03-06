#include <stdio.h>
#include <stdlib.h>
#include "sort.h"

int a[SIZE];
int ref[SIZE];

int nondet_int();

int main () {
  int i, v, prev;
  int s = nondet_int();
  __CPROVER_assume((s > 0) && (s <=SIZE));
  for (i = 0; i < s; i++) {
    v = nondet_int();
    __CPROVER_assume((v >= 0) && (v <= MAX));
    printf ("LOG: ref[%d] = %d\n", i, v);
    ref[i] = v;
    a[i] = v;
  }
  sort(a, s);
  prev = a[0];
  printf ("LOG: checking %d\n", v);
  for (i = 0; i < s; i++) {
    printf ("LOG: a[%d] = %d\n", i, a[i]);
    assert (a[i] >= prev);
    prev = a[i];
  }
}
