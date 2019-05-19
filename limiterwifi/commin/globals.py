import os


DEVNUL = open (os.devnull,'w')
BROADCAST = 'FF:FF:FF:FF:FF:FF'

BIN_TC = '/sbin/iptables'
BIN_IPTABLES = '/sbin/iptables'
BIN_SYSCTL ='/sbin/sysctl'

IP_FORWARD_LOC = 'net.ipv4.ip_forward'