# Project Generic Event Dispatcher
# ---------------------------------
# This project implements a generic event dispatcher with a easy to use
# interface which includes customized event type and function which decides
# whether an event should be dispatched to a specific widget.

DEBUG = 1

def debug(text):
    if DEBUG:
        print("DEBUG: " + str(text))

class GDEvent():
    def __init__(self, event_type):
        assert(type(event_type) == str)
        self.event_type = event_type

    def get_event_type(self):
        return self.event_type
"""
# Example customized Event class:
class MyGraphicsEvent(GDEvent):
    def __init__(self):
        GDEvent.__init__(self, "graphics")
"""

class GDEventCollection():
    def __init__(self):
        self.collection = []

    def addEventType(self, event):
        assert(issubclass(event, GDEvent))
        self.collection.append(event)

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
        for event in eventCollection:
            self.event_handlers[event.event_type] = [] # listener stack
        debug("Dispathcer Initialized...")

    def event_check_belongs(self, event):
        # This should be overridden by client
        # to
        return True

    def register_event_type(self, target, *types):
        for typ in types:
            debug("registered event type: " + typ)

    def unregister_event_type(self, target, *types):
        for typ in types:
            debug("unregistered event type: " + typ)

    def invoke_event(self, event):
        # invoke_event is called when a dispatcher itself listens to
        # receives an event that is evaluated to be dispatched to it
        # according to the client event_belongs() function
        event_type = event.get_event_type
        for handler in self.event_handlers[event_type]:
            if handler.event_check_belongs(event):
                invoke_event(event)
