# Redo the task #0 but by using Puppet

exec { 'update':
  command => 'sudo apt-get update',
  path    => ['/usr/bin', '/bin'],
}

package { 'nginx':
  ensure  => installed,
  require => Exec['update'],
}

exec { 'mkdir1':
  command => 'sudo mkdir -p /data/web_static/releases/test/',
  path    => ['/usr/bin', '/bin'],
  require => Package['nginx'],
}

exec { 'mkdir2':
  command => 'sudo mkdir -p /data/web_static/shared/',
  path    => ['/usr/bin', '/bin'],
  require => Exec['mkdir1'],
}

file { 'index':
  ensure  => 'present',
  path    => '/data/web_static/releases/test/index.html',
  content => "Holberton School web_static",
  require => Exec['mkdir2'],
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

file_line { 'location1':
  ensure  => present,
  path    => '/etc/nginx/sites-available/default',
  after   => 'listen 80 default_server;',
  line    => 'location /hbnb_static/ {',
  require => Exec['chown'],
}

file_line { 'location2':
  ensure  => present,
  path    => '/etc/nginx/sites-available/default',
  after   => 'location /hbnb_static/ {',
  line    => 'alias /data/web_static/current/;',
  require => File_line['location1'],
}

file_line { 'location3':
  ensure  => present,
  path    => '/etc/nginx/sites-available/default',
  after   => 'alias /data/web_static/current/;',
  line    => '}',
  require => File_line['location2'],
}

exec { 'restart':
  command => 'sudo service nginx restart',
  path    => ['/usr/bin', '/bin'],
  require => File_line['location'],
}
