#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() 
{
    
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */ 
    
    // char
    char c;
    scanf("%c", &c);
    printf("%c\n", c);
    
    // string 
    char s[150];
    scanf("%s", s);
    printf("%s\n", s);
    
    // sentense
    char sen[500];
    scanf("\n"); 
    scanf("%[^\n]%*c", sen);
    printf("%s", sen);
    
    return 0;
}