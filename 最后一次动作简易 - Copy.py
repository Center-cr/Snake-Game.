import turtle
import time
import random

global game_state,pen2,monster,head,food,pen,pen1,num_array,food_num,wn,score,delay,num_str,count,pre_x,pre_y,starttime ,endtime, last_length,time_eated,time_win
## 怪物

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

monster = turtle.Turtle()
monster.shape("square")
monster.color("purple")
monster.penup()
monster.goto(200, 200)
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
pre_direction = "Stop"
segments = []

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
# 画布边距画笔
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

global pen2
pen2 = turtle.Turtle()
pen2.speed(0)
pen2.shape("square")
pen2.color("red")
pen2.penup()
pen2.hideturtle()  # 隐藏笔迹
pen2.goto(0, 0)

global pen3
pen3 = turtle.Turtle()
pen3.speed(0)
pen3.shape("square")
pen3.color("red")
pen3.penup()
pen3.hideturtle()  # 隐藏笔迹
pen3.goto(0, 0)


def init():
    global monster, head, food, pen, pen1, num_array, food_num, wn, score, delay, num_str, count, starttime , endtime
    global segments,game_state

    food_num= num_array = ['1', '2', '3', '4', '5']
    food_num = 5
    segments = []
    # food.clear()
    starttime = time.time()
    endtime = time.time()
    for i in range(5):
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        # new_segment.color(
        #     "black")  # tail colour
        new_segment.color(random.choice(["green", "red", "blue", "black", "yellow", "pink"]))
        new_segment.penup()
        new_segment.setx(1000)
        new_segment.sety(1000)
        # new_segment.goto(x, y)
        segments.append(new_segment)

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
    if head.direction != "stop":
        head.direction = "stop"
        return
    if head.direction == "stop":
        head.direction = pre_direction
        return
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


def win():
    # 输赢界面画笔
    global pen2
    pen2 = turtle.Turtle()
    pen2.speed(0)
    pen2.shape("square")
    pen2.color("red")
    pen2.penup()
    pen2.hideturtle()  # 隐藏笔迹
    pen2.goto(0, 0)
    pen2.write("WIN", align="center",
               font=("candara", 24, "bold"))
    time.sleep(3)
    pen2.clear()

def lose():
    global pen3
    # pen3 = turtle.Turtle()
    # pen3.speed(0)
    # pen3.shape("square")
    # pen3.color("black")
    # pen3.penup()
    # pen3.hideturtle()  # 隐藏笔迹
    # pen3.goto(0, 0)
    pen3.write("LOOSE", align="center",
               font=("candara", 24, "bold"))
    count_lose = 3
    while count_lose:
        count_lose -=1
        wn.ontimer(lose,100)
    # pen3.clear()
    # pen3.clear()

def staus_upgrade():
    global monster, head, food, pen, pen1, num_array, food_num, wn, score, delay, num_str, count,starttime ,endtime
    pen.clear()
    endtime = time.time()
    time_c = int(endtime - starttime)
    # print(time_c)
    pen.write("Contact: {} Time: {} Motion {} ".format(
        score, time_c, head.direction), align="center", font=("candara", 18, "bold"))

def If_Over():
    global pen3,time_eated, time_win, monster, head, food, pen, pen1, num_array, food_num, wn, score, delay, num_str, count, starttime, endtime,last_length
    if food_num == 0:
        print("here")
        time_win = time.time()
        print(int(time_win - time_eated))
        if int(time_win - time_eated) > 5:
            # win()
            clearall()
            init()
            Game_Start()
    if  head.xcor() > 250 or head.xcor() < -250 or head.ycor() > 210 or head.ycor() < -290:
        lose()
        # pen3.clear()
        clearall()
        init()
        Game_Start()



def clearall():
    time.sleep(1)
    #头部归位，停止运动
    head.goto(0, 0)
    head.direction = "Stop"
    #身体清空
    for segment in segments:
        segment.goto(1000, 1000)
    segments.clear()
    # pen1.pen.clear()
    # pen.write("Contact: {} Time: {} Motion {} ".format(0, 0, 0), align="center", font=("Arial", 24, "bold"))

def food_eated1():
    global monster, head, food, pen, pen1, num_array, food_num, wn, score, delay, num_str, count, last_length,time_eated
    if head.distance(food) < 20:
        food_num -= 1
        food.clear()
        score += int(num_str)
        time_eated = time.time()
        if int(num_str) > 0:
            for i in range(int(num_str)):
                new_segment = turtle.Turtle()
                new_segment.speed(0)
                new_segment.shape("square")
                # new_segment.color(
                #     "black")  # tail colour
                new_segment.color(random.choice(["green", "red", "blue", "black", "yellow", "pink"]))
                new_segment.penup()
                new_segment.setx(1000)
                new_segment.sety(1000)
                # new_segment.goto(x, y)
                segments.append(new_segment)
            print("len seg", len(segments))
        if food_num >0:
            ##生成一次食物减少一次，直到五次
            x = random.randint(-230, 230)
            y = random.randint(-270, 200)
            food.goto(x, y)
            num_str = random.choice(num_array)
            del_num()

        print("food_num ", food_num)
        print("array", len(num_array))
        if food_num == 0:
            last_length = num_str
            # If_Over()
        food.write(num_str, align="center",
                              font=("candara", 20, "bold"))
        delay -= 0.001
        staus_upgrade()

def food_eated():
    global monster, head, food, pen, pen1, num_array, food_num, wn, score, delay, num_str, count,time_eated
    if head.distance(food) < 20:
        food.clear()
        food_num -= 1
        time_eated = time.time()
        print("food_num ", food_num)
        # print("food_num ",food_num)
        score += int(num_str)
        # if score > high_score:
        #     high_score = score
        # Adding segment
        if len(segments) > 0:
            x = segments[len(segments) - 1].xcor()
            y = segments[len(segments) - 1].ycor()
        else:
            x = head.xcor()
            y = head.ycor()
        for i in range(int(num_str)):
            new_segment = turtle.Turtle()
            new_segment.speed(0)
            new_segment.shape("square")
            # new_segment.color(
            #     "black")  # tail colour
            new_segment.color(random.choice(["green", "red", "blue", "black", "yellow","pink"]))
            new_segment.penup()
            new_segment.setx(x)
            new_segment.sety(y)
            # new_segment.goto(x, y)
            segments.append(new_segment)
        print("len seg", len(segments))
        x = random.randint(-230, 230)
        y = random.randint(-270, 200)
        food.goto(x, y)
        num_str = random.choice(num_array)
        del_num()
        food.write(num_str, align="center",
                              font=("candara", 20, "bold"))
        delay -= 0.001
        staus_upgrade()

def grow():
    global monster, head, food, pen, pen1, num_array, food_num, wn, score, delay, num_str, count,pre_x,pre_y
    ##身体第一块跑向头
    if len(segments) > 0:
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
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"
            colors = random.choice(['red', 'blue', 'green'])
            shapes = random.choice(['square', 'circle'])
            for segment in segments:
                segment.goto(1000, 1000)
            segment.clear()
            score = 0
            delay = 0.1



def Game_Start():
    global monster,head,food,pen,pen1,num_array,food_num,wn,score,delay,num_str,count,last_length,segments
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
    # Checking for head collisions with body segments
    if_head_runto_body()
    staus_upgrade()
    wn.ontimer(Game_Start, 100)

# init()
grow()
Game_Start()
wn.mainloop()
# if __name__ == "main":
#      Game_Start()
