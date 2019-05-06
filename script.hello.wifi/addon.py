import xbmcaddon
import xbmcgui
import urllib
import uuid
import socket
import json

addon       = xbmcaddon.Addon()
addonname   = addon.getAddonInfo('name')
mac = ':'.join('%02X' % ((uuid.getnode() >> 8*i) & 0xff) for i in reversed(xrange(6)))
#response = urllib.urlopen('http://192.168.50.120/welcome.json'+mac)
response = urllib.urlopen('https://hello.roundtable-solution.com/spittze/getmx.php?mac='+mac)
hostname = socket.gethostname()

data = json.load(response)
#varirable from database
room = data['room_id']
user = data['user']
pwd  = data['pwd']
#text to display
title = "Spittze Hotel"
line1 = "Breakfast Time 6.00-10.00"
line2 = "Sleep with me Free SPITTZE WIFI"
line3 = "USER : "+user+" PWD : "+pwd

xbmcgui.Dialog().ok(title,line1,line2,line3)
