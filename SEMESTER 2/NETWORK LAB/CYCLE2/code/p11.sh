find_month() {
    case $1 in
        1) echo "January";;
        2) echo "February";;
        3) echo "March";;
        4) echo "April";;
        5) echo "May";;
        6) echo "June";;
        7) echo "July";;
        8) echo "August";;
        9) echo "September";;
        10) echo "October";;
        11) echo "November";;
        12) echo "December";;
        *) echo "Invalid month number";;
    esac
}

while true
do
    echo "Menu:"
    echo "1. Find month for a number"
    echo "2. Exit"
    echo -n "Enter your choice: "
    read choice

    case $choice in
        1)  echo -n "Enter the month number (1-12): "
            read month_num
            find_month $month_num
            ;;
        2)  echo "Exiting..."
            exit 0
            ;;
        *)  echo "Invalid choice. Please enter 1 or 2."
            ;;
    esac
done
