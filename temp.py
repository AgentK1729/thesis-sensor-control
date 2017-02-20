import struct
import sys,os
import socket
import binascii
import pcapy
from time import sleep

def sniff():
	rawSocket = socket.socket(socket.PF_PACKET, socket.SOCK_RAW, socket.htons(0x0800))
	#ifconfig eth0 promisc up
	receivedPacket = rawSocket.recv(2048)

	#TCP Header...
	tcpHeader = receivedPacket[34:54]
	try:
		tcpHdr = struct.unpack("!4s4s12s", tcpHeader)
		sourcePort = socket.inet_ntoa(tcpHdr[0])
		destinationPort = socket.inet_ntoa(tcpHdr[1])
		
		return (sourcePort, destinationPort)

	except Exception as e:
		print "Exception"
		return ("exception-source", "exception-destination")


volume = {}
count = 0
while count < 10:
	print count
	(source, dest) = sniff()
	volume[source] = volume.get(source, -1) - 1
	volume[dest] = volume.get(dest, 1) + 1
	count += 1

print volume