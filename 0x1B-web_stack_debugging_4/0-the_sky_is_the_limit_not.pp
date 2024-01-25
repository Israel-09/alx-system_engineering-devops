#increse the amount of traffic a server can handle


#uncrease the ulmit
exec {'increase ulmit':
  command => 'sed -i "s/15/4096"/ /etc/default/nginx',
  provider => shell
}

exec {'restart the server':
  command => "sudo service nginx restart",
  provider => shell
}
