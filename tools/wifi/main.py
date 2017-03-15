from scapy.all import *

def printPackage(package):
    if package.haslayer(Dot11Beacon):
        print "[802.11] : Beacon"
    elif package.haslayer(Dot11ProbeReq):
        print "[802.11] : ProbeReq"
    elif package.haslayer(TCP):
        print "[TCP]"
    elif package.haslayer(DNS):
        print "[DNS]"
        
sniff(iface="mon0", prn=printPackage)

