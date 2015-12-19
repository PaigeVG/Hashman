from curses import *
from input_functs import *

class InputHandler:
    def __init__(self,window):
        self.window = window
    
        KEY_A = ord('a')
        KEY_D = ord('d')
        KEY_W = ord('w')
        KEY_S = ord('s')
    
        MOVE_LEFT  = move_cursor,(self.window, -1,  0)
        MOVE_RIGHT = move_cursor,(self.window,  1,  0)
        MOVE_UP    = move_cursor,(self.window,  0, -1)
        MOVE_DOWN  = move_cursor,(self.window,  0,  1)
    
        KEY_MAPPING = {KEY_A:     MOVE_LEFT,
                       KEY_LEFT:  MOVE_LEFT,
                       KEY_D:     MOVE_RIGHT,
                       KEY_RIGHT: MOVE_RIGHT,
                       KEY_W:     MOVE_UP,
                       KEY_UP:    MOVE_UP,
                       KEY_S:     MOVE_DOWN,
                       KEY_DOWN:  MOVE_DOWN}

   
    def listen_for_key(self):
        try:           
            key = self.window.getch()
            if key != -1:
                evaluate_key(key)
                return key
        except:
            return False 

    def evaluate_key(self, key):
        function = InputHandler.KEY_MAPPING[key][0]
        args = InputHandler.KEY_MAPPING[key][1]
        function(*args)
    

   





