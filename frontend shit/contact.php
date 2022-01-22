<?php
$name = $_Post['name'];
$visitor_email = $_POST['email'];
$message = $_POST['message'];

$email_from = 'fluxcache@gmail.com';
$email_subject = "New Form Submission";

$email_body = "User Name: $name.\n". "User Email: $visitor_email.\n". "User Message: $message.\n";

$to = "fluxcache@gmail.com";

$headers = "From: $email_from \r\n";
$headers .= "Reply-To: $visitor_email \r\n";

mail($to,$email_subject,$email_body,$headers);
header("location: contact.html");



?> 