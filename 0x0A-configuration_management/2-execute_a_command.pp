#exec killmenow
exec { 'killmenow':
    command  => 'pkill -f "killmenow"',
    provider => 'shell',
}
