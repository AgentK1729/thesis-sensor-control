import serial, sys
from sqlite3 import connect
from time import sleep


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




def monitor(Map, index):
	# ser_monitor = serial.Serial('/dev/ttyACM0', 115200)	
	while True:
		from random import randint
		# line = [int(i) for i in ser_monitor.readline().split("\t")[:-1]]
		line = [randint(10, 50), randint(10, 50), randint(10, 50)]
		Map = generate_line(line, Map, 19-index)
		index = (index+1) % 20
		return (disp_map(Map), line, index)