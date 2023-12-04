# Install Nginx
package { 'nginx':
  ensure => installed,
}

# Configure custom HTTP header in Nginx
file { '/etc/nginx/sites-available/my_custom_site':
  ensure  => file,
  content => "server {
                listen 80 default_server;
                add_header X-Served-By $hostname;
                # Add other Nginx configurations as needed
              }",
  notify  => Service['nginx'],
}

# Create a symbolic link to enable the site
file { '/etc/nginx/sites-enabled/my_custom_site':
  ensure => link,
  target => '/etc/nginx/sites-available/my_custom_site',
  notify => Service['nginx'],
}

# Ensure Nginx service is running and enable it on boot
service { 'nginx':
  ensure  => running,
  enable  => true,
  require => Package['nginx'],
}
