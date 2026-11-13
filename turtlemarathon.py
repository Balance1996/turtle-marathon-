from turtle import Turtle,Screen
import random
screen=Screen()
screen.setup(width=500,height=400)
rand_bet=screen.textinput("Turtle Marathon Race","Place your bet on which turtle color wins:")


contestant_tag=["red","orange","yellow","green","blue","purple"]

turtle_location=[(-230,-100), (-230,-50),(-230,-20),(-230,30),(-230,90),(-230,150)]

paired=list(zip(contestant_tag,turtle_location))
all_racers=[]
for contestant_tag,turtle_location in paired:
    Racer=Turtle(shape="turtle")
    all_racers.append(Racer)
    Racer.penup()
    Racer.color(contestant_tag)
    Racer.goto(turtle_location[0],turtle_location[1])
print(all_racers)
#draw vertical finish line from north to south
finish_line = Turtle()
finish_line.penup()
finish_line.goto(200, -180)
finish_line.setheading(90)
finish_line.pendown()
finish_line.forward(360)
#getting winner turtle
no_winner=True
while no_winner:
    for racer in all_racers:
        random_pace=random.randint(1,10)
        racer.forward(random_pace)
        if racer.xcor()>230:
            winner_color=racer.pencolor()
            print(f'The winner turtle is {winner_color}.')
            no_winner=False


screen.exitonclick()