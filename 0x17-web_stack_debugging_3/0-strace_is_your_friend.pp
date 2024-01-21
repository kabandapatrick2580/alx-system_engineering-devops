# A puppet to replace a line in a file on a server
$my_file = '/var/www/html/wp-settings.php'
#replacing line containing "phpp" with "php"
exec { 'replace_line':
  command => "sed -i 's/phpp/php/g' ${my_file}",
  path    => ['/bin','/usr/bin']
}
