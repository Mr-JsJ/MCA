#!/bin/bash

fibonacci() {
    local limit=$1
    local a=0
    local b=1
    local temp

    echo "Fibonacci sequence up to $limit:"
    echo -n "$a $b "

    while [ $b -le $limit ]
    do
        temp=$((a + b))
        if [ $temp -le $limit ]; then
            echo -n "$temp "
        else
            break
        fi
        a=$b
        b=$temp
    done
    echo
}

echo -n "Enter the limit (N): "
read N

fibonacci $N

