import turtle
import time
import random
# global x, y
class Snake():
    def __init__(self):

        self.head = turtle.Turtle()
        self.head.shape("square")
        self.head.color("red")
        self.head.penup()
        self.head.goto(0, 0)
        self.head.direction = "Stop"
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
class Food1():
    # food in the game
    def __init__(self):
        self.food = turtle.Turtle()
        self.colors = random.choice(['red', 'green', 'black'])
        self.shapes = random.choice(['square', 'triangle', 'circle'])
        self.food.speed(0)
        self.food.shape(self.shapes)
        self.food.color(self.colors)
        food.hideturtle()
        self.food.penup()
        self.food.goto(0, 100)
class Food():
    def __init__(self):
        self.num_array = ['1', '2', '3', '4', '5']
        self.num_str =random.choice(self.num_array)
        self.food = turtle.Turtle()
        self.food.speed(0)
        self.food.shape("square")
        self.food.color("black")
        self.food.penup()
        self.food.hideturtle()#隐藏笔迹
        self.food.goto(0, 100)
        self.food.write(self.num_str, align="center",
                  font=("candara", 24, "bold"))
        self.food_num = 5
        self.del_num()
    def del_num(self):
        ##关键代码，解决无法删除列表中某个值的问题
        if len(self.num_array)>0 :
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
        self.pen.hideturtle()#隐藏笔迹
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
        self.pen.hideturtle()#隐藏笔迹
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
        self.score = 0
        self.delay = 0.1
        self.high_score = 0
        # self.x = 0
        # self.y = 0
        self.wn = turtle.Screen()##画笔对象
        self.segments = []
        self.wn = turtle.Screen()
        self.wn.title("Snake Game")
        self.wn.bgcolor("white")
        # the width and height can be put as user's choice
        self.wn.setup(width=580, height=660)
        self.wn.tracer(0)
        self.snake = Snake()#蛇对象
        self.pen1 = Pen()
        self.pen2 = Pen1()
        self.food1 = Food()
        self.keylisten()#设置监听
        self.Game_Start()

    def keylisten(self):
        self.wn.listen()
        self.wn.onkeypress(self.snake.group, "w")
        self.wn.onkeypress(self.snake.godown, "s")
        self.wn.onkeypress(self.snake.goleft, "a")
        self.wn.onkeypress(self.snake.goright, "d")

    # def erasableWrite(tortoise, name, font, align, reuse=None):
    #     eraser = turtle.Turtle() if reuse is None else reuse
    #     eraser.hideturtle()
    #     eraser.up()
    #     eraser.setposition(tortoise.position())
    #     eraser.write(name, font=font, align=align)
    #     return eraser
    def If_Over(self):
        if self.food1.food_num == 0 or  self.snake.head.xcor() > 250 or self.snake.head.xcor() < -250 or self.snake.head.ycor() > 210 or self.snake.head.ycor() < -290:
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
            self.pen1.pen.clear()
            self.pen1.pen.write("Score : {} High Score : {} ".format(self.score, self.high_score), align="center",
                                font=("Arial", 24, "bold"))
            self.food1.num_array = ['1', '2', '3', '4', '5']
            self.food1.food_num = 5
    def Game_Start(self):
        # while True:
            # self.wn.ontimer(self,)
        self.wn.update()
        ##游戏结束
        self.If_Over()
        if self.snake.head.distance(self.food1.food) < 20:
            self.food1.food.clear()
            self.food1.food_num -= 1
            print("food_num ",self.food1.food_num)
            self.If_Over()
            # print("food_num ",self.food1.food_num)
            x = random.randint(-250, 250)
            y = random.randint(-290, 210)
            self.food1.food.goto(x, y)
            self.food1.num_str= random.choice(self.food1.num_array)
            self.food1.del_num()
            self.food1.food.write(self.food1.num_str, align="center",
                            font=("candara", 24, "bold"))
            # Adding segment
            new_segment = turtle.Turtle()
            new_segment.speed(0)
            new_segment.shape("square")
            new_segment.color("black")  # tail colour
            new_segment.penup()
            self.segments.append(new_segment)
            self.delay -= 0.001
            self.score += 10
            if self.score > self.high_score:
                self.high_score = self.score
            self.pen1.pen.clear()
            self.pen1.pen.write("Score : {} High Score : {} ".format(
                self.score, self.high_score), align="center", font=("candara", 24, "bold"))
        # Checking for head collisions with body segments
        for index in range(len(self.segments) - 1, 0, -1):
            x = self.segments[index - 1].xcor()
            y = self.segments[index - 1].ycor()
            self.segments[index].goto(x, y)
        if len(self.segments) > 0:
            x = self.snake.head.xcor()
            y = self.snake.head.ycor()
            self.segments[0].goto(x, y)
        self.snake.move()
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
                self.pen1.pen.clear()
                self.pen1.pen.write("Score : {} High Score : {} ".format(
                    self.score, self.high_score), align="center", font=("candara", 24, "bold"))

        self.wn.ontimer(self.Game_Start  , 100)

if __name__ == "__main__":
    game = Game()
    game.wn.mainloop()