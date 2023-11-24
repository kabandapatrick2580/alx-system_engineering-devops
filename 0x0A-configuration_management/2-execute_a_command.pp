# Kill the "killmenow" process using pkill
exec { 'killmenow_process':
command => 'pkill - killmenow',
refreshonly => true,
onlyif => 'pgrep -f killmenow',
}
