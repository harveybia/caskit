#!/usr/bin/env python3
import sys
#import
#import kivy
#from scripts import easyterm

def CASsystemInit():
    #term = easyterm.TerminalController()
    #print term.render("${BLACK}${BG_WHITE}Initializing Casit environment${NORMAL}")
    print("TerminalController Test Success...")

def CASgenerateWidgetID():
    return "RaNdOmId"

class CASAbstractWidget():
    def __init__(self):
        self.id = CASgenerateWidgetID()

class CASWidget(CASAbstractWidget):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        super.init()

class CASWidgetGroup(CASAbstractWidget):
    def __init__(self, layer=0):
        self.layer = layer
        self.id = CASgenerateWidgetID()
        super.init()

if __name__ == "__main__":
    print(sys.version)
    CASsystemInit()
