import curses
import os
import sys
import time
from curses import *
from input_functs import *
from input_handler import *


HEIGHT = 30
WIDTH = 90
START_Y = 0
START_X = 0
DEFAULT_FPS = 60

def main():
    window = setup()
    while True:
        if game_clock.tick():
            game_loop(window)


def game_loop(window):
    input_handler.listen_for_key()
    #run logic
    window.refresh()

def setup():
    setup_curses()
    window = setup_window()
    global game_clock
    game_clock = Clock(DEFAULT_FPS)
    global input_handler
    input_handler = InputHandler(window)
    return(window)

def setup_curses():
    curses.initscr()
    curses.start_color()
    curses.cbreak()
    curses.noecho()
    curses.curs_set(1)

def setup_window():
    os.system("resize -s {} {}".format(HEIGHT,WIDTH))
    window = curses.newwin(HEIGHT, WIDTH, START_Y, START_X)
    window.keypad(True)
    window.nodelay(1)
    return(window)
    

class Clock:

    def __init__(self, clock_fps):
        self.fps = clock_fps
        self.last = time.time()

    def tick(self):
        now = time.time()
        time_delta = now - self.last  
                      
        if time_delta > (1/self.fps):
            self.last = now
            return True
        else:
            return False





main()
