from curses import *
from input_functs import *

class InputHandler:
    def __init__(self,window):
        self.window = window
    
        self.KEY_A = ord('a')
        self.KEY_D = ord('d')
        self.KEY_W = ord('w')
        self.KEY_S = ord('s')
    
        self.MOVE_LEFT  = move_cursor,(self.window, -1,  0)
        self.MOVE_RIGHT = move_cursor,(self.window,  1,  0)
        self.MOVE_UP    = move_cursor,(self.window,  0, -1)
        self.MOVE_DOWN  = move_cursor,(self.window,  0,  1)
    
        self.key_mapping = {self.KEY_A:     self.MOVE_LEFT,

                            self.KEY_D:     self.MOVE_RIGHT,

                            self.KEY_W:     self.MOVE_UP,

                            self.KEY_S:     self.MOVE_DOWN}

    def listen_for_key(self):
        #try:           
        key = self.window.getch()
        if key == 410:
            print("fuck me in the ass and call me sally")
        elif key != -1:
            self.evaluate_key(key)
            return key
        #except:
            #return False 

    def evaluate_key(self, key):
        function = self.key_mapping[key][0]
        args = self.key_mapping[key][1]
        function(*args)

