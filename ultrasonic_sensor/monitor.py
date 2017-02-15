import serial
from sqlite3 import connect

monitor = serial.Serial('/dev/ttyACM0', 115200)

while True:
	conn = connect("data.sqlite")
	cur = conn.cursor()
	query = "insert into sensor_data(green, red, yellow) values (?, ?, ?)"
	line = [int(i) for i in monitor.readline().split("\t")[:-1]]
	cur.execute(query, line)
	print line
	conn.commit()
	conn.close()