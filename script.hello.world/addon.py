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
response = urllib.urlopen('https://m0z.xyz/deprimetv/get.php?mac='+mac)
hostname = socket.gethostname()

data = json.load(response)

title = data['title']
name = data['name']
room = data['room']
line1 = data['line1']+data['name']
line2 = data['line2']+data['room']
line3 = data['line3']


xbmcgui.Dialog().ok(title,line1,line2,line3)