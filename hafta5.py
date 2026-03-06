from scapy.layers.l2 import Dot3, LLC

from scapy.packet import Raw
from scapy.utils import wrpcap

from scapy.all import *


eth = Dot3(dst="ff:ff:ff:ff:ff:ff", src="00:11:22:33:44:55")


llc_layer = LLC(dsap=0xaa, ssap=0xaa, ctrl=3)


data = Raw(load="Merhaba! Bu bir sahte LLC cercevesidir.")

packet = eth / llc_layer / data
wrpcap("odev_test.pcap", packet)

print("Paket 'odev_test.pcap' adıyla kaydedildi.")

Muhammet Furkan Mengene

