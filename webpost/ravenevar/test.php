<?php

	$text = $_POST['feedback'];
	echo $text;
	fwrite(fopen('/var/www/html/messages/message.txt', 'a'), $text);
	echo "Successful.";
	fclose(fopen('/var/www/html/messages/message.txt', 'a'));

?>
