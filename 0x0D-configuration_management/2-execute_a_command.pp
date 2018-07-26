# Using Puppet, create a manifest that kills a process named 'killmenow'
# Must use 'exec' and 'pkill'

exec { 'pkill killmenow':
  command => '/usr/bin/pkill -f /killmenow',
}
