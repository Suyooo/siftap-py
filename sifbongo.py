import evdev
from select import select

devices = [evdev.InputDevice(path) for path in evdev.list_devices()]

locmap = {}
used = set()

for loc in range(1,10,2):
    print("Press START on bongos for spots " + str(loc) + " and " + str((loc+1)%10))
    locset = False
    while not locset:
        r, w, x = select(devices, [], [])
        for fd in r:
            for event in fd.read():
                if event.type != 1 or event.value == 0: continue
                if event.code == 295 or event.code == 297:
                    if fd.path in used: continue
                    if event.code == 297:
                        # Double GC Adapter
                        locmap[(fd.path,290)] = (loc, 0)
                        locmap[(fd.path,291)] = (loc, 1)
                        locmap[(fd.path,288)] = ((loc+1) % 10, 0)
                        locmap[(fd.path,289)] = ((loc+1) % 10, 1)
                    if event.code == 295:
                        # GC/PS/XB Adapter
                        locmap[(fd.path,289)] = (loc, 0)
                        locmap[(fd.path,291)] = (loc, 1)
                        locmap[(fd.path,288)] = ((loc+1) % 10, 0)
                        locmap[(fd.path,290)] = ((loc+1) % 10, 1)
                    used.add(fd.path)
                    locset = True
                    break

import siftap
presses = [0,0,0,0,0,0,0,0,0]

while 1:
    r, w, x = select(devices, [], [])
    for fd in r:
        for event in fd.read():
            if event.type != 1: continue
            locid, pos = locmap.get((fd.path,event.code), (None,None))
            if locid == None or locid == 0: continue
            
            pp = presses[locid-1]
            if event.value == 0:
                if pos == 0: presses[locid-1] = pp & 0b10
                else: presses[locid-1] = pp & 0b01
            else:
                if pos == 0: presses[locid-1] = pp | 0b01
                else: presses[locid-1] = pp | 0b10
            
            if presses[locid-1] == 0 and pp > 0: siftap.release(locid)
            elif presses[locid-1] > 0 and pp == 0: siftap.hold(locid)

siftap.quit()
quit()
