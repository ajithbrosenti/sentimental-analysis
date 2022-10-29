<?php
	$host = 'localhost';
	$db = 'chat';
	$username = 'moodle';
	$pwd = 'Moodle@123';
	$dns = "mysql:host=$host;dbname=$db";
	
	try {
		$conn = new PDO($dns, $username, $pwd);
		$conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
	}catch(PDOException $e) {
		echo "connection failed: ".$e->getMessage();
	}
?>
