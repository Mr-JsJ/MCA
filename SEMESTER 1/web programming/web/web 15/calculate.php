<html>  
<body>  
<form method="get">  
    Enter a number:  
    <input type="number" name="number">  
    <input type="submit" value="Submit">  
</form>  
</body>  
</html>  
<?php  
    if($_GET)
    {  
        $number = $_GET['number'];
        if( $number==0)
   {  
   echo "$number is nither odd or even"; 
          } 
        else if(($number % 2) == 0)
        {  
            echo "$number is an Even number";  
        }
        else
        {  
            echo "$number is Odd number";  
        }  
    }  
?>  
