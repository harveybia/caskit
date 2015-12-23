#!/usr/bin/env python3

# Project Generic Event Dispatcher
# ---------------------------------
# This project implements a generic event dispatcher with a easy to use
# interface which includes customized event type and function which decides
# whether an event should be dispatched to a specific widget.

# Project Written in python3
import time
from utils import debug
DEBUG = 1

class GDEvent():
    event_type = "defaulteventtype"
    def __init__(self):
        pass

    def get_event_type(self):
        return type(self).event_type
"""
# Example customized Event class:
class EGClockSignal(GDEvent):
    event_type = "clocksignal"
    def __init__(self, category):
        GDEvent.__init__(self)
        self.category = categoryE
"""

class GDEventCollection():
    def __init__(self):
        self.collection = []

    def addEventType(self, Event):
        # Commenting the assertion of class requirement will allow 3rd
        # party event types to be easilly transmitted through mechanism
        # assert(issubclass(Event, GDEvent))
        self.collection.append(Event)

"""
def templateCheckBelongs(event):
    # For graphics
    return event.x <
"""

class GDDispatcher():
    # A dispatcher can be connected to another with levels
    def __init__(self, eventCollection):
        self.event_handlers = {} # event_handlers keeps track of listeners
        # O(length(eventCollection)) runtime complexity upon once initialzation)
        for event in eventCollection.collection:
            self.event_handlers[event.event_type] = [] # listener stack
        # A listener should be able to listen to same event type from different
        # dispatchers
        self.registered_dispatchers = {}
        debug("Dispathcer Initialized: %s"%str(self))

    def event_check_belongs(self, event):
        # This should be implemented by client
        return True

    def def_event_type(self, typ):
        # Handlers will NOT be overridden by redeclaring
        if typ not in self.event_handlers.keys():
            self.event_handlers[typ] = []
        else:
            pass

    def undef_event_type(self, typ):
        # Recursively undefine the types of events top down
        if not self.event_handlers[typ]:
            # Base case, unregister event from parent and undef it
            # The dispatcher will not maintain its access to event source
            # once all llisteners of the event type are unlinked
            self.unregister_event_type(self.registered_dispatchers[typ])
        for handler in self.event_handlers:
            # Recursively call undef
            handler.undef_event_type(typ)

    def register_event_type(self, target, *types):
        for typ in types:
            debug("registering event type: " + typ)
            if typ not in self.event_handlers.keys():
                debug("warning: registering undefined event")
                return
            else:
                if self not in target.event_handlers[typ]:
                    # Not duplicate allowed
                    target.event_handlers[typ].append(self)
                    if typ not in self.registered_dispatchers.keys():
                        self.registered_dispatchers[typ] = []
                    self.registered_dispatchers[typ].append(target)
                    debug("||registered type: " + typ + " from %s"%str(self))

    def unregister_event_type(self, target, *types):
        for typ in types:
            debug("unregistered event type: " + typ)
            if typ not in target.event_handlers.keys():
                debug("info: unregistering undefined event")
                return
            else:
                if self in target.event.handlers[typ]:
                    target.event_handlers[typ].remove(self)
                    assert(typ in self.registered_dispatchers.keys())
                    self.registered_dispatchers[typ].remove(target)
                else:
                    debug("warning: unregistering unregistered dispatcher")
                    return

    def invoke_event(self, event):
        # invoke_event is called when a dispatcher itself listens to
        # receives an event that is evaluated to be dispatched to it
        # according to the client event_belongs() function

        # This is usually not to be overridden
        if self.event(event):
            # This indicates that event has been handled and further
            # propagation for this event will happen
            return
        event_type = event.get_event_type()
        for handler in self.event_handlers[event_type]:
            if handler.event_check_belongs(event):
                handler.invoke_event(event)

    def event(self, event):
        # Design choice: event returns boolean value to see if event is
        # handled or not. If True is returned then the event will not
        # propagate further down from dispatcher

        # This method is to be overridden by customized classes
        debug("event received by %s"%str(self))
        debug("||event is %s"%str(event))
        return False

# Unit Test (Succeeded)
# ---------------------------------
# Example Application

class EGClockSignal(GDEvent):
    event_type = "clocksignal"
    def __init__(self, category):
        GDEvent.__init__(self)
        self.category = category

class EGOtherSignal(GDEvent):
    event_type = "othersignal"
    def __init__(self):
        GDEvent.__init__(self)

egcollection = GDEventCollection()
egcollection.addEventType(EGClockSignal)
egcollection.addEventType(EGOtherSignal)

class ExampleWidget(GDDispatcher):
    def __init__(self):
        GDDispatcher.__init__(self, egcollection)

egwidget = ExampleWidget()

class ExampleSubWidget(GDDispatcher):
    def __init__(self):
        GDDispatcher.__init__(self, egcollection)

    def event_check_belongs(self, event):
        if event.event_type == "clocksignal":
            # Event specific evaluation
            if event.category == 0:
                return True
            else:
                return False
        return True

egsubwidget = ExampleSubWidget()

egsubwidget.register_event_type(egwidget, "clocksignal")

# Function based mainloop
terminated = False
while not terminated:
    time.sleep(0.2)
    clkinstance = EGClockSignal(category = 0)
    clkinstance2 = EGClockSignal(category = 1)
    eventinstance = EGOtherSignal()
    egwidget.invoke_event(clkinstance)
    egwidget.invoke_event(clkinstance2)
    egwidget.invoke_event(eventinstance)
    debug("=================================")

"""
# A typical application class as driver loop
class GDApplication(GDDispatcher):
    def __init__(self):
        # Do some initialzation steps
        self.terminated = False

    def loop(self, *flags):
        while not self.terminated:
            # Poll event from native event dispatcher

    def start(self, *args):
        self.loop()
"""
