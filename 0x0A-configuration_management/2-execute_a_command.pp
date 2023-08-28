# a manifest to kill running process, killmenow

exec { 'kill_command':
  command => 'pkill -f killmenow',
  path	  => ['/bin', '/usr/bin'],
}
