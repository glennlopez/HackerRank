#include <stdio.h>

void update(int *a,int *b) {
    // Complete this function 
    int a_old = *a;
    int b_old = *b;
    *a = a_old + b_old;
    *b = abs(a_old - b_old);
}

int main() {
    int a, b;
    int *pa = &a, *pb = &b;
    
    scanf("%d %d", &a, &b);
    update(pa, pb);
    printf("%d\n%d", a, b);

    return 0;
}