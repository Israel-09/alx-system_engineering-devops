# script that installs and configure nginx for a web server

package { 'nginx':
  ensure => 'installed',
}

exec { 'allow https':
  command =>	"usr/sbin/ufw allow 'Nginx HTTP'",
}

file { 'root page':
  ensure  => 'present',
  path    => '/var/www/html/index.html',
  content => 'Hello World!',
}

file_line { 'configure redirect':
  path  => '/etc/nginx/sites-enabled/default',
  line  => "server_name _;\n\trewrite ^redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;",
  match => 'server_name _;',
}
