from curses import *
from input_functs import *

KEY_A = ord('a')
KEY_D = ord('d')
KEY_W = ord('w')
KEY_S = ord('s')

def input_init():
    MOVE_LEFT  = move_cursor,(window, -1,  0)
    MOVE_RIGHT = move_cursor,(window,  1,  0)
    MOVE_UP    = move_cursor,(window,  0, -1)
    MOVE_DOWN  = move_cursor,(window,  0,  1)


class InputHandler:

    #KEY_MAPPING = {KEY_A:     MOVE_LEFT,
    #               KEY_LEFT:  MOVE_LEFT,
    #               KEY_D:     MOVE_RIGHT,
    #               KEY_RIGHT: MOVE_RIGHT,
    #               KEY_W:     MOVE_UP,
    #               KEY_UP:    MOVE_UP,
    #               KEY_S:     MOVE_DOWN,
    #               KEY_DOWN:  MOVE_DOWN}

    def __init__(self):
        KEY_MAPPING = {KEY_A:     MOVE_LEFT,
               KEY_LEFT:  MOVE_LEFT,
               KEY_D:     MOVE_RIGHT,
               KEY_RIGHT: MOVE_RIGHT,
               KEY_W:     MOVE_UP,
               KEY_UP:    MOVE_UP,
               KEY_S:     MOVE_DOWN,
               KEY_DOWN:  MOVE_DOWN}
    
    def listen_for_key(self,window):
        try:           
            key = window.getch()
            if key != -1:
                evaluate_key(key)  
                return key
        except:
            return False

    def evaluate_key(self, key):
        print("Key is being evaluated weee!!")
        function = InputHandler.KEY_MAPPING[key][0]
        args = InputHandler.KEY_MAPPING[key][1]
        function(*args)
        #eval(InputHandler.KEY_MAPPING[key])





