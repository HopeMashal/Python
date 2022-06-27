import random
import curses   #Use { https://pypi.org/project/windows-curses/ } --> RUN { pip install windows-curses } in terminal
# For more informations about curses use { https://docs.python.org/3/howto/curses.html }

# To run the code use { python Snake_Game.py } --> in Command Prompt

s = curses.initscr()  #? Whole Screen
curses.curs_set(0) #? Cursor State (visibility can be set to 0,1,2 for invisible,normal,very visible)
sh, sw = s.getmaxyx()  #? sh -> height, sw -> width ==> return a tuple (y , x) of the height and width of the window
w = curses.newwin(sh, sw, 0, 0)  #? return a new window, whose left-upper corner is at (0,0), and whose height/width is sh/sw
w.keypad(1)  #? Window is ready to receive commands using the keyboard
w.timeout(100)  #? every 100ms --> the window is updated

snk_x = sw//4  #? Initial location of the snake in x-axis
snk_y = sh//2  #? Initial location of the snake in y-axis
snake = [  #? The snake's coordinates
    [snk_y, snk_x],
    [snk_y, snk_x-1],
    [snk_y, snk_x-2]
]

food = [sh//2, sw//2] #? Initial location of the food in (y-axis , x-axis)
w.addch(food[0], food[1], curses.ACS_PI)  #? Paint food at (sh//2, sw//2) with attributes (Shape -> PI)

key = curses.KEY_RIGHT  #? Initial direction of the snake's movement (Right)

while True:  #? Infinite Loop (Stop when you are lose)
    next_key = w.getch()  #? When user click new bottom in the keyboard (up,down,right,left) --> New direction of the snake's movement
    key = key if next_key == -1 else next_key #? If user didn't click any bottom --> key value hasn't changed, BUT if user click any bottom --> change the direction to next_key value

    if snake[0][0] in [0, sh] or snake[0][1] in [0, sw] or snake[0] in snake[1: ]:
        curses.endwin()
        quit()
      #? Check if the snake hits the edge (border) of the window or itself --> GAME OVER
      

    new_head = [snake[0][0], snake[0][1]]

    if key == curses.KEY_DOWN:
        new_head[0] += 1
    if key == curses.KEY_UP:
        new_head[0] -= 1
    if key == curses.KEY_RIGHT:
        new_head[1] += 1
    if key == curses.KEY_LEFT:
        new_head[1] -= 1

    snake.insert(0, new_head)

    if snake[0] == food:
        food = None
        while food is None:
            nf = [
                random.randint(1, sh-1),
                random.randint(1, sw-1)
            ]
            food = nf if nf not in snake else None
        w.addch(food[0], food[1], curses.ACS_PI)
    else:
        tail = snake.pop()
        w.addch(tail[0], tail[1], ' ')

    w.addch(snake[0][0], snake[0][1], curses.ACS_CKBOARD)