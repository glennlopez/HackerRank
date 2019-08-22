#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>


int main()
{
	
    //get stdio
    int a, b;
    float x, y;
    
    scanf("%d %d", &a, &b);
    scanf("%f %f", &x, &y);
    
    
    //calculate
    printf("%d %d\n", a+b, a-b);
    printf("%0.1f %0.1f\n", x+y, x-y);
    
    
    return 0;
}





