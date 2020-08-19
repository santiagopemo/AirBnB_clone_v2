# Redo the task #0 but by using Puppet

exec { 'update':
  command => 'sudo apt-get update',
  path    => ['/usr/bin', '/bin'],
}

package { 'nginx':
  ensure  => installed,
  require => Exec['update'],
}

file { '/data/web_static/releases/test':
  ensure  => directory,
  require => Package['nginx'],
}

file { '/data/web_static/shared':
  ensure  => directory,
  require => Package['/data/web_static/releases/test'],
}

file { 'index':
  ensure  => 'present',
  path    => '/data/web_static/releases/test/index.html',
  content => 'Holberton School web_static',
  require => File['/data/web_static/shared'],
}

file { 'current':
  ensure  => 'link',
  path    => '/data/web_static/current',
  target  => '/data/web_static/releases/test',
  require => File['index'],
}

exec { 'chown':
  command => 'sudo -R ubuntu:ubuntu /data/ ',
  path    => ['/usr/bin', '/bin'],
  require => File['current'],
}

exec { 'chown':
  command => 'sudo sed -i "/:80 default_server/ a \\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}" \
/etc/nginx/sites-available/default',
  path    => ['/usr/bin', '/bin'],
  require => exec['chown'],
}

exec { 'restart':
  command => 'sudo service nginx restart',
  path    => ['/usr/bin', '/bin'],
  require => exec['location1'],
}
