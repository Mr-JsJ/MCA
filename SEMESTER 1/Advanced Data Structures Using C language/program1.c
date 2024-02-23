//Merge two sorted arrays and store in a third array
#include<stdio.h>
int main()
{
 int s3,j,s1,s2,i,k;
 printf("Enter the size of two array:");
 scanf("%d",&s1);
 scanf("%d",&s2);
 int a1[s1],a2[s2];
 printf("Enter the valuesof 1st array");
 for(i=0;i<s1;i++)
  {
  scanf("%d",&a1[i]);
  } 
printf("Enter the valuesof 2nd array");
 for(j=0;j<s2;j++)
  {
  scanf("%d",&a2[j]);
  }
  s3=s1+s2;
  int a3[s3];  
  i=0;j=0;k=0;
    while((i<s1)&&(j<s2))
    {
    if(a1[i]<a2[j])
      {
       a3[k]=a1[i];
     i++;
      } 
    else
      {
       a3[k]=a2[j];   
      j++;
      }  
    k++;   
    }
  while(i<s1) 
    {
   a3[k++]=a1[i++];
    }
  while(j<s2)
   {
   a3[k++]=a2[j++];
   }
printf("Merged array=");
 for(i=0;i<s3;i++)
  {
  printf("%d",a3[i]);
  } 

}
