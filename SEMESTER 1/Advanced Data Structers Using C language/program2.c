//Implementation of singly linked list-Insertion, Deletion
#include<stdio.h>
#include<stdlib.h>

struct node {
  int data;
  struct node *next;
};

struct node *head=NULL;
	
void insertbeg() 
	{ 
	struct node *newnode;
    newnode = malloc(sizeof(struct node));
	int val;
    printf("Enter the value:\n");
    scanf("%d",&val);
    newnode->data=val;
    newnode->next=head;
    head=newnode;
    }

void insertend()
    {
    struct node *newnode;
    newnode = malloc(sizeof(struct node));
    if(head==NULL)
    {
      insertbeg();
     }
   else
   {  
    int val;
    printf("Enter the value:\n");
    scanf("%d",&val);
    newnode->data=val;
    newnode->next=NULL;
    struct node *temp;
    temp=head;
    while(temp->next!=NULL)
    {
    temp=temp->next;    
    }
    temp->next=newnode;
     }
    }
	

	void insertpos()
	{
	int i; 
	struct node *newnode;
    newnode = malloc(sizeof(struct node));
    struct node *temp;
    temp->next=head;
	int val,pos;
    printf("Enter the value:\n");
    scanf("%d",&val);
    printf("Enter the position:\n");
    scanf("%d",&pos);
    newnode->data=val;
    if(pos==1)
    {
	newnode->data=val;
    newnode->next=head;
    head=newnode;
	}
    for(i=1;i<pos;i++)
    {
        if(temp->next!=NULL)
        {
            temp=temp->next;
        }
    }
    newnode->next=temp->next;
    temp->next=newnode;
}	


	void delfirst()
	{
    if(head==NULL)
    {printf("NO VALUES FOR DELETION");}
    else
    {
    head=head->next;
	}}
	


void dellast() 
        {
       if(head==NULL)
        {
         printf("NO VALUE FORE DELETION");  
           }
        else
          { 
        	struct node *temp=head;
         while(temp->next->next!=NULL)
		 {
          temp=temp->next;
          } 
         temp->next=NULL;	
         	} 	 }
	

	    
void delpos()
{
if(head==NULL)
{printf("NO VALUE FOR DELETION");}
else
  { 
    int pos,i;
     struct node *temp=head;
	     	printf("Enter the the position ");
	     	scanf("%d",&pos);
     	 if(pos==1)
        {
	    head=head->next;
	    }
       for(i=1;i<pos;i++)
        {
        if(temp->next!=NULL)
        {
        temp=temp->next;  	
        }  
        if(temp->next==NULL)
        {	
        break;
		}
	    }
	    if(i==pos)
	    {
	   temp->next=temp->next->next;
        }
        else 
	{
	printf("position not found");
	}
	}}

void traversal()
{
  struct node *temp;
   temp=head;
 while(temp!=NULL)
{
 printf("%d--->",temp->data);
 temp=temp->next;
}
}

int main()
{ 
 	int opt;
	while(opt!=8)
	{
		printf("\n1:Insert at the beginning of the list\n");
		printf("2:Insert at the end of the list\n");
		printf("3:Insert at the middle of the list\n");
		printf("4:Delete the first node of the list\n");
		printf("5:Delete the last node of the list\n");
	        printf("6:Delete the specifc node from the list\n");
		printf("7:Traversal the list\n");
		printf("8:Exit\n");
		scanf("%d",&opt);
	    	switch(opt)
			{
				case 1:
					insertbeg();
					break;
				case 2:
				    insertend();
					break;
				case 3:
				    insertpos();
					break;
				case 4:
					delfirst();
				 	break;
	     		        case 5:
				 	dellast();
					 break;
				case 6:
				    delpos();
			    	break;
				case 7:
					traversal();
					break;
				case 8:
					printf("Exit");
					break;
				default :
				     printf("Invalid Input");						 
				}
    } 
}
