import turtle
import time
import random

class Monster():
    def __init__(self):

        self.monster = turtle.Turtle()
        self.monster.shape("square")
        self.monster.color("purple")
        self.monster.penup()
        self.monster.goto(200, 200)
        self.monster.direction = "Stop"
        self.pre_direction = "Stop"
        self.monster.speed(1)
    def chase(self,head):
        x=head.xcor()
        y=head.ycor()
        x1=self.monster.xcor()
        y1=self.monster.ycor()
        if abs(y1-y) > abs(x1-x):
            if y1 < y:
                self.monster.sety(y1 + 20)
            else:
                self.monster.sety(y1 - 20)
        else:
            if x1 < x:
                self.monster.setx(x1 + 20)
            else:
                self.monster.setx(x1 - 20)
        # self.monster.ontimer(self.chase, 100)

# global x, y
class Snake():
    def __init__(self):

        self.head = turtle.Turtle()
        self.head.shape("square")
        self.head.color("red")
        self.head.penup()
        self.head.goto(0, 0)
        self.head.direction = "Stop"
        self.pre_direction = "Stop"
        # self.keylisten()
        self.x = 0
        self.y = 0

    def group(self):
        if self.head.direction != "down":
            self.head.direction = "up"

    def godown(self):
        if self.head.direction != "up":
            self.head.direction = "down"

    def goleft(self):
        if self.head.direction != "right":
            self.head.direction = "left"

    def goright(self):
        if self.head.direction != "left":
            self.head.direction = "right"

    def stop(self):
        self.pre_direction = self.head.direction
        if self.head.direction != "stop":
            self.head.direction = "stop"
            return
        if self.head.direction == "stop":
            self.head.direction = self.pre_direction
            return

    def move(self):
        if self.head.direction == "up":
            self.y = self.head.ycor()
            self.head.sety(self.y + 20)
        if self.head.direction == "down":
            self.y = self.head.ycor()
            self.head.sety(self.y - 20)
        if self.head.direction == "left":
            self.x = self.head.xcor()
            self.head.setx(self.x - 20)
        if self.head.direction == "right":
            self.x = self.head.xcor()
            self.head.setx(self.x + 20)
        # print(self.x,self.y)


class Food():
    def __init__(self):
        self.num_array = ['1', '2', '3', '4', '5']
        self.num_str = random.choice(self.num_array)
        self.food = turtle.Turtle()
        self.food.speed(0)
        self.food.shape("square")
        self.food.color("black")
        self.food.penup()
        self.food.hideturtle()  # 隐藏笔迹
        self.food.goto(0, 100)
        self.food.write(self.num_str, align="center",
                        font=("candara", 24, "bold"))
        self.food_num = 5
        self.del_num()

    def del_num(self):
        ##关键代码，解决无法删除列表中某个值的问题
        if len(self.num_array) > 0:
            for i in reversed(range(len(self.num_array))):
                if self.num_array[i] == self.num_str:
                    del self.num_array[i]
                    # print(self.num_array[i])


class Pen():
    def __init__(self):
        self.pen = turtle.Turtle()
        self.pen.speed(0)
        self.pen.shape("square")
        self.pen.color("black")
        self.pen.penup()
        self.pen.hideturtle()  # 隐藏笔迹
        self.pen.goto(0, 210)
        self.pen.write("Score : 0  High Score : 0", align="center",
                       font=("candara", 24, "bold"))
        # self.pen.goto(0,210)
        # self.pen.forward(500)


class Pen1():
    def __init__(self):
        self.pen = turtle.Turtle()
        self.pen.speed(0)
        self.pen.shape("square")
        self.pen.color("black")
        self.pen.penup()
        self.pen.hideturtle()  # 隐藏笔迹
        self.pen.goto(-250, 210)
        self.pen.pendown()
        self.pen.forward(500)
        self.pen.right(90)
        self.pen.forward(500)
        self.pen.right(90)
        self.pen.forward(500)
        self.pen.right(90)
        self.pen.forward(580)
        self.pen.right(90)
        self.pen.forward(500)
        self.pen.right(90)
        self.pen.forward(580)
        # self.pen.goto(0,0)
        # self.pen.write("Score : 0  High Score : 0", align="center",
        #           font=("candara", 24, "bold"))
        # self.pen.goto(0,210)
        # self.pen.forward(500)


class Game():
    def __init__(self):
        self.starttime = time.time()
        self.endtime = time.time()
        self.count = 3
        self.stop_flag = 0
        self.score = 0
        self.delay = 0.1
        self.high_score = 0
        # self.x = 0
        # self.y = 0
        self.wn = turtle.Screen()  ##画笔对象
        self.segments = []
        self.wn = turtle.Screen()
        self.wn.title("Snake Game")
        self.wn.bgcolor("white")
        # the width and height can be put as user's choice
        self.wn.setup(width=580, height=660)
        self.wn.tracer(0)
        self.snake = Snake()  # 蛇对象
        self.monster1 = Monster()
        self.pen1 = Pen()
        self.pen2 = Pen1()
        self.food1 = Food()
        self.keylisten()  # 设置监听
        self.Game_Start()

    def keylisten(self):
        self.wn.listen()
        self.wn.onkeypress(self.snake.group, "w")
        self.wn.onkeypress(self.snake.godown, "s")
        self.wn.onkeypress(self.snake.goleft, "a")
        self.wn.onkeypress(self.snake.goright, "d")
        self.wn.onkeypress(self.stop, " ")
    def staus_upgrade(self):
        self.pen1.pen.clear()
        self.endtime = time.time()
        time_c = int(self.endtime - self.starttime)
        # print(time_c)
        self.pen1.pen.write("Contact: {} Time: {} Motion {} ".format(
            self.score, time_c, self.snake.head.direction), align="center", font=("candara", 18, "bold"))

    def If_Over(self):
        if self.food1.food_num == 0 or self.snake.head.xcor() > 250 or self.snake.head.xcor() < -250 or self.snake.head.ycor() > 210 or self.snake.head.ycor() < -290:
            time.sleep(1)
            self.snake.head.goto(0, 0)
            self.snake.head.direction = "Stop"
            # self.snake.colors = random.choice(['black', 'blue', 'green'])
            # self.snake.shapes = random.choice(['square', 'circle'])
            for segment in self.segments:
                segment.goto(1000, 1000)
            self.segments.clear()
            self.score = 0
            self.delay = 0.1
            # self.pen1.pen.clear()
            self.pen1.pen.write("Contact: {} Time: {} Motion {} ".format(0, 0, 0), align="center",
                                font=("Arial", 24, "bold"))
            self.food1.food.clear()

            self.food1.num_array = ['1', '2', '3', '4', '5']
            self.food1.food_num = 5
            # x = random.randint(-230, 230)
            # y = random.randint(-270, 200)
            # self.food1.food.goto(x, y)
            # self.food1.num_str = random.choice(self.food1.num_array)
            # self.food1.del_num()
            # self.food1.food.write(self.food1.num_str, align="center",
            #                       font=("candara", 20, "bold"))
            self.starttime = time.time()
            self.endtime = time.time()

    def stop(self):
        self.snake.stop()
        if self.stop_flag == 1:
            self.stop_flag = 0
            return
        if self.stop_flag == 0:
            self.stop_flag = 1
            return
    def food_eated(self):
        if self.snake.head.distance(self.food1.food) < 20:
            self.food1.food.clear()
            self.food1.food_num -= 1
            print("food_num ", self.food1.food_num)
            self.If_Over()
            # print("food_num ",self.food1.food_num)
            self.score += int(self.food1.num_str)
            # if self.score > self.high_score:
            #     self.high_score = self.score
            # Adding segment
            if len(self.segments)>0:
                x = self.segments[len(self.segments) - 1].xcor()
                y = self.segments[len(self.segments) - 1].ycor()
            else :
                x = self.snake.head.xcor()
                y = self.snake.head.ycor()
            for i in range(int(self.food1.num_str)):
                new_segment = turtle.Turtle()
                new_segment.speed(0)
                new_segment.shape("square")
                # new_segment.color(
                #     "black")  # tail colour
                new_segment.color(random.choice(["green","red","blue","black","yellow"]))
                new_segment.penup()
                # new_segment.setx(x)
                # new_segment.sety(y)
                new_segment.goto(x,y)
                self.segments.append(new_segment)
            print("len seg", len(self.segments))
            x = random.randint(-230, 230)
            y = random.randint(-270, 200)
            self.food1.food.goto(x, y)
            self.food1.num_str = random.choice(self.food1.num_array)
            self.food1.del_num()
            self.food1.food.write(self.food1.num_str, align="center",
                                  font=("candara", 20, "bold"))
            self.delay -= 0.001
            self.staus_upgrade()
    def grow(self):
        ##身体第一块跑向头
        if len(self.segments) > 0:
            x = self.snake.head.xcor()
            y = self.snake.head.ycor()
            self.segments[0].goto(x, y)
        for index in range(len(self.segments)-1 , 0, -1):
            # for index in range(0,len(self.segments)-1, 1):
            x = self.segments[index - 1].xcor()
            y = self.segments[index - 1].ycor()
            self.segments[index].goto(x, y)
        if len(self.segments) > 0:
            x = self.snake.head.xcor()
            y = self.snake.head.ycor()
            self.segments[0].goto(x, y)
        #     time.sleep(0.001)
        # for index in range(0,len(self.segments) - 1, 1):
        #     # for index in range(0,len(self.segments)-1, 1):
        #     x = self.segments[index].xcor()
        #     y = self.segments[index].ycor()
        #     self.segments[index+1].goto(x, y)
        #     time.sleep(0.001)
            # self.snake.move()
    def chase(self):
        x= self.snake.head.xcor()
        y= self.snake.head.ycor()
        x1= self.monster1.monster.xcor()
        y1= self.monster1.monster.ycor()
        # if abs(y1-y) > abs(x1-x):
        #     if y1 < y:
        #         self.monster1.monster.sety(y1 + 20)
        #     else:
        #         self.monster1.monster.sety(y1 - 20)
        # else:
        #     if x1 < x:
        #         self.monster1.monster.setx(x1 + 20)
        #     else:
        #         self.monster1.monster.setx(x1 - 20)
        # self.wn.tracer(n=5, delay=0)
        if abs(y1-y) > abs(x1-x):
            if y1 < y:
                self.monster1.monster.seth(90)
                self.monster1.monster.forward(20)
            else:
                self.monster1.monster.seth(270)
                self.monster1.monster.forward(20)
        else:
            if x1 < x:
                self.monster1.monster.seth(0)
                self.monster1.monster.forward(20)
            else:
                self.monster1.monster.seth(180)
                self.monster1.monster.forward(20)
    def Game_Start(self):
        # while True:
        # self.wn.ontimer(self,)
        # self.monster1.chase(self.snake.head)

        # self.monster1.monster.speed(5)
        self.count -= 1
        if self.count == 0:
            self.count = 3
            self.chase()
        self.wn.update()
        ##游戏结束
        self.If_Over()
        self.food_eated()
        # len(self.segments)
        self.grow()
        self.snake.move()
        # Checking for head collisions with body segments
        for segment in self.segments:
            if segment.distance(self.snake.head) < 20:
                time.sleep(1)
                self.snake.head.goto(0, 0)
                self.snake.head.direction = "stop"
                self.colors = random.choice(['red', 'blue', 'green'])
                self.shapes = random.choice(['square', 'circle'])
                for segment in self.segments:
                    segment.goto(1000, 1000)
                segment.clear()
                self.score = 0
                self.delay = 0.1
                # self.staus_upgrade()
                # self.pen1.pen.clear()
                # self.endtime = time.time()
                # time_c = int(self.endtime-self.starttime)
                # print(time_c)
                # self.pen1.pen.write("Score : {} High Score : {}  Time: {}".format(
                #     self.score, self.high_score, time_c), align="center", font=("candara", 24, "bold"))
        self.staus_upgrade()
        self.wn.ontimer(self.Game_Start, 100)


if __name__ == "__main__":
    game = Game()
    game.wn.mainloop()
