import turtle
import time
import random

global snake_hide,collision_flag,monster,head,food,pen,pen1,num_array,food_num,wn,score,delay,num_str,count,pre_x,pre_y,starttime ,endtime, last_length,time_eated,time_win
## 怪物
monster = turtle.Turtle()
monster.shape("square")
monster.color("purple")
monster.penup()
monster.goto(random.randint(110,210), random.randint(110,210))
monster.direction = "Stop"
pre_direction = "Stop"
monster.speed(1)
# 蛇
head = turtle.Turtle()
head.shape("square")
head.color("red")
head.penup()
head.goto(0, 0)
head.direction = "Stop"





##b标题画笔
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("black")
pen.penup()
pen.hideturtle()  # 隐藏笔迹
pen.goto(0, 210)
pen.write("Score : 0  High Score : 0", align="center",
               font=("candara", 24, "bold"))
#画布画笔
pen1 = turtle.Turtle()
pen1.speed(0)
pen1.shape("square")
pen1.color("black")
pen1.penup()
pen1.hideturtle()  # 隐藏笔迹
pen1.goto(-250, 210)
pen1.pendown()
pen1.forward(500)
pen1.right(90)
pen1.forward(500)
pen1.right(90)
pen1.forward(500)
pen1.right(90)
pen1.forward(580)
pen1.right(90)
pen1.forward(500)
pen1.right(90)
pen1.forward(580)



#主窗体
starttime = time.time()
endtime = time.time()
count = 3
stop_flag = 0
score = 6

high_score = 0

wn = turtle.Screen()  ##画笔对象
wn = turtle.Screen()
wn.title("Snake Game")
wn.bgcolor("white")
# the width and height can be put as user's choice
wn.setup(width=580, height=660)
wn.tracer(0)




##蛇
def group():
    if head.direction != "down":
        head.direction = "up"


def godown():
    global monster, head, food, pen, pen1, num_array, food_num, wn, score, delay, num_str, count
    if head.direction != "up":
        head.direction = "down"


def goleft():
    global monster, head, food, pen, pen1, num_array, food_num, wn, score, delay, num_str, count
    if head.direction != "right":
        head.direction = "left"


def goright():
    global monster, head, food, pen, pen1, num_array, food_num, wn, score, delay, num_str, count
    if head.direction != "left":
        head.direction = "right"


def stop():
    global monster, head, food, pen, pen1, num_array, food_num, wn, score, delay, num_str, count
    pre_direction = head.direction
    # if head.direction != "stop":
    #     head.direction = "stop"
    #     return
    # if head.direction == "stop":
    #     head.direction = pre_direction
    #     return
# 食物
def del_num():
    global monster, head, food, pen, pen1, num_array, food_num, wn, score, delay, num_str, count
    ##关键代码，解决无法删除列表中某个值的问题
    if len(num_array) > 0:
        for i in reversed(range(len(num_array))):
            if num_array[i] == num_str:
                del num_array[i]
                # print(num_array[i])
def move():
    global monster, head, food, pen, pen1, num_array, food_num, wn, score, delay, num_str, count
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
    if head.direction == "down":
            y = head.ycor()
            head.sety(y - 20)
    if head.direction == "left":
            x = head.xcor()
            head.setx(x - 20)
    if head.direction == "right":
            x = head.xcor()
            head.setx(x + 20)
#设置监听
wn.listen()
wn.onkeypress(group, "w") # if food_num == 0:
        #     for i in range(int(last_length)):
        #         print(int(last_length))
        #         move()
        #         grow()
        #         move()
        #         time.sleep(1)
wn.onkeypress(godown, "s")
wn.onkeypress(goleft, "a")
wn.onkeypress(goright, "d")


def staus_upgrade():
    global monster, head, food, pen, pen1, num_array, food_num, wn, score, delay, num_str, count,starttime ,endtime
    pen.clear()
    endtime = time.time()
    time_c = int(endtime - starttime)
    # print(time_c)
    pen.write("Contact: {} Time: {} Motion {} ".format(
        score, time_c, head.direction), align="center", font=("candara", 18, "bold"))


def If_Over():
    global collision_flag,time_eated, time_win, monster, head, food, pen, pen1, num_array, food_num, wn, score, delay, num_str, count, starttime, endtime,last_length
    if food_num == 0:
        print("here")
        time_win = time.time()
        print(int(time_win - time_eated))
        if int(time_win - time_eated) > 5:
            time.sleep(10)
    if collision_flag or head.xcor() > 250 or head.xcor() < -250 or head.ycor() > 210 or head.ycor() < -290:
        food.clear()
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "Stop"
        monster.goto(random.randint(110, 210), random.randint(110, 210))
        for segment in segments:
            segment.goto(1000, 1000)
        segments.clear()
        score = 0
        delay = 0.1
        # pen1.pen.clear()
        pen.write("Contact: {} Time: {} Motion {} ".format(0, 0, 0), align="center",font=("Arial", 24, "bold"))
        init()

def food_eated():
    global monster, head, food, pen, pen1, num_array, food_num, wn, score, delay, num_str, count, last_length,time_eated
    if head.distance(food) < 20:
        food_num = len(num_array)
        food.clear()
        score += int(num_str)
        time_eated = time.time()
        if int(num_str) > 0:
            head.direction = int(num_str)
            for i in range(int(num_str)):
                new_segment = turtle.Turtle()
                new_segment.speed(0)
                new_segment.shape("square")
                # new_segment.color(
                #     "black")  # tail colour
                new_segment.color(random.choice(["green", "red", "blue", "black", "yellow", "pink"]))
                new_segment.penup()
                new_segment.setx(2000)
                new_segment.sety(2000)
                # new_segment.goto(x, y)
                segments.append(new_segment)
            print("len seg", len(segments))
        if food_num > 0:
            ##生成一次食物减少一次，直到五次
            x = random.randint(-230, 230)
            y = random.randint(-270, 200)
            food.goto(x, y)
            num_str = random.choice(num_array)

        print("food_num ", food_num)
        if food_num == 0:
            last_length = num_str
            # If_Over()
        del_num()
        food.write(num_str, align="center",
                              font=("candara", 20, "bold"))
        delay -= 0.001
        staus_upgrade()

def grow():
    global monster, head, food, pen, pen1, num_array, food_num, wn, score, delay, num_str, count,pre_x,pre_y
    ##身体第一块跑向头
    if len(segments) > 0:
        # pre_seg = turtle.Turtle()
        # pre_seg.shape("square")
        # # new_segment.color(
        # #     "black")  # tail colour
        # pre_seg.color(random.choice(["green", "red", "blue", "black", "yellow", "pink"]))
        # pre_seg.penup()
        pre_x = segments[0].xcor()
        pre_y = segments[0].ycor()
        # pre_seg.goto(x, y)
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)
    for index in range(len(segments) - 1, 0, -1):
        # for index in range(0,len(segments)-1, 1)
        if index == 1:
            segments[1].goto(pre_x, pre_y)
            return
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x, y)

def chase():
    global monster, head, food, pen, pen1, num_array, food_num, wn, score, delay, num_str, count
    x = head.xcor()
    y = head.ycor()
    x1 = monster.xcor()
    y1 = monster.ycor()
    # if abs(y1-y) > abs(x1-x):
    #     if y1 < y:
    #         monster1.monster.sety(y1 + 20)
    #     else:
    #         .sety(y1 - 20)
    # else:
    #     if x1 < x:
    #         .setx(x1 + 20)
    #     else:
    #         .setx(x1 - 20)
    # wn.tracer(n=5, delay=0)
    if abs(y1 - y) > abs(x1 - x):
        if y1 < y:
            monster.seth(90)
            monster.forward(20)
        else:
            monster.seth(270)
            monster.forward(20)
    else:
        if x1 < x:
            monster.seth(0)
            monster.forward(20)
        else:
            monster.seth(180)
            monster.forward(20)

def if_head_runto_body():
    global collision_flag, time_eated, time_win, monster, head, food, pen, pen1, num_array, food_num, wn, score, delay, num_str, count, starttime, endtime, last_length
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            print("i am here")
            # collision_flag = 1
            head.direction = "Stop"
            colors = random.choice(['red', 'blue', 'green'])
            shapes = random.choice(['square', 'circle'])
            for segment in segments:
                segment.goto(1000, 1000)
                segment.clear()
            # return 1
            # init()
            # Game_Start()
            score = 0
            delay = 0.1

def init():
    global collision_flag,monster, head, food, pen, pen1, num_array, food_num, wn, score, delay, num_str, count, starttime , endtime
    global segments,snake_hide
    # 初始化
    collision_flag = 0
    starttime = time.time()
    endtime = time.time()
    segments = []
    # 食物
    num_array = ['1', '2', '3', '4', '5']
    num_str = random.choice(num_array)
    food = turtle.Turtle()
    food.speed(0)
    food.shape("square")
    food.color("black")
    food.penup()
    food.hideturtle()  # 隐藏笔迹
    food.goto(0, 100)
    food.write(num_str, align="center",
               font=("candara", 24, "bold"))
    food_num = 5
    for i in reversed(range(len(num_array))):
        if num_array[i] == num_str:
            del num_array[i]
    #尾巴初始长度为5
    snake_hide = 5
    for i in range(5):
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        # new_segment.color(
        #     "black")  # tail colour
        new_segment.color(random.choice(["green", "red", "blue", "black", "yellow", "pink"]))
        new_segment.penup()
        new_segment.setx(2000)
        new_segment.sety(2000)
        # new_segment.goto(x, y)
        segments.append(new_segment)

def Game_Start():
    global snake_hide,collision_flag,monster,head,food,pen,pen1,num_array,food_num,wn,score,delay,num_str,count,last_length,segments
    ## 蛇走n步 ，怪物走 1 步
    wn.update()
    food.write(num_str, align="center",
               font=("candara", 24, "bold"))
    count -= 1
    if count == 0:
        count = random.choice([ 2, 3, 4])
        chase()

    ##游戏结束
    food_eated()
    If_Over()
    # len(segments)
    grow()

    move()
    if snake_hide > 0 and head.direction != "Stop":
        snake_hide -= 1
    print("hide'''''",snake_hide)
    # Checking for head collisions with body segments
    if_head_runto_body()
    staus_upgrade()
    wn.ontimer(Game_Start, 100)

init()
grow()
Game_Start()
wn.mainloop()
# if __name__ == "main":
#      Game_Start()
#      wn.mainloop()