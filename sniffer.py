import NetworkManager as nmg

for dev in nmg.NetworkManager.GetDevices():
    if dev.DeviceType != nmg.NM_DEVICE_TYPE_WIFI:
        continue

    aps = dev.SpecificDevice().GetAccessPoints()
    for ap in sorted(aps, key=lambda ap: ap.Strength):
        print ap.Ssid, ap.Strength