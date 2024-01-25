# Configure user limits for the 'holberton' user.

# Define the base command for adjusting limits
$limits_command = 'sed -i "/^holberton {0}/s/{1}/50000/g" /etc/security/limits.conf'

# Adjust hard limits for 'holberton' user
exec { 'adjust-hard-limits-for-holberton':
  command => $limits_command.format('hard', 4),
  path    => '/usr/local/bin:/bin/'
}

# Adjust soft limits for 'holberton' user
exec { 'adjust-soft-limits-for-holberton':
  command => $limits_command.format('soft', 5),
  path    => '/usr/local/bin:/bin/'
}
