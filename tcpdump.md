# TCMPDUMP

#### capture icmp traffic on interface eth0
`sudo tcpdump -i eth0 icmp`

#### capture ssh traffic on interface eth0 and only capture 1000 packets
`sudo tcpdump -i eth0 port 22 -c 1000`

### capture icmp traffic from either source 192.168.1.95 or destination 192.168.1.87
`sudo tcpdump 'icmp and ((src 192.168.1.95 ) or (dst 192.168.1.87 ))'`

### Match all packets to/from ip. "-n" flag do not do DNS lookup
`sudo tcpdump -n -i eth0 host 192.168.1.87`

### capture dns request
`sudo tcpdump -i eth0 port 53`

### match icmp Echo responses
`sudo tcpdump 'icmp[icmptype] = icmp-echoreply'`

### Capture all DNS packets on a machine and write them to a file
`sudo tcpdump -n -i eth0 '(tcp or udp) and port 53' -w /tmp/dns-$(date +%Y-%m-%d).pcap`

### capture qos ipv4 AF4 packets 
`sudo tcpdump -i eth0 'ip[1] = 0x00'`

### capture qos ipv6 for http 
`sudo tcpdump -i eth0 ip6 and port 80`

### to get your tcpdump off, you can use scp
`scp /tmp/tcpdump_out.pcap ur_average_neteng@<host>:/tmp/out.pcap`

### other important flags
```
--list-interfaces : Shows all interfaces that can be captured
-n : Avoids port name resolution. Very useful to speedup capture
-N : Avoids domain name resolution. Very useful to speedup capture.
-nn : to avoid both port and domain name resolution
-r  : Reads from a file
-w  : Writes to a file
-s(number): Captures a slice of the packet. s96 will get only tcp header
-v : Turns on the verbose mode
-vv : Turns on more verbose
-vvv: Turns on even more verbose
```
