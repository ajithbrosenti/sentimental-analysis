<?php
    $hostname = "<host_name>";
    $username = "<user_name>";
    $pwd = "<password>";
    $db = "<db>";

    $conn = mysqli_connect($hostname, $username, $pwd, $db);
    
    if( !$conn ) 
        die("CONNECTION FAILED: ".mysqli_connect_error());
?>
