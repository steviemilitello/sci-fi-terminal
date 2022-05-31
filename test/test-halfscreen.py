import curses 
from curses import wrapper
from art import *

curses.initscr()

# win1 = curses.newwin(1, 20, 20, 45)
win2 = curses.newwin(1, 20, 45, 87)


def main(stdscr):
    # win1.clear()
    win2.clear()
    stdscr.addstr(17, 25, " _    _ _____ _     _____ ________  ___ _____ ",curses.A_BOLD)
    stdscr.addstr(18, 25, "| |  | |  ___| |   /  __ \  _  |  \/  ||  ___|",curses.A_BOLD)
    stdscr.addstr(19, 25, "| |  | | |__ | |   | /  \/ | | | .  . || |__  ",curses.A_BOLD)
    stdscr.addstr(20, 25, "| |/\| |  __|| |   | |   | | | | |\/| ||  __| ",curses.A_BOLD)
    stdscr.addstr(21, 25, "\  /\  / |___| |___| \__/\ \_/ / |  | || |___ ",curses.A_BOLD)
    stdscr.addstr(22, 25, " \/  \/\____/\_____/\____/\___/\_|  |_/\____/  ",curses.A_BOLD)
    stdscr.addstr(24, 37, "PRESS ENTER TO BEGIN",curses.A_BOLD)
    win2.addstr("copyright", curses.A_BOLD)
    stdscr.refresh()
    # win1.refresh()
    win2.refresh()
    stdscr.getch()


wrapper(main)