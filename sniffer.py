import struct
import sys,os
import socket
import binascii
import pcapy
from time import time, sleep
from datetime import datetime
from sqlite3 import connect

def sniff():
	rawSocket = socket.socket(socket.PF_PACKET, socket.SOCK_RAW, socket.htons(0x0800))
	receivedPacket = rawSocket.recv(65565)

	#TCP Header...
	tcpHeader = receivedPacket[34:54]
	try:
		tcpHdr = struct.unpack("!4s4s12s", tcpHeader)
		sourcePort = socket.inet_ntoa(tcpHdr[0])
		destinationPort = socket.inet_ntoa(tcpHdr[1])
		return True

	except Exception as e:
		return False

conn = connect("traffic.sqlite")
cur = conn.cursor()
query = "insert into traffic values (?, ?, ?)"

days = {"Monday":1, "Tuesday":2, "Wednesday":3, "Thursday":4, "Friday":5, "Saturday":6, "Sunday":7}
midnight = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
epoch = time() + 300
while time() < epoch:
	end = time() + 10
	packets = 0
	while time() < end:
		if sniff():
			packets += 1

	curr_time = (datetime.now()-midnight).seconds
	day = days[datetime.now().strftime("%A")]
	print day, curr_time, packets,
	cur.execute(query, (day, curr_time, packets))
	conn.commit()
	print "Added to db"

conn.close()