from turtle import Turtle

class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("C:\Workspace\Python\snake_game\data.txt") as data:
            self.high_score = int(data.read())
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 280)
        self.display_score()

    def display_score(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", move = False, align = "center", font = ("Courier", 16, "bold"))
    
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("C:\Workspace\Python\snake_game\data.txt", 'w') as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.display_score()
        
    def update_score(self):
        self.score += 1
        self.display_score()