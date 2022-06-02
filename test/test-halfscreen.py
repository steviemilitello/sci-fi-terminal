import curses 
from curses import wrapper, panel
from curses.textpad import Textbox, rectangle

curses.initscr()

win1 = curses.newwin(1, 20, 45, 87)


def main(stdscr):
    win1.clear()
    stdscr.addstr(17, 25, " _    _ _____ _     _____ ________  ___ _____ ",curses.A_BOLD)
    stdscr.addstr(18, 25, "| |  | |  ___| |   /  __ \  _  |  \/  ||  ___|",curses.A_BOLD)
    stdscr.addstr(19, 25, "| |  | | |__ | |   | /  \/ | | | .  . || |__  ",curses.A_BOLD)
    stdscr.addstr(20, 25, "| |/\| |  __|| |   | |   | | | | |\/| ||  __| ",curses.A_BOLD)
    stdscr.addstr(21, 25, "\  /\  / |___| |___| \__/\ \_/ / |  | || |___ ",curses.A_BOLD)
    stdscr.addstr(22, 25, " \/  \/\____/\_____/\____/\___/\_|  |_/\____/  ",curses.A_BOLD)
    stdscr.addstr(24, 37, "PRESS ENTER TO BEGIN ", curses.A_BOLD)
    win1.addstr("copyright", curses.A_BOLD)
    win1.refresh()
    # box = Textbox(win2)
    # rectangle(stdscr, 1, 1, 5, 20)
    # stdscr.refresh()
    # box.edit() #ctrl + g to get out
    # text = box.gather().strip().replace("\n", "") # for getting text to appear all on one line
    # stdscr.addstr(10, 40, text)
    while True:
        key = stdscr.getkey()
        if key == "KEY_ENTER" or ord("\n") or 10 or 13 or 36 or 76:
            stdscr.clear()
            win1.clear()
            rectangle(stdscr, 20, 5, 25, 85)
            stdscr.addstr(21, 7, "MESSAGES", curses.A_BOLD)
            stdscr.addstr(22, 7, "NAVIGATION", curses.A_BOLD)
            stdscr.addstr(23, 7, "DIAGNOSTICS", curses.A_BOLD)
            stdscr.addstr(21, 20, "CREW", curses.A_BOLD)
            stdscr.addstr(22, 20, "CARGO", curses.A_BOLD)
            stdscr.addstr(23, 20, "SYSTEM INFO", curses.A_BOLD)
            stdscr.refresh()
        else:
            stdscr.addstr(17, 25, "ERROR", curses.A_BOLD)

wrapper(main)

