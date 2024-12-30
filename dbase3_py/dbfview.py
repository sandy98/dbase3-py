#!/usr/bin/env python3
#-*- coding: utf_8 -*-
# dbfview.py - A simple DBF file viewer using curses

import subprocess
import os, sys
if os.name == 'posix':
    import curses
elif os.name == 'nt':
    import unicurses as curses
else:
    print("Unsupported OS")
    sys.exit(1)

from functools import reduce
try:
    from dbase3_py.dbase3 import DbaseFile
except ImportError:
    from dbase3 import DbaseFile

def show(stdscr, title, subtitle, text):
    """
    Shows a list of scrolling text lines under a title and subtitle in a curses window.
    """
    max_line_length = reduce(lambda x, y: max(x, len(y)), text, 0)
    curses.cbreak()
    stdscr.keypad(True)

    # Initialize color pairs
    curses.start_color()
    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLUE)  # Unselected text
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_WHITE)   # Selected text
    curses.init_pair(3, curses.COLOR_BLUE, curses.COLOR_WHITE)  # Title
    curses.init_pair(4, curses.COLOR_WHITE, curses.COLOR_RED)   # Subtitle

    # Hide the cursor
    curses.curs_set(0)

    # Set default background color to blue
    stdscr.bkgd(' ', curses.color_pair(1))

    # Draw the title and subtitle once
    height, width = stdscr.getmaxyx()
    stdscr.addstr(0, 0, title.center(width), curses.color_pair(3))
    stdscr.addstr(1, 0, subtitle.ljust(width).rjust(len(subtitle)+1)[:width-1], curses.color_pair(4))

    index = 0
    start_line = 0  # Line in the list where the visible window starts
    prev_index = -1
    prev_start_line = -1

    while True:
        # Calculate the number of visible lines for scrolling, starting from the third line
        visible_lines = height - 2  # Leave the first 2 lines for the title and subtitle

        # Adjust the start_line to ensure the cursor stays within the visible window
        if index < start_line:
            start_line = index
        elif index >= start_line + visible_lines:
            start_line = index - visible_lines + 1

        # Only redraw lines if scrolling or index changes
        if start_line != prev_start_line or index != prev_index:
            # Redraw visible lines
            for i, line in enumerate(text[start_line:start_line + visible_lines]):
                # Calculate the screen line to draw on (offset by 2 for title and subtitle)
                screen_line = i + 2
                try:
                    if start_line + i == index:
                        attr = curses.color_pair(2)
                    else:
                        attr = curses.color_pair(1)
                    stdscr.addstr(screen_line, 0, line.rjust(max_line_length)[:width-1], attr)
                except curses.error as e:
                    sys.stderr.write(f"Error drawing line {start_line + i}: {e}\n")
                    sys.stderr.flush()
            # Update only changed parts of the screen
            curses.doupdate()

        # Update previous state
        prev_index = index
        prev_start_line = start_line

        # Wait for input
        key = stdscr.getch()

        # Handle key inputs
        if key == curses.KEY_UP and index > 0:
            index -= 1
        elif key == curses.KEY_DOWN and index < len(text) - 1:
            index += 1
        elif key == curses.KEY_PPAGE:  # Page Up
            index = max(0, index - visible_lines)
        elif key == curses.KEY_NPAGE:  # Page Down
            index = min(len(text) - 1, index + visible_lines)
        elif key == ord('q') or key == ord('Q') or key == 27:  # Quit on 'q'
            break

def main():
    if len(sys.argv) < 2:
        print("Usage: python dbfview.py <filename.dbf>")
        sys.exit(1)
    filename = sys.argv[1]
    if not os.path.exists(filename):
        print(f"File {filename} not found.")
        sys.exit(1)
    dbf = DbaseFile(filename)
    title = f"{filename} - {dbf.header.records} records"
    # subtitle = "Use arrow keys to scroll, 'q' to quit"
    if dbf.header.records == 0:
        text = ["No records found."]
    elif dbf.header.records > 10000:
        func = dbf.csv
        subtitle = dbf.csv_headers_line()
    else:
        func = dbf.lines       
        subtitle = dbf.headers_line()

    text = func().split('\n')
    try:
        curses.set_escdelay(25)  # Reduce delay for ESC key
    except:
        pass    
    try:
        curses.wrapper(lambda stdscr: show(stdscr, title, subtitle, text))
    except curses.error as e:
        subprocess.run(["clear"])
        sys.stderr.write(f"Error initializing curses: {e}\n")
        sys.stderr.flush()
        sys.exit(1)
    except KeyboardInterrupt as e:
        subprocess.run(["clear"])
        sys.exit(0)

if __name__ == "__main__":
    main()  # Run the main function if the script is executed directly
