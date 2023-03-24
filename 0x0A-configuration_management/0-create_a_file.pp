# create file /tmp/school with permission=0744, owner=www-data, group=www-data and content='I love puppet'
file { '/tmp/school':
  ensure  => 'file',
  path    => '/tmp/school',
  content => 'I love Puppet',
  owner   => 'www-data',
  group   => 'www-data',
  mode    => '0744',
}
