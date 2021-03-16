import ipaddress

net4 = ipaddress.ip_network("10.30.26.64/27")
for host in net4.hosts():
    print(host)
