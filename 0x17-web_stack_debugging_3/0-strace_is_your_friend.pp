# there is a spelling error i.e. phpp
# so we change phpp to php
$edit = '/var/www/html/wp-settings.php'
exec {'change':
  command => "sed -i 's/phppp/php/g' ${edit}",
  path    => ['/bin', '/usr/bin']
}
