# Define the file resource
file {'/tmp/school':
  ensure  => file,
  mode    => '0744',
  owner   => 'www-data',
  group   => 'ww-data',
  content => 'I love Puppet',
}
