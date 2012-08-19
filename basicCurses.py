# -*- coding: utf-8 -*-
import curses

def main(self):
    screen = curses.initscr()
    screen.border(0)
    
    #main loop
    while True:
        #write title on the first line (x=0)
        screen.addstr(0,15, 'My great menu')
        screen.addstr(8,2, '1 - What is the answer to life ? ')
        screen.addstr(9,2, '2 - Give me my computer uptime')
        screen.addstr(15,2, 'q - Bye Bye')
        #get user input
        event = screen.getch()
        if event == ord("q"):
            break
        elif event == ord("1"):
            #just print 42
        elif event == ord("2"):
            #print uptime  
    #restore your terminal in its original state
    curses.endwin()

if __name__ == '__main__':
    #use curses.wrapper to keep your terminal "safe"
    curses.wrapper(main)
