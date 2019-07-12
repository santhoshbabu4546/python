#include<stdio.h>
int main()
{
    int j,b,fact=1;

    scanf("%d",&b);
    if(b<=20)
    {
    for(j=1;j<=b;j++)
    {
        fact=fact*j;

    }
    printf("%d",fact);

}
}
