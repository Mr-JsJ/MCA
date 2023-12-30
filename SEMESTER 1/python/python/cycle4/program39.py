def fibonacci(first,second,limit):
    if limit>=1: 
     print(first)
     nth=second+first
     first=second
     second=nth
     limit=limit-1
     fibonacci(first,second,limit)
limit=int(input("ENTER THE LIMIT::"))
fibonacci(0,1,limit) 
