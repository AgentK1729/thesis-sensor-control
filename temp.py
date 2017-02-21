import struct
import sys,os
import socket
import binascii
import pcapy
from time import time, sleep

def sniff():
	rawSocket = socket.socket(socket.PF_PACKET, socket.SOCK_RAW, socket.htons(0x0800))
	#ifconfig eth0 promisc up
	receivedPacket = rawSocket.recv(65565)

	#TCP Header...
	tcpHeader = receivedPacket[34:54]
	try:
		tcpHdr = struct.unpack("!4s4s12s", tcpHeader)
		sourcePort = socket.inet_ntoa(tcpHdr[0])
		destinationPort = socket.inet_ntoa(tcpHdr[1])
		
		# return (sourcePort, destinationPort)
		return True

	except Exception as e:
		# return ("exception-source", "exception-destination")
		return False


while True:
	end = time() + 10
	packets = 0
	print "Gathering",
	while time() < end:
		if sniff():
			packets += 1

	print packets

	sleep(10)