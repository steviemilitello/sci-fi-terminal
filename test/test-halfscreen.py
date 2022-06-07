import curses 
from curses import wrapper
from curses.textpad import Textbox, rectangle

curses.initscr()

win1 = curses.newwin(1, 30, 44, 77)
win2 = curses.newwin(1, 50, 28, 22)
box = Textbox(win2)

def main(stdscr):
    win1.clear()
    win2.clear()
    stdscr.addstr(17, 25, " _    _ _____ _     _____ ________  ___ _____ ",curses.A_BOLD)
    stdscr.addstr(18, 25, "| |  | |  ___| |   /  __ \  _  |  \/  ||  ___|",curses.A_BOLD)
    stdscr.addstr(19, 25, "| |  | | |__ | |   | /  \/ | | | .  . || |__  ",curses.A_BOLD)
    stdscr.addstr(20, 25, "| |/\| |  __|| |   | |   | | | | |\/| ||  __| ",curses.A_BOLD)
    stdscr.addstr(21, 25, "\  /\  / |___| |___| \__/\ \_/ / |  | || |___ ",curses.A_BOLD)
    stdscr.addstr(22, 25, " \/  \/\____/\_____/\____/\___/\_|  |_/\____/  ",curses.A_BOLD)
    stdscr.addstr(24, 37, "PRESS ENTER TO BEGIN ", curses.A_BOLD)
    win1.addstr("copyright", curses.A_BOLD)
    win1.refresh()
    win2.refresh()
    while True:
        key = stdscr.getkey()
        if key == "KEY_ENTER" or ord("\n") or 10 or 13 or 36 or 76:
            stdscr.clear()
            win1.clear()
            win2.clear()
            rectangle(stdscr, 20, 19, 26, 92)
            rectangle(stdscr, 20, 5, 22, 35)
            rectangle(stdscr, 20, 5, 24, 35)
            rectangle(stdscr, 20, 5, 26, 35)
            rectangle(stdscr, 20, 19, 22, 35)
            rectangle(stdscr, 20, 19, 24, 35)
            rectangle(stdscr, 20, 19, 26, 35)
            stdscr.addstr(21, 7, "MESSAGES", curses.A_BOLD)
            stdscr.addstr(23, 7, "NAVIGATION", curses.A_BOLD)
            stdscr.addstr(25, 7, "DIAGNOSTICS", curses.A_BOLD)
            stdscr.addstr(21, 21, "CREW", curses.A_BOLD)
            stdscr.addstr(23, 21, "CARGO", curses.A_BOLD)
            stdscr.addstr(25, 21, "SYSTEM INFO", curses.A_BOLD)
            stdscr.addstr(28, 7, "ENTER COMMAND: ", curses.A_BOLD)
            while True:
                key = stdscr.getkey()
                if key == "KEY_ENTER" or ord("\n") or 10 or 13 or 36 or 76: 
                    box.edit()
                    text = box.gather().strip().replace("\n", "")
                    if text == "message" or "MESSAGE":
                        stdscr.addstr(30, 7, "VIEW / SEND ", curses.A_BOLD)
                    if text == "navigation" or "NAVIGATION":
                        stdscr.addstr(30, 7, "NAVIGATION ", curses.A_BOLD)
                    if text == "diagnostics" or "DIAGNOSTICS":
                        stdscr.addstr(30, 7, "DIAGNOSTICS ", curses.A_BOLD)
                    if text == "crew" or "CREW":
                        stdscr.addstr(30, 7, "CREW MANIFEST ", curses.A_BOLD)
                    if text == "cargo" or "CARGO":
                        stdscr.addstr(30, 7, "CARGO ", curses.A_BOLD)
                    if text == "system info" or "SYSTEM INFO ":
                        stdscr.addstr(30, 7, "SYSTEM INFO", curses.A_BOLD)
                    else:
                        stdscr.addstr(30, 7, "ERROR", curses.A_BOLD)

wrapper(main)

