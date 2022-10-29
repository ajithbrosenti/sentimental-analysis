<?php
	$host = '<host_name>';
	$db = '<database_name>';
	$username = '<user_name>';
	$pwd = '<password>';
	$dns = "mysql:host=$host;dbname=$db";
	
	try {
		$conn = new PDO($dns, $username, $pwd);
		$conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
	}catch(PDOException $e) {
		echo "connection failed: ".$e->getMessage();
	}
?>
