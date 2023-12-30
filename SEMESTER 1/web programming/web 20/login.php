<?php
$host = "localhost";
$username = "root";
$password = "";
$database = "userlogin";

$conn = mysqli_connect($host, $username, $password, $database);

if ($conn) {
    if (isset($_REQUEST["login"])) {
        $mail = $_REQUEST["email"];
        $password = $_REQUEST["password"];

        $sql = "SELECT * FROM students";
        $result = mysqli_query($conn, $sql);

        while ($row = mysqli_fetch_array($result)) {
            if (($row['mail'] == $mail) && ($row['password'] == $password)) {
                setcookie("user_email", $mail, time() + (86400 * 30), "/");
                header("Location:student-details.php");
                exit();
            } else {
                $flag=0;
            }
        }
        if($flag==0){
            echo "<script> alert('Incorrect Username or Password') </script>";
        }
    }

    mysqli_close($conn);
}
?>
