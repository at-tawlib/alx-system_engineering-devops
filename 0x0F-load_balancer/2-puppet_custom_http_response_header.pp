# use puppet to automate creating HTTP header response

exec {'update':
  command => 'sudo apt-get update',
}

-> package { 'nginx':
  ensure => 'present',
}

-> file_line { 'header':
  path  => '/etc/nginx/nginx.conf',
  match => 'http {',
  line  => "http {\n\tadd_header X-Served-By \"${hostname}\";",
}

-> exec { 'run':
  command => 'sudo service nginx restart',
}
