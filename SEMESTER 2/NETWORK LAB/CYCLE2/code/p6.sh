#!/bin/bash


echo "Enter the filename :"
read filename

if [ -e "$filename" ]; then
    echo "$filename exists."
else
    echo "$filename does not exist."
fi

