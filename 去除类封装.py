import turtle
import time
import random

global monster,head,food,pen,pen1,num_array,food_num,wn,score,delay,num_str,count
## 怪物
monster = turtle.Turtle()
monster.shape("square")
monster.color("purple")
monster.penup()
monster.goto(200, 200)
monster.direction = "Stop"
pre_direction = "Stop"
monster.speed(1)

#蛇
head = turtle.Turtle()
head.shape("square")
head.color("red")
head.penup()
head.goto(0, 0)
head.direction = "Stop"
pre_direction = "Stop"
segments = []


#食物
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
score = 0
delay = 0.1
high_score = 0
# x = 0
# y = 0
wn = turtle.Screen()  ##画笔对象
segments = []
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
wn.listen()
wn.onkeypress(group, "w")
wn.onkeypress(godown, "s")
wn.onkeypress(goleft, "a")
wn.onkeypress(goright, "d")


def staus_upgrade():
    global monster, head, food, pen, pen1, num_array, food_num, wn, score, delay, num_str, count
    pen.clear()
    endtime = time.time()
    time_c = int(endtime - starttime)
    # print(time_c)
    pen.write("Contact: {} Time: {} Motion {} ".format(
        score, time_c, head.direction), align="center", font=("candara", 18, "bold"))


def If_Over():
    global monster, head, food, pen, pen1, num_array, food_num, wn, score, delay, num_str, count
    if food_num == 0 or head.xcor() > 250 or head.xcor() < -250 or head.ycor() > 210 or head.ycor() < -290:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "Stop"
        # colors = random.choice(['black', 'blue', 'green'])
        # shapes = random.choice(['square', 'circle'])
        for segment in segments:
            segment.goto(1000, 1000)
        segments.clear()
        score = 0
        delay = 0.1
        # pen1.pen.clear()
        pen.write("Contact: {} Time: {} Motion {} ".format(0, 0, 0), align="center",
                            font=("Arial", 24, "bold"))
        food.clear()

        num_array = ['1', '2', '3', '4', '5']
        food_num = 5

        starttime = time.time()
        endtime = time.time()


def food_eated():
    global monster, head, food, pen, pen1, num_array, food_num, wn, score, delay, num_str, count
    if head.distance(food) < 20:
        food.clear()
        food_num -= 1
        print("food_num ", food_num)
        If_Over()
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
            new_segment.color(random.choice(["green", "red", "blue", "black", "yellow"]))
            new_segment.penup()
            # new_segment.setx(x)
            # new_segment.sety(y)
            new_segment.goto(x, y)
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
    global monster, head, food, pen, pen1, num_array, food_num, wn, score, delay, num_str, count
    ##身体第一块跑向头
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)
    for index in range(len(segments) - 1, 0, -1):
        # for index in range(0,len(segments)-1, 1):
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x, y)
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)
    #     time.sleep(0.001)
    # for index in range(0,len(segments) - 1, 1):
    #     # for index in range(0,len(segments)-1, 1):
    #     x = segments[index].xcor()
    #     y = segments[index].ycor()
    #     segments[index+1].goto(x, y)
    #     time.sleep(0.001)
    # move()


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


def Game_Start():
    global monster,head,food,pen,pen1,num_array,food_num,wn,score,delay,num_str,count
    # while True:
    # wn.ontimer()
    # .chase(head)

    # .speed(5)
    count -= 1
    if count == 0:
        count = 3
        chase()
    wn.update()
    ##游戏结束
    If_Over()
    food_eated()
    # len(segments)
    grow()
    move()
    # Checking for head collisions with body segments
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
            # staus_upgrade()
            # pen1.pen.clear()
            # endtime = time.time()
            # time_c = int(endtime-starttime)
            # print(time_c)
            # pen1.pen.write("Score : {} High Score : {}  Time: {}".format(
            #     score, high_score, time_c), align="center", font=("candara", 24, "bold"))
    staus_upgrade()
    wn.ontimer(Game_Start, 100)


Game_Start()
wn.mainloop()
# if __name__ == "main":
#      Game_Start()
#      wn.mainloop()