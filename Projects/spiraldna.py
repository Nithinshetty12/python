# !/usr/bin/env python3
import os
import sys
import time
import math
from collections import deque

try:
    
    from colorama import init as colorama_init, Fore, Style
except ImportError:
    print("This script needs colorama. Install with: pip install colorama")
    sys.exit(1)

colorama_init()


FPS = 30                     
SCROLL_SPEED = 1            
AMPLITUDE_CAP = 20         
CONNECTOR_CHAR = "─"        
DNA_LETTERS = [("A", "T"), ("T", "A"), ("C", "G"), ("G", "C")]
DNA_COLORS = [Fore.CYAN, Fore.MAGENTA, Fore.GREEN, Fore.YELLOW] 
CONNECTOR_COLOR = Fore.BLUE
FADE_CONNECTOR = False    

def get_terminal_size():
    try:
        size = os.get_terminal_size()
        return size.columns, size.lines
    except OSError:
        return 80, 24

def hide_cursor():
    sys.stdout.write("\033[?25l")
    sys.stdout.flush()

def show_cursor():
    sys.stdout.write("\033[?25h")
    sys.stdout.flush()

def clear_screen():
    sys.stdout.write("\033[2J\033[H")
    sys.stdout.flush()

def clamp(n, low, high):
    return max(low, min(high, n))

def make_line(cols, left_x, right_x, base_left, base_right, color_pair):
    """
    Build one line with colored bases at left_x and right_x and a connector between.
    """
    left_x = int(left_x)
    right_x = int(right_x)
    if left_x > right_x:
        left_x, right_x = right_x, left_x
        base_left, base_right = base_right, base_left

    left_x = clamp(left_x, 0, cols-1)
    right_x = clamp(right_x, 0, cols-1)

    cells = [" "] * cols

    if right_x - left_x > 1:
        for i in range(left_x + 1, right_x):
            cells[i] = CONNECTOR_CHAR

    cells[left_x] = base_left
    cells[right_x] = base_right

    cL, cR = color_pair, color_pair
    conn_style = (Style.DIM if FADE_CONNECTOR else Style.NORMAL) + CONNECTOR_COLOR

    for i in range(cols):
        if i == left_x:
            cells[i] = cL + cells[i] + Style.RESET_ALL
        elif i == right_x:
            cells[i] = cR + cells[i] + Style.RESET_ALL
        elif cells[i] == CONNECTOR_CHAR:
            cells[i] = conn_style + cells[i] + Style.RESET_ALL

    return "".join(cells)

def main():
    cols, rows = get_terminal_size()

    rows = max(10, rows - 1)

    amplitude = min(AMPLITUDE_CAP, max(6, (cols // 2) - 6))
    center = cols // 2

    buffer = deque([" " * cols for _ in range(rows)], maxlen=rows)

    phase = 0.0
    phase_step = (2 * math.pi) / 24.0  
    frame = 0
    delay = 1.0 / FPS

    hide_cursor()
    clear_screen()

    try:
        while True:

            x_offset = math.sin(phase) * amplitude
            left_x = center - int(round(x_offset))
            right_x = center + int(round(x_offset))

            pair = DNA_LETTERS[frame % len(DNA_LETTERS)]
            color = DNA_COLORS[frame % len(DNA_COLORS)]
            base_left, base_right = pair[0], pair[1]

            line = make_line(cols, left_x, right_x, base_left, base_right, color)

            for _ in range(SCROLL_SPEED):
                buffer.append(line)


            sys.stdout.write("\033[H") 
            for ln in buffer:
                sys.stdout.write(ln + "\n")
            sys.stdout.flush()

            phase += phase_step
            frame += 1
            time.sleep(delay)

            if frame % 50 == 0:
                new_cols, new_rows = get_terminal_size()
                if new_cols != cols or new_rows != rows + 1:
                    cols, rows = new_cols, max(10, new_rows - 1)
                    amplitude = min(AMPLITUDE_CAP, max(6, (cols // 2) - 6))
                    center = cols // 2
                    buffer = deque([" " * cols for _ in range(rows)], maxlen=rows)
                    clear_screen()

    except KeyboardInterrupt:
        pass
    finally:
        show_cursor()
        sys.stdout.write(Style.RESET_ALL + "\n")
        sys.stdout.flush()

if __name__ == "__main__":
    main()
