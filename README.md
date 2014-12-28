# IWY Master
Python Class to Controll the IWY Master Blub RGB with Width.

Amazon Link: http://www.amazon.de/gp/product/B00G8XUMS8

# Usage
Add the IWYMaster.py in the same Folder like you have your "controll" Script
```
from IWYMaster import IWYMaster
l = IWYMaster()
```
Add Lights to the Class (You can see the Connected Lamps on your Router):
```
l.addBlub("192.168.1.15", "Wohnzimmer")
l.addBlub("192.168.1.6", "Flur")
```
Turn Lights on:
```
l.on("Wohnzimmer")
l.on("Flur")
```
Turn Lighst off:
```
l.off("Wohnzimmer")
l.off("Flur")
```
Change Color:
The Colors are Byts RGB. You can also dimm the Lamp with this Command:
100% Red:
```
l.changeColor("Wohnzimmer", 0xff, 0x00, 0x00)
l.changeColor("Flur", 0xff, 0x00, 0x00)
```
50% Green:
```
l.changeColor("Wohnzimmer", 0x00, 0x77, 0x00)
l.changeColor("Flur", 0x00, 0x77, 0x00)
```
Turn on the "warm" white:
```
l.setWarmWidth("Wohnzimmer")
l.setWarmWidth("Flur")
```

Dimm the "warm" white:
```
l.setWarmWidth("Wohnzimmer", 0x44)
l.setWarmWidth("Flur", 0x44)
```

