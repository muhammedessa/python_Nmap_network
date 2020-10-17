# python-nmap
#brew install nmap => OSX
#sudo apt-get install nmap => Linux
#export PATH="$PATH:/usr/local/nmap/bin"

#Windows
#C:\Program Files (x86)\Nmap
#My PC > System Information > Advance settings > Environment Variables

















#Scan A Single Host

# import nmap
# nm = nmap.PortScanner()
# scan_range = nm.scan(hosts="192.168.0.104")
# print (scan_range['scan'])















#Scan Multiple Hosts

# import nmap
# nm = nmap.PortScanner()
# scan_range = nm.scan(hosts="192.168.0.101 192.168.0.104 192.168.0.103 192.168.0.102")
# print (scan_range['scan'])











#Scan Range Of Hosts

# import nmap
# nm = nmap.PortScanner()
# scan_range = nm.scan(hosts="192.168.0.101-104")
# print (scan_range['scan'])












#CIDR Range

# import nmap
# nm = nmap.PortScanner()
# scan_range = nm.scan(hosts="192.168.0.1/24")
# print (scan_range['scan'])






