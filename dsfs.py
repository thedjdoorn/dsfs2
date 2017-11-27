import platform
import urllib2
import hashlib

from notify import *

print("Welkom bij Doorn's Schittermagische FocusScript - De 2018 editie!")
testNotification()
print("Als het goed is heb je nu een notificatie gehad. Zo niet dan heb je pech")

response = urllib2.open("http://focusweekend.nl/tickets/")
m = hashlib.md5()
m.update(response.read())
initial = m.digest()
