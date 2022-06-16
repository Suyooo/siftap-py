#!/usr/bin/python

import subprocess, random

siftap_input = "/dev/input/event2"
siftap_locs = {
    1: (140, 600),
    2: (178, 409),
    3: (286, 246),
    4: (449, 138),
    5: (640, 100),
    6: (831, 138),
    7: (994, 246),
    8: (1102, 409),
    9: (1140, 600)
}
siftap_reverse_coords = False

siftap_shell = None

def init():
    global siftap_shell
    
    subprocess.check_output(['adb','push','minitouch','/data/local/tmp/'])
    siftap_shell = subprocess.Popen(['adb','shell','/data/local/tmp/minitouch -i'], stdin=subprocess.PIPE)

def quit():
    global siftap_shell
    siftap_shell.kill()

def touchevent(t,locid):
    global siftap_shell,siftap_locs
    if not siftap_shell: raise Error("minitouch not started")    
    
    p = siftap_locs[locid]
    p = p if not siftap_reverse_coords else (p[1],p[0])
    if t == "t":
        siftap_shell.stdin.write(bytes("d "+str(locid)+" "+str(p[1])+" "+str(p[0])+" 50\nc\nw 50\nu "+str(locid)+"\nc\n","utf-8"))
    elif t == "h":
        siftap_shell.stdin.write(bytes("d "+str(locid)+" "+str(p[1])+" "+str(p[0])+" 50\nc\n","utf-8"))
    elif t == "r":
        siftap_shell.stdin.write(bytes("u "+str(locid)+"\nc\n","utf-8"))
    siftap_shell.stdin.flush()

def tap(locid): touchevent("t",locid)
def hold(locid): touchevent("h",locid)
def release(locid): touchevent("r",locid)

init()

if __name__ == "__main__":
    while True:
        try:
            i = input()
            if len(i) > 1: hold(int(i[0]))
            else: tap(int(i))
        except Exception as e:
            print(e)
