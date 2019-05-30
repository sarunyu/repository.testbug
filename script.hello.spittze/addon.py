import xbmcaddon
import xbmcgui
import urllib
import uuid
import socket
import json

addon       = xbmcaddon.Addon()
addonname   = addon.getAddonInfo('name')
mac = ':'.join('%02X' % ((uuid.getnode() >> 8*i) & 0xff) for i in reversed(xrange(6)))
#hostname = socket.gethostname()    
#ip = socket.gethostbyname(hostname)  
#get data
response = urllib.urlopen('https://m0z.xyz/login/getmx.php?mac='+mac)
data = json.load(response)
#varirable from database
room = data['room']
name = data['name']
user = data['user']
pwd  = data['pwd']
stat = data['stats']
#text to display
title = "Welcome "+name+" to Spittze Hotel"
line1 = "The hotel has free wifi"
line2 = "Username : "+user+" and Password : "+pwd
line3 = "Have a good stay. Thank you."

dev1 = "Room is check-out"
dev2 = "Room Number "+room
dev3 = "MAC : "+mac
dev4 = "IP  : "
#condition
if stat =="Check-in":
    xbmcgui.Dialog().ok(title,line1,line2,line3)
else:
   xbmcgui.Dialog().ok(dev1,dev2,dev3,dev4)
