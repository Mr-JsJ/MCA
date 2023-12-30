<?php
$host = "localhost";
$username = "root";
$password = "";
$database = "book";

$conn = new mysqli($host, $username, $password, $database);
if($conn->connect_error)
{
die("connection failed".$conn->connect_error);
}
$result = mysqli_query($conn, "SELECT * FROM book_details");
if (mysqli_num_rows($result) > 0) {
    echo "<h2>Book Details:</h2>";
    echo "<table border='1'>";
    echo "<tr><th>Book No</th><th>Title</th><th>Edition</th><th>Publisher</th></tr>";

    while ($row = mysqli_fetch_assoc($result)) {
        echo "<tr><td>{$row['book_no']}</td><td>{$row['title']}</td><td>{$row['edition']}</td><td>{$row['publisher']}</td></tr>";
    }

    echo "</table>";
} else {
    echo "No books found.";
}

mysqli_close($conn);
?>


<html>
<head>
    <title>Book Details</title>
</head>
<body>
    <form method="post" action="form.php">
        <label for="book_no">Book No:</label>
        <input type="text" name="book_no" required><br>

        <label for="title">Title:</label>
        <input type="text" name="title" required><br>

        <label for="edition">Edition:</label>
        <input type="text" name="edition" required><br>

        <label for="publisher">Publisher:</label>
        <input type="text" name="publisher" required><br>

        <input type="submit" value="Add Book">
    </form>
</body>
</html>
