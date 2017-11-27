#!/usr/bin/env python
import platform

def notify (title, description):
    if (platform.system() == "Linux"):
        import gi
        gi.require_version('Notify', '0.7')
        from gi.repository import Notify
        Notify.init("Hello world")
        Hello=Notify.Notification.new(title, description, "dialog-information")
        Hello.show()
    elif (platform.system() == "Windows"):
        from win10toast import ToastNotifier
        toaster = ToastNotifier()
        toaster.show_toast(title, description)
    elif (platform.system() == "Darwin"):
        from Foundation import NSUserNotification
        from Foundation import NSUserNotificationCenter
        from Foundation import NSUserNotificationDefaultSoundName

        notification = NSUserNotification.alloc().init()
        notification.setTitle_(title)
        notification.setInformativeText_(description)

        center = NSUserNotificationCenter.defaultUserNotificationCenter()
        center.deliverNotification_(notification)

def testNotification ():
    notify("Dit is een testnotificatie", "Als je deze ziet werkt alles")
