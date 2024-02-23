//Singly Linked Stack - Push, Pop, Linear Search
#include<stdio.h>
#include<stdlib.h>
struct node
{
int data;
struct node *next; 
};
struct node *top=NULL;
 void push()
     {
 struct node *newnode;
newnode=malloc(sizeof(struct node));
int val;
    printf("Enter the value:\n");
    scanf("%d",&val);
    newnode->data=val;
    newnode->next=top;
    top=newnode;
    printf("%d has pushed",val);
}

void pop()
    {
if(top==NULL)
{
printf("STACK UNDERFLOW");
}
else
{
printf("%d has poped",top->data);
top=top->next;

}

}

void search()
    {
    struct node*temp=top;
  int val,i=1;
printf("ENTER THE VALUE");
scanf("%d",&val);
while(temp!=NULL)
{
if(temp->data==val)
{
printf("%d value has found in position:%d",temp->data,i);
}
else
{
printf("value not found");
}
i++;
temp=temp->next;
}
}


void traversal()
		{
		    struct node *temp=top;
		    while(temp!=NULL)
		    {
		        printf("%d---->",temp->data);
		        temp=temp->next;
		    }
		}

		    
int main()
{
int opt;
	while(opt!=5)
	{
		printf("\n\n1:PUSH\n");
		printf("2:POP\n");
		printf("3:SEARCH\n");
		printf("4:DISPLAY\n");
                printf("5:exit");		
                scanf("%d",&opt);
	    	switch(opt)
			{
				case 1:
					push();
					break;
				case 2:
				    pop();
					break;
				case 3:
				    search();
					break; 
                                case 4:
                                     traversal();
                                       break;
				case 5:
					printf("Exit");
					break;
				default :
				     printf("Invalid Input");	
}}}
