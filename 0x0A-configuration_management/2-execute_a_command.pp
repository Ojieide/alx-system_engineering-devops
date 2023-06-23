# Create a manifest that kills a process named killmenow using puppet
exec { 'pkill -f killmenow':
  path => '/usr/bin/:/usr/local/bin/:/bin/'
}
