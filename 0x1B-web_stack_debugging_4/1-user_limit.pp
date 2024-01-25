# Puppet Manifest: Configure file limits for the Holberton user

# Description: This Puppet manifest facilitates the login and file operations for the user 'holberton' without encountering errors.

# Define hard file limit for the user 'holberton'
file { '/etc/security/limits.d/holberton-hard-limits.conf':
  ensure  => 'file',
  content => "holberton hard nofile 50000\n",
}

# Define soft file limit for the user 'holberton'
file { '/etc/security/limits.d/holberton-soft-limits.conf':
  ensure  => 'file',
  content => "holberton soft nofile 50000\n",
}
