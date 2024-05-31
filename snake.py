from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180
class Snake:

    def __init__(self) :
        self.snake_blocks = []
        self.create_snake()
        self.head = self.snake_blocks[0]


    def create_snake(self):
        for positions in STARTING_POSITIONS:
             self.add_sblock(positions)


    def add_sblock(self, positions):
            new_sblock = Turtle("square")
            new_sblock.color("white")
            new_sblock.penup()
            new_sblock.goto(positions)
            self.snake_blocks.append(new_sblock)

    def extend(self):
         self.add_sblock(self.snake_blocks[-1].position())
        
    def move(self):
            for i in range(len(self.snake_blocks)-1, 0, -1): #Last block take the position of second last block.
                new_x = self.snake_blocks[i-1].xcor()
                new_y = self.snake_blocks[i-1].ycor()
                self.snake_blocks[i].goto(new_x, new_y)
            self.head.forward(MOVE_DISTANCE)


    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)


    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)    


    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)   


    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)   
