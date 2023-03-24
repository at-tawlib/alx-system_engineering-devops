# kills a process named kllmenow
exec { 'pkill':
  command => '/bin/pkill killme',
  path    => '/usr/bin:/usr/sbin:/bin',
}
