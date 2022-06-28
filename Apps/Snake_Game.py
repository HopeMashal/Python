import random
import curses   #Use { https://pypi.org/project/windows-curses/ } --> RUN { pip install windows-curses } in terminal
# For more information about curses use { https://docs.python.org/3/howto/curses.html }

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

snake_life = 3
w.addstr(0, (sw//2)-11, "Your Snake Life : ")
w.addstr(0, (sw//2)+7, str(snake_life))
w.addstr(0, (sw//2)+8, "/3")

key = curses.KEY_RIGHT  #? Initial direction of the snake's movement (Right)

while True:  #? Infinite Loop (Stop when you are lose)

    w.addstr(1, (sw//2)-11, "Your Snake Length : ")
    w.addstr(1, (sw//2)+9, str(len(snake)))

    next_key = w.getch()  #? When user click new button in the keyboard (up,down,right,left) --> New direction of the snake's movement
    key = key if next_key == -1 else next_key #? If user didn't click any button --> key value hasn't changed, BUT if user click any button --> change the direction to next_key value

    if snake[0][0] in [0, sh] or snake[0][1] in [0, sw] or snake[0] in snake[1: ]:
        snake_life -= 1
        if snake_life !=0:
            w.clear()
            w.addstr(0, (sw//2)-11, "Your Snake Life : ")
            w.addstr(0, (sw//2)+7, str(snake_life))
            w.addstr(0, (sw//2)+8, "/3")
            snake = [ 
                [snk_y, snk_x],
                [snk_y, snk_x-1],
                [snk_y, snk_x-2]
            ]
            key = curses.KEY_RIGHT
            w.addch(snake[0][0], snake[0][1], curses.ACS_CKBOARD)
            food = [sh//2, sw//2] 
            w.addch(food[0], food[1], curses.ACS_PI)
        if snake_life == 0:
            curses.endwin()
            print("GAME OVER!! :(")
            quit()
      #? Check if the snake hits the edge (border) of the window or itself --> if snake's life is equal (0 -> ZERO) => GAME OVER (Close the window) 

    new_head = [snake[0][0], snake[0][1]]   #? The coordinates of the head (snake's head)

    if key == curses.KEY_DOWN:
        new_head[0] += 1
    if key == curses.KEY_UP:
        new_head[0] -= 1
    if key == curses.KEY_RIGHT:
        new_head[1] += 1
    if key == curses.KEY_LEFT:
        new_head[1] -= 1
        #? The new location (coordinates) of the snake's head when the user click any button

    snake.insert(0, new_head)  #? Change the value of snake's head to (new head)

    if snake[0] == food: #? If snake eat the food (the snake's head and the food in the same coordinates)
        food = None  #? No food
        while food is None: #? If No food run this loop
            nf = [  #? New Food Array (coordinate (y,x)) 
                random.randint(3, sh-1),
                random.randint(1, sw-1)
            ]
            food = nf if nf not in snake else None  #? If new food doesn't hit with snake's body --> food = new food, ELSE food = None
        w.addch(food[0], food[1], curses.ACS_PI)   #? ADD the food to the screen
    else:
        tail = snake.pop()  #? If snake doesn't eat the food, delete the tail
        w.addch(tail[0], tail[1], ' ')  #? tail value is equal space

    try:
        w.addch(snake[0][0], snake[0][1], curses.ACS_CKBOARD)  #? The snake's shape
    except:
        w.clear()
        print("ERROR: Snake hits the border of the screen")
