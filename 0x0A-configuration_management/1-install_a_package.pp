# a puppet manifest that install flask

package { 'flask':
    ensure	=> '2.1.0',
    provider	=> 'pip3',
}
