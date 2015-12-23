#!/usr/bin/env python3

# Project GUI Alignment Model
# ---------------------------------
# This project implements an alignment model used to determine effeiciently
# the position of widgets in its context dynamically with constraints

from genericEventDispatcher import GDEvent, GDDispatcher
from utils import debug

# Constraint events (abstract graphical events

class AMConstraintChanged(GDEvent):
    event_type = "AMconstraintchanged"
    def __init__(self, constraintItem):
        GDEvent.__init__(self)
        self.constraintItem = constraintItem

# Instance Unique states of Alignment Model for one storyboard
STORYBOARD_SET = 0


# Mechanism Implementation

def __getReferenceToWidget

class AMConstraint():
    def __init__(self, firstItem, firstAttribute, secondItem, secondAttribute,
                constant):

        self.firstItem = firstItem
        self.firstAttribute = firstAttribute
        self.secondItem = secondItem
        self.secondAttribute = secondAttribute

    def setActive(self, status):
        if status = True:
            self.active = True
            # Do stuff to invoke an constraint change event to view controller
