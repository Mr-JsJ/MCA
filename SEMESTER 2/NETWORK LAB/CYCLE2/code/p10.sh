addition() {
    sum=$(($num1 + $num2))
    echo "Sum of $num1 and $num2 is: $sum"
}

subtraction() {
    difference=$(($num1 - $num2))
    echo "Difference between $num1 and $num2 is: $difference"
}

multiplication() {
    product=$(($num1 * $num2))
    echo "Product of $num1 and $num2 is: $product"
}

division() {
    if [ $num2 -eq 0 ]; then
        echo "Cannot divide by zero."
    else
        quotient=$(($num1 / $num2))
        echo "Quotient of $num1 divided by $num2 is: $quotient"
    fi
}

while true
do
    echo "Menu:"
    echo "1. Sum"
    echo "2. Difference"
    echo "3. Product"
    echo "4. Quotient"
    echo "5. Exit"
    echo -n "Enter your choice: "
    read choice

    case $choice in
        1)  echo "Enter two numbers:"
            read num1
            read num2
            addition
            ;;
        2)  echo "Enter two numbers:"
            read num1
            read num2
            subtraction
            ;;
        3)  echo "Enter two numbers:"
            read num1
            read num2
            multiplication
            ;;
        4)  echo "Enter two numbers:"
            read num1
            read num2
            division
            ;;
        5)  echo "Exiting..."
            exit 0
            ;;
        *)  echo "Invalid choice. Please enter a number between 1 and 5."
            ;;
    esac
done
