from ship import Ship
from turtle import Screen
from invaders import Invader
from blaster import Blaster
from deathray import Deathray
from scoreboard import Score
from random import choice
import time
# from tkinter import *

deathray_clock = 3
new_wave_clock = 20

# window = Tk()
# label = Label(text='Select difficulty (easy, medium, hard, or impossible)')
# label.grid(column=0, row=0)
# difficulty_input = Entry()
# difficulty_input.grid(column=0, row=1)
# difficulty = difficulty_input.get()
#
# window.mainloop()

difficulty = input("Select difficulty (easy, medium, hard, or impossible): ").lower()

if difficulty == 'easy':
    new_wave_clock = 20
    deathray_clock = 5

elif difficulty == 'medium':
    new_wave_clock = 15
    deathray_clock = 2

elif difficulty == 'hard':
    new_wave_clock = 15
    deathray_clock = 1

elif difficulty == 'impossible':
    new_wave_clock = 15
    deathray_clock = .1

else:
    print('That is not a valid input')
    difficulty = input('Select difficulty (easy, medium, hard, or impossible): ').lower()

speed = 0.02
banishment = 900
start_time = time.time()
new_wave_time = time.time()

# Creates and sets up the game screen
screen = Screen()
rootwindow = screen.getcanvas().winfo_toplevel()
rootwindow.call('wm', 'attributes', '.', '-topmost', '1')
rootwindow.call('wm', 'attributes', '.', '-topmost', '0')
screen.setup(height=800, width=900)
screen.bgcolor('black')
screen.title("Invaders from SPAAAAAACE!")
screen.tracer(0)
screen.listen()


# This function creates and keeps track of all the lasers coming from the user's ship
def create_blast():
    blast = Blaster()
    blast.setposition(ship.xcor(), ship.ycor())
    blast_list.append(blast)


# This function creates and keeps track of all the lasers coming from the alien ships
def create_deathray():
    threat = choice(invader_list)
    death = Deathray()
    deathray_list.append(death)
    death.setposition(x=threat.xcor(), y=threat.ycor())


# Creates the necessary instances
ship = Ship()
ship.setposition(0, -200)
score = Score()

# These lists organize their respective instances
blast_list = []
deathray_list = []
invader_list = []


# Creates a wave of invader ships
def new_wave():
    x_pos = -300
    y_pos = 350
    for n in range(29):
        invader = Invader()
        if n % 15 == 0 and n != 0:
            x_pos = -280
            y_pos -= 50
        invader.setposition(x=x_pos, y=y_pos)
        x_pos += 35
        invader_list.append(invader)


new_wave()

# Determines game controls
screen.onkeypress(ship.move_right, 'Right')
screen.onkeypress(ship.move_left, 'Left')
screen.onkeypress(ship.move_up, 'Up')
screen.onkeypress(ship.move_down, 'Down')
screen.onkeypress(create_blast, 'space')


game_on = True
while game_on:
    screen.update()
    time.sleep(speed)

    # Determines the movement of the invaders
    for inv in invader_list:
        if inv.ycor() < -380:
            game_on = False
            score.game_over()
        if inv.xcor() > 320 or inv.xcor() < -320:
            for vader in invader_list:
                vader.bounce_x()

        # Game ends if ship hits invader
        if inv.distance(ship) < 10:
            game_on = False
            score.game_over()
        inv.move()

    # Moves the user's laser blasts and removes the blast and invader if they collide
    for bl in blast_list:
        bl.move()
        for inv in invader_list:
            if bl.distance(inv) < 20:
                bl.reset()
                bl.setposition(x=300, y=banishment)
                blast_list.remove(bl)
                banishment += 50
                inv.reset()
                inv.setposition(x=300, y=banishment)
                invader_list.remove(inv)
                banishment += 50
    current_time = time.time()

    # Determines if it is time for an enemy ship to fire a deathray
    if current_time - start_time > deathray_clock:
        create_deathray()
        start_time = current_time

    # Determines if it is time for the next wave of enemies
    if current_time - new_wave_time > new_wave_clock:
        new_wave()
        new_wave_time = current_time

    # Removes rays and blasts if they collide
    for ray in deathray_list:
        ray.move()
        for bl in blast_list:
            if ray.distance(bl) < 20:
                bl.reset()
                bl.setposition(x=300, y=banishment)
                blast_list.remove(bl)
                banishment += 50
                ray.reset()
                ray.setposition(x=300, y=banishment)
                deathray_list.remove(ray)

        # Ends game if user ship is hit with deathray
        if ray.distance(ship) < 20:
            game_on = False
            score.game_over()

        # Ends game if there are no more invaders
        if not invader_list:
            game_on = False
            score.win()

screen.exitonclick()

# TODO: Class for game animations
# TODO: Make cooldown period for blaster
# TODO: Make difficulty levels
