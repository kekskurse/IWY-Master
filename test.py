from IWYMaster import IWYMaster
import time
l = IWYMaster()
l.addBlub("192.168.1.15", "Wohnzimmer")
l.addBlub("192.168.1.6", "Flur")
l.changeColor("Wohnzimmer", 0xff, 0x00, 0x00)
l.changeColor("Flur", 0xff, 0x00, 0x00)
time.sleep(2)
l.setWarmWidth("Wohnzimmer", 0xff)
l.setWarmWidth("Flur", 0xff)