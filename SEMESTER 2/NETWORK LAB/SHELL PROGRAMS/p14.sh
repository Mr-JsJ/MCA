#!/bin/bash

echo "Enter the value of n:"
read n

sum=0
counter=1

while [ $counter -le $n ]
do

    square=$((counter * counter))

    sum=$((sum + square))


    counter=$((counter + 1))
done

echo "The sum of squares of the first $n numbers is: $sum"

