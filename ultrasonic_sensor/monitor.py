import serial, sys
from sqlite3 import connect
from time import sleep

"""
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
"""

import colorama
colorama.init()
def put_cursor(x,y):
    print "\x1b[{};{}H".format(y+1,x+1)

def clear():
    print "\x1b[2J"


def disp_map(Map):
	final = ''
	for row in Map:
		final += ''.join(row) + '\n'
	return final

def init_map():
	Map = []
	for i in range(20):
		Map.append(["x"] + [" "]*39 + ["x"])
	return Map


def generate_line(values, Map, index):
	# green = front, red = left, yellow = right
	green, red, yellow = values[0], values[1], values[2]

	x_count_red = 20 - int(round(red/10))
	x_count_yellow = 20 - int(round(yellow/10))
	Map[index] = ["x"]*x_count_red + [" "]*(20-x_count_red) +\
	[" "] + [" "]*(20-x_count_yellow) + ["x"]*x_count_yellow

	return Map



clear()
put_cursor(0,0)
Map = init_map()
from random import randint
index = 0
while True:
	Map = generate_line([randint(5,100), randint(5,100), randint(5,100)], Map, 19-index)
	print disp_map(Map)
	sleep(1)
	put_cursor(0,0)
	index = (index+1) % 20
	if index == 0:
		Map = init_map()