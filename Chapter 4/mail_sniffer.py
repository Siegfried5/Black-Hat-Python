from scapy.all import *

# our packet callback
def packet_callback(packet):
	print packet.show()

# fire up our sniffer
<<<<<<< HEAD
sniff(prn=packet_callback,count=1)
=======
sniff(prn=packet_callback,count=1)
>>>>>>> origin/HEAD
