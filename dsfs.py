import urllib2
import argparse
import time
import Levenshtein


from notify import *

parser = argparse.ArgumentParser(description='Controleer voor wijzigingen op de Focus aanmeldpagina.', prog="dsfs.py")
parser.add_argument('-j', action='store_true', default=False, dest="james", help="Controleer ook de TicketJames homepagina")
parser.add_argument('-i', action='store', dest='interval', type=int, help="Interval voor het ophalen in seconden", default=30 )
args = parser.parse_args()

print("Welkom bij Doorn's Schittermagische FocusScript - De 2018 editie!")
testNotification()
print("Als het goed is heb je nu een notificatie gehad. Zo niet dan heb je pech")

fresponse = urllib2.urlopen("http://focusweekend.nl/tickets/")
finitial = fresponse.read()

if args.james:
    jresponse  = urllib2.urlopen("https://www.ticketjames.com/")
    jinitial = jresponse.read()

running = True
while running:
    altered = False
    domain = ""

    time.sleep(args.interval)
    print("Focus site checken...")
    fopen = urllib2.urlopen("http://focusweekend.nl/tickets/")
    fnew = fopen.read()
    if Levenshtein.distance(finitial, fnew) > 145:
        print("Focus is anders")
        altered  = True
        domain = "http://focusweekend.nl/tickets/"
    if args.james:
        print("TJ site checken...")
        jopen = urllib2.urlopen("https://www.ticketjames.com/")
        jnew = jopen.read()
        if Levenshtein.distance(jinitial, jnew) > 47:
            print("TJ is anders")
            altered = True
            domain = "https://www.ticketjames.com/"

    if altered:
        running = False
        notify("Website is aangepast", "Snel, ga kijken of er tickets zijn!")

