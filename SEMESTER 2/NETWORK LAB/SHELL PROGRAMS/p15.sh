#!/bin/bash

decimal_to_binary() {
    local decimal=$1
    local binary=""

    while [ $decimal -gt 0 ]
    do
        remainder=$((decimal % 2))
        binary="$remainder$binary"
        decimal=$((decimal / 2))
    done

    echo $binary
}


echo "Enter a decimal number:"
read decimal

binary=$(decimal_to_binary $decimal)
echo "Binary representation of $decimal is: $binary"

