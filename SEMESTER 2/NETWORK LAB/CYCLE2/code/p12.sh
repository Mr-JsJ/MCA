factorial() {
    local num=$1
    local result=1
    
    while [ $num -gt 1 ]
    do
        result=$((result * num))
        num=$((num - 1))
    done
    
    echo $result
}

echo -n "Enter a number: "
read number

result=$(factorial $number)
echo "Factorial of $number is: $result"
