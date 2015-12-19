import curses
#----------------------------------------------------------------------------#
def valid_move(window, dx, dy):
    pos = curses.getsyx()
    y, x = pos[0], pos[1]

    if not (y + dy) in range(0, window.getmaxyx()[0]):
        return False

    elif not (x + dx) in range(0, window.getmaxyx()[1]):
        return False

    else:
        return True
#----------------------------------------------------------------------------#
def move_cursor(window, dx, dy):

    pos = curses.getsyx()
    
    if valid_move(window, dx, dy):
        y = pos[0] + dy
        x = pos[1] + dx
    else:
        return False

    window.move(y,x)
    window.refresh()
    return True
#----------------------------------------------------------------------------#
