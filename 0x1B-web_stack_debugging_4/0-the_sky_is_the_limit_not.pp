# puppet manifest to increase the amount of request a server can process

exec { 'increase the limit':
  command  => 'sed -i "s/15/2048/g" /etc/default/nginx',
  provider => 'shell',
}

-> exec { 'nginx-restart':
  command => 'service nginx restart',
  provide => 'shell'
}
