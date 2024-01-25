# Configure OS settings to allow smooth 
# login and file operations for the 'holberton' user.

# Adjust hard limits for 'holberton' user
exec { 'adjust-hard-limits-for-holberton':
  command => "sed -i '/^holberton hard/s/4/50000/g' /etc/security/limits.conf",
  path    => '/usr/local/bin:/bin/'
}

# Adjust soft limits for 'holberton' user
exec { 'adjust-soft-limits-for-holberton':
  command => "sed -i '/^holberton soft/s/5/50000/g' /etc/security/limits.conf",
  path    => '/usr/local/bin:/bin/'
}
