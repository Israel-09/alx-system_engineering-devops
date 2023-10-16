exec { "fix-server-error":
	provider	=> "shell",
	command		=> "sed -i 's/.phpp/php/g' /var/www/html/wp-settings.php",
}
