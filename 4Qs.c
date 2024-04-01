#include <stdio.h>
#include <math.h>
int main()
{
    int a;
    int b;
    int c;
    int res=1;
    
    scanf("%d",&a);
    scanf("%d",&b);
    scanf("%d",&c);
    
    for(int i=0;i<=b;i++)
    {
        res=res*a;  
    }
    res=res%c;
    printf("%d",res);
    return 0;
}
