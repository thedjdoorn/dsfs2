import urllib2
from threading import Thread

import Levenshtein

AMOUNT_FETCHES = 100

finitial = urllib2.urlopen("http://focusweekend.nl/tickets/").read()
jinitial = urllib2.urlopen("https://www.ticketjames.com/").read()

fmin = 100
fmax = 0
ftotal = 0

jmin = 100
jmax  = 0
jtotal = 0


def focus():
    global ftotal
    global fmax
    global fmin

    fnew = urllib2.urlopen("http://focusweekend.nl/tickets/").read()
    l = Levenshtein.distance(fnew, finitial)
    ftotal += l
    if l < fmin:
        fmin = l
    if l> fmax:
        fmax = l


def james():
    global jtotal
    global jmax
    global jmin

    jnew = urllib2.urlopen("https://www.ticketjames.com/").read()
    l = Levenshtein.distance(jnew, jinitial)
    jtotal += l
    if l < jmin:
        jmin = l
    if l > jmax:
        jmax = l


fthreads = []
for i in range(AMOUNT_FETCHES):
    t = Thread(target=focus)
    fthreads.append(t)
    t.start()

print ("FThreads started")
jthreads = []
for x in range(AMOUNT_FETCHES):
    t = Thread(target=james)
    jthreads.append(t)
    t.start()

print ("JThreads started")
for f in fthreads:
    f.join()

print ("FThreads finished")
print ("FTotal " + str(ftotal))
print ("FAvg " + str(ftotal/AMOUNT_FETCHES))
print ("FMin " + str(fmin))
print ("FMax " + str(fmax))

for j in jthreads:
    j.join()

print ()
print ("JThreads finished")
print ("JTotal " + str(jtotal))
print ("JAvg " + str(jtotal/AMOUNT_FETCHES))
print ("JMin " + str(jmin))
print ("JMax " + str(jmax))