<?php
$host = "localhost";
$username = "root";
$password = "";
$database = "book";

$conn = new mysqli($host, $username, $password, $database);

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $book_no = $_POST["book_no"];
    $title = $_POST["title"];
    $edition = $_POST["edition"];
    $publisher = $_POST["publisher"];

    $sql = "INSERT INTO `book_details` (book_no, title, edition, publisher) VALUES ('$book_no', '$title', '$edition', '$publisher')";

    if ($conn->query($sql) === TRUE) {
        echo "SUCCESSFULLY STORED";
    } else {
        echo "ERROR: " . $conn->error;
    }
    $conn->close();
}
?>

