import pyglet
from pyglet.window import mouse
from pyglet.gl import *

#Raw Events
MOUSEBUTTONDOWN = 22
MOUSEBUTTONUP   = 23
MOUSEMOTION     = 24
MOUSEDRAG       = 25
#Wrapped Events
MOUSECLICK      = 32

#Global Runtime Variables
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600 # This should be optimized later

window = pyglet.window.Window(width = WINDOW_WIDTH,
                              height = WINDOW_HEIGHT)

label = pyglet.text.Label("Hello world",
                          font_name = "Segue UI",
                          font_size = 10,
                          x = window.width//2,
                          y = window.height//2,
                          anchor_x = "center", anchor_y = "center")

class CASEvent():
    def __init__(self, event_type, source=None, modifiers=None):
        self.event_type = event_type
        self.source = source
        self.modifiers = modifiers

class AnimationModel():
    LINEAR = 10
    QUADRATIC = 11
    CUSTOMIZED = 12
    def __init__(self):
        self.animation = LINEAR

class LinearAnimationModel(AnimationModel):
    def __init__(self, speed=10):
        AnimationModel.__init__(self)


def dispatch_event(event):
    print(event)
    if (event.event_type == MOUSEBUTTONDOWN):
        label.text = str(event)
"""
class CASContext():
    def __init__(self):
        self.platform = pyglet.window.get_platform()
        self.display = pyglet.get_default_display()
""" # Accessible by pyglet.window directly, deprecated class

def isColor4f(color):
    if (type(color) != tuple and len(color) != 4):
        raise TypeError("Incorrect color type!")

def CASdrawRect(rect):
    assert(type(rect) == Rect)
    # With reference points starting from left upper corner of canvas
    x = rect.x
    y = WINDOW_HEIGHT - rect.y
    w = rect.w
    h = rect.h
    color = rect.color
    glBegin(GL_QUADS)
    glColor4f(color[0]/255, color[1]/255, color[2]/255, color[3]/255)
    glVertex2f(x, y)
    glVertex2f(x, y - h)
    glVertex2f(x + w, y - h)
    glVertex2f(x + w, y)
    glEnd()

class Rect():
    def __init__(self, x, y, w, h, parent=None, color=(255,255,255,255)):
        #Primitive test Rect Class, OpenGL implemented (Backend Connection)
        assert(parent == None or type(parent) == Rect)
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.parent = parent
        isColor4f(color)
        self.color = color

    def draw(self):
        CASdrawRect(self)

def __CASdrawRectWithBorder(boarder):
    pass

class Widget(pyglet.event.EventDispatcher):
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.active = True
        self.visible = True
        # Active will be overidden by visible
        pyglet.event.EventDispatcher.__init__(self)

    def on_mouse_clicked(self, event):
        self.dispatch_event("on_mouse_clicked", event)

Widget.register_event_type("on_mouse_clicked")

@window.event
def on_draw():
    glClear(GL_COLOR_BUFFER_BIT)
    window.clear()
    label.draw()
    glLoadIdentity()
    rect1 = Rect(50,100,300,100, color=(255,10,10,10))
    rect1.draw()

@window.event
def on_mouse_press(x, y, button, modifiers):
    if button == mouse.LEFT:
        dispatch_event(CASEvent(MOUSEBUTTONDOWN, button, modifiers))

pyglet.app.run()
