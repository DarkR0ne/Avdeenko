from ipaddress import *
ip_сети = "111, 81, 192, 0"
ip_узла = "111,81,208,27"
for mask in range(33):
    net = ip_network(f"{ip_сети}/{mask}", )
    if ip_узла in str(net):
        print(net.netmask)
