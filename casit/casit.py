#!/usr/bin/env python3

# Project casit GUI model
# ---------------------------------
# This project implementes the main GUI model for casper development kit
# All classes and functions, methods begin with prefix "UI"

import sys
from utils import debug

# Runtime Unique states of casit based on storyboards


def UIsystemInit():
    print("Initializing casit system - Why do I need this?")

def __UIgenerateWidgetID():
    # Efficient algorithm to generate non-colliding ids for different objects
    return "ran-dom-id1"

class UIAbstractWidget():
    def __init__(self):
        self.id = __UIgenerateWidgetID()

class UIWidget(UIAbstractWidget):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        super.init()

class UIWidgetGroup(UIAbstractWidget):
    def __init__(self, layer=0):
        self.layer = layer
        self.id = CASgenerateWidgetID()
        super.init()

if __name__ == "__main__":
    print(sys.version)
    CASsystemInit()
