import NetworkManager as nmg
from sqlite3 import connect
from time import sleep

def sniff():
	while True:
		ssids = {}

		for dev in nmg.NetworkManager.GetDevices():
		    if dev.DeviceType != nmg.NM_DEVICE_TYPE_WIFI:
		        continue

		    # key[0] = count, key[1] = total strength
		    aps = dev.SpecificDevice().GetAccessPoints()
		    for ap in sorted(aps, key=lambda ap: ap.Strength):
		        ssids[ap.Ssid] = ssids.get(ap.Ssid, [0, 0])
		        ssids[ap.Ssid][0] += 1
		        ssids[ap.Ssid][1] += ap.Strength
		        if ap.Ssid == "UMBC Campus":
		        	print ap.Ssid, ap.Frequency


		ssids_list = [(key, item[0], item[1]) for key, item in ssids.iteritems()]

		conn = connect("ssid.sqlite")
		cur = conn.cursor()
		query = "insert into signals values (?, ?, ?)"

		for tup in ssids_list:
			cur.execute(query, tup)

		conn.commit()
		conn.close()

		sleep(30)

sniff()