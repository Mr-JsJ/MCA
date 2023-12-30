<?php
setcookie('user_email', '', time() - 3600, '/');
header('Location: index.html');
exit();
?>
