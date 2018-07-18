#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() 
{
	
    char s[100];
    scanf("%[^\n]%*c", s);
  	
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */  
    printf("Hello, World!\n");
    for(int i = 0; s[i] != '\0'; i++){
        printf("%c", s[i]);
    }
    printf("\n");
    return 0;
}