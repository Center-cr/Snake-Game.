import turtle
import time
import random
#上一步head动作
global pre_direction
#蛇的整体
global snake
#蛇还有多少没有伸展出来
global snake_hide
#蛇的身体segments[0]
global pre_x,pre_y
#蛇的身体长度
global contact
#monster画笔
global monster
#头部画笔
global head
#食物
global num_array,food_num,num_st
#其他信息画笔
global pen,pen1, pen2
#窗体
global wn
#时间计量
global starttime, endtime, time_eated, time_win, count, count2,time_lose,time_collision



## 怪物
monster = turtle.Turtle()
monster.shape("square")
monster.color("purple")
monster.penup()
monster.goto(200, 200)
monster.direction = "Stop"
pre_direction = "Stop"
monster.speed(1)

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

pen2 = turtle.Turtle()
pen2.speed(0)
pen2.shape("square")
pen2.color("black")
pen2.penup()
pen2.hideturtle()  # 隐藏笔迹
pen2.goto(0, 0)

#主窗体
starttime = time.time()
endtime = time.time()
count = 3
stop_flag = 0
contact = 5
delay = 0.1
high_contact = 0
# x = 0
# y = 0
wn = turtle.Screen()  ##画笔对象
wn = turtle.Screen()
wn.title("Snake Game")
wn.bgcolor("white")
# the width and height can be put as user's choice
wn.setup(width=580, height=660)
wn.tracer(0)


##蛇
def goup():
    if head.direction != "down":
        head.direction = "up"


def godown():
    # global monster, head, food, pen, pen1, num_array, food_num, wn, contact, delay, num_str, count
    if head.direction != "up":
        head.direction = "down"


def goleft():
    # global monster, head, food, pen, pen1, num_array, food_num, wn, contact, delay, num_str, count
    if head.direction != "right":
        head.direction = "left"


def goright():
    # global monster, head, food, pen, pen1, num_array, food_num, wn, contact, delay, num_str, count
    if head.direction != "left":
        head.direction = "right"


def stop():
    global pre_direction
    # print(pre_direction)
    if head.direction != "stop":
        pre_direction = head.direction
        head.direction = "stop"
        return
    if head.direction == "stop":
        head.direction = pre_direction
        print("之前动作",pre_direction)
        print("尝试恢复",head.direction)
        return

def move():
    # global monster, head, food, pen, pen1, num_array, food_num, wn, contact, delay, num_str, count
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
wn.onkeypress(goup, "Up") # if food_num == 0:
wn.onkeypress(stop," ")
wn.onkeypress(godown, "Down")
wn.onkeypress(goleft, "Left")
wn.onkeypress(goright, "Right")
def win():
    pen2.color("red")
    pen2.write("WIN", align="center",
              font=("candara", 30, "bold"))
def lose():
    pen2.color("black")
    pen2.write("LOOSE", align="center",
              font=("candara", 30, "bold"))
def staus_upgrade():
    # global monster, head, food, pen, pen1, num_array, food_num, wn, contact, delay, num_str, count,starttime ,endtime
    pen.clear()
    endtime = time.time()
    time_c = int(endtime - starttime)
    # print(time_c)
    pen.write("Contact: {} Time: {} Motion {} ".format(
        contact, time_c, head.direction), align="center", font=("candara", 18, "bold"))

def food_born():
    global food_num,foods,num_array,num_str,foods,num_array1,num_food
    food_x_array = []
    for i in range(0,food_num,1):
        food_x_array.append(random.randrange(-200,200))
    food_y_array = []
    for i in range(0,food_num,1):
        food_y_array.append(random.randrange(-270,200))
    #随机加载 1~ 5个食物

    foods= []
    for i in range(0,food_num,1):
        print("food_num", food_num, "num_array", num_array)
        food = turtle.Turtle()
        food.speed(0)
        food.shape("square")
        food.color("black")
        food.penup()
        food.hideturtle()  # 隐藏海龟
        food.goto(food_x_array[i], food_y_array[i])
        # num_str = random.choice(num_array)
        num_str =str(num_array[i])
        up_or_down = random.choice([0,1])
        if food_num == 1:
            up_or_down= 0
        print("up_or_down",up_or_down)
        if up_or_down == 0:
            print("food_generated",num_str)
            food.write(num_str, align="center",
                       font=("candara", 24, "bold"))
        else:
            pass
        foods.append(food)
        # time.sleep(0.05)

def If_Over():
    global foods
    global time_lose,time_collision
    global collision_flag,time_eated, time_win, monster, head, food, pen, pen1, num_array, food_num, wn, contact, delay, num_str, count, starttime, endtime,last_length
    if food_num == 0:
        # food.clear()
        time_win = time.time()
        print(int(time_win - time_eated))
        win()
        if int(time_win - time_eated) > 2:
            pen2.clear()
            for index in range(0,len(foods),1):
                foods[index].clear()
                time.sleep(0.2)
                kill_food()
                foods= []
            time.sleep(1)
            head.goto(1000, 1000)
            head.direction = "stop"
            head.clear()
            for segment in segments:
                segment.goto(1000, 1000)
            segments.clear()
            contact = 5
            delay = 0.1
            # pen1.pen.clear()
            pen.write("Contact: {} Time: {} Motion {} ".format(0, 0, 0), align="center", font=("Arial", 24, "bold"))
            init()
    if  collision_flag :
        time_lose = time.time()
        head.direction = "stop"
        lose()
        print("time_lose...................",int(time_lose - time_collision))
        if int(time_lose - time_collision)> 2:
            # food.clear()
            pen2.clear()
            kill_food()
            time.sleep(1)
            head.goto(1000, 1000)
            head.direction = "stop"
            head.clear()
            monster.goto(200, 200)
            for segment in segments:
                segment.goto(1000, 1000)
            segments.clear()
            contact = 5
            delay = 0.1
            # pen1.pen.clear()
            pen.write("Contact: {} Time: {} Motion {} ".format(0, 0, 0), align="center", font=("Arial", 24, "bold"))
            init()

def kill_food():
    global food_num,foods
    # for i in range(0,food_num):
    #     foods[i].clear()
    if len(foods)>0 :
         for i in range(0,len(foods)):
            foods[i].goto(3000,3000)
            foods[i].clear()
    foods = []

def food_eated():
    global snake_hide,monster, head, food, pen, pen1, num_array, food_num, wn, contact, delay, num_str, count, last_length,time_eated
    global foods,food_x_array,food_y_array,num_array1
    for index in reversed(range(0,len(foods))):
        # print("index--------------------------",index)
        if head.distance(foods[index]) < 20:
            if food_num > 0:
                food_num -= 1
            # print("food_num",food_num)
            # print("index......",index,"num_aray1",num_array1)
            foods[index].clear()
            time.sleep(0.1)
            kill_food()
            # del foods[index]
            time_eated = time.time()
            if int(num_array[index]) > 0:
                snake_hide += int(num_array[index])
                for i in range(int(num_array[index])):
                    new_segment = turtle.Turtle()
                    new_segment.speed(0)
                    new_segment.shape("square")
                    # new_segment.color(
                    #     "black")  # tail colour
                    new_segment.color("black")
                    new_segment.penup()
                    new_segment.setx(1000)
                    new_segment.sety(1000)
                    # new_segment.goto(x, y)
                    segments.append(new_segment)
                print("len seg", len(segments))
                contact += int(num_array[index])
                print("clear", num_array[index])
                del num_array[index]
            # num_str ='0'
            if food_num > 0:
                food_born()
            print("food_num ", food_num)
            # del_num()
            # if food_num > 0:
            #     foods[index].write(num_str, align="center",
            #                font=("candara", 20, "bold"))
            delay -= 0.001
            staus_upgrade()

def seg_move():
    global monster, head, food, pen, pen1, num_array, food_num, wn, contact, delay, num_str, count,pre_x,pre_y
    ##身体第一块跑向头
    if head.direction != "stop":
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
    global monster, head, food, pen, pen1, num_array, food_num, wn, contact, delay, num_str, count
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

def if_chased():
    global snake,collision_flag,segments,head,monster,time_collision
    # seg = segments
    # seg.append(head)
    for index in range(0,len(snake),1):
        if snake[index].distance(monster) <20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"
            time_collision= time.time()
            print("here..........qqqq.....................")
            colors = random.choice(['red', 'blue', 'green'])
            shapes = random.choice(['square', 'circle'])
            for segment in segments:
                segment.goto(1000, 1000)
            segment.clear()
            collision_flag = 1

def if_collision():
    global collision_flag, segments, time_collision
    if head.xcor() > 250 or head.xcor() < -250 or head.ycor() > 210 or head.ycor() < -290:
        collision_flag = 1
        time_collision = time.time()
def if_head_runto_body():
    global collision_flag,segments,time_collision
    for segment in segments:
        if segment.distance(head) < 20 and snake_hide == 0:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"
            print("here...............................")
            time_collision = time.time()
            colors = random.choice(['red', 'blue', 'green'])
            shapes = random.choice(['square', 'circle'])
            for segment in segments:
                segment.goto(1000, 1000)
            segment.clear()
            collision_flag = 1
            contact = 0
            delay = 0.1

def init():
    global monster, head, food, pen, pen1, num_array, food_num, wn, contact, delay, num_str, count, starttime , endtime
    global segments,snake_hide,collision_flag,food_x_array ,food_y_array ,foods,num_array1,count2
    # 初始化
    count2 = 10
    contact = 5
    collision_flag = 0
    starttime = time.time()
    endtime = time.time()
    segments = []
    # food.clear()
    # num_array = ['1', '2', '3', '4', '5']
    # food_num = 5
    # 蛇
    head = turtle.Turtle()
    head.shape("square")
    head.color("red")
    head.penup()
    head.goto(0, 0)
    head.direction = "stop"
    pre_direction = "stop"
    segments = []

    # 食物
    num_array = ['1', '2', '3', '4', '5']
    num_array1 = ['1', '2', '3', '4', '5']
    food_num = 5
    food_born()
    snake_hide = 5
    for i in range(5):
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        # new_segment.color(
        #     "black")  # tail colour
        new_segment.color("black")
        new_segment.penup()
        new_segment.setx(1000)
        new_segment.sety(1000)
        # new_segment.goto(x, y)
        segments.append(new_segment)

def Game_Start():
    global collision_flag,count2,snake,snake_hide,monster,head,food,pen,pen1,num_array,food_num,wn,contact,delay,num_str,count,last_length,segments
    ## 蛇走n步 ，怪物走 1 步
    wn.update()
    # food.write(num_str, align="center",
    #            font=("candara", 24, "bold"))
    count -= 1
    if count == 0:
        count = random.choice([ 2, 3, 4])
        chase()
    count2 -= 1
    if count2 == 0 :
        count2 = 50
        kill_food()
        food_born()

    ##游戏结束
    food_eated()
    snake = []
    snake.append(head)
    for i in range(0,len(segments),1):
        snake.append(segments[i])
    If_Over()
    # len(segments)
    seg_move()

    move()
    if snake_hide > 0 and head.direction != "stop":
        snake_hide -= 1
        time.sleep(0.05)
    # print("hide'''''",snake_hide)
    # Checking for head collisions with body segments
    if collision_flag == 0:
        if_head_runto_body()
        if_chased()
        if_collision()
    staus_upgrade()
    wn.ontimer(Game_Start, 100)

init()
seg_move()
Game_Start()
wn.mainloop()
# if __name__ == "main":
#      Game_Start()
#      wn.mainloop()