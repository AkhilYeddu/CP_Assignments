#include <stdio.h>
int main()
{
    int x;
    scanf("%d",&x);
    for(int i=2;i<=x*x;i++)
    {
        int is_prime=1;
        
        for(int j=2;j<i;j++)
        {
            if(i%j==0)
            {
                is_prime=0;
                break;
                
            }
        }
        if(is_prime==1){
            printf("%d ",i);
            i=i+2;
            
        }
        
    }
    return 0;
}