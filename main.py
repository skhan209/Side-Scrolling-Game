#!/bin/python3

import turtle
import math
import random
import time

#Object Dictionaries 

player = {"name": "Player", "turtle" : turtle.Turtle(), "shape":"Fruit_blueberry.png","radius":5,"move_distance" : 5,"lives":4,"score":-10 }
enemy = {"name": "Enemy", "turtle" : turtle.Turtle(), "shape":"zombie_pom.png","radius":35, "move_distance" : 2 }
benefit_obj = {"name": "Benefit_object", "turtle" : turtle.Turtle(), "shape":"ben_obj.png","radius":22, "move_distance" : 6 }
score_pen = {"name": "Score", "turtle" : turtle.Turtle()}
player_life_pen = {"name": "Lives", "turtle" : turtle.Turtle()}
splash_screen = {"name": "Splash_screen", "turtle" : turtle.Turtle()}
screen_stamps = {"name": "Splash stamp objects", "turtle" : turtle.Turtle(), "shape":"blueberry.png", "shape2":"zombie_pomegranate.png","shape3":"powerup.png" }




#Creating the START Screen 

#Sets up start screen's color and screen size

screen = splash_screen["turtle"].getscreen()
screen.setup(width=500,height= 500)
screen.bgcolor("black")
t1 = splash_screen["turtle"]




#USED THE FOLLOWING SOURCE FOR THE START SCREEN:
# #https://github.com/wynand1004/Projects/blob/master/Space%20Arena/space_arena.py


#Function uses turtle to draw numbers/charcers 
def draw_character(character,color,size, x, y):
  t1.speed(0)
  t1.penup()
  t1.pencolor(color)
  t1.pensize(size)
  t1.pendown()
  
  #Draws the character
  characters = {}
  characters["1"] = ((-5, 10), (0, 10), (0, -10), (-5, -10), (5, -10))
  characters["2"] = ((-5, 10),(5, 10),(5, 0), (-5, 0), (-5, -10), (5, -10))
  characters["A"] = ((-5, -10), (-5, 10), (5, 10), (5, -10), (5, 0), (-5, 0))
  characters["B"] = ((-5, -10), (-5, 10), (3, 10), (3, 0), (-5, 0), (5,0), (5, -10), (-5, -10))
  characters["C"] = ((5, 10), (-5, 10), (-5, -10), (5, -10))
  characters["D"] = ((-5, 10), (-5, -10), (5, -8), (5, 8), (-5, 10))
  characters["E"] = ((5, 10), (-5, 10), (-5, 0), (0, 0), (-5, 0), (-5, -10), (5, -10))
  characters["F"] = ((5, 10), (-5, 10), (-5, 0), (5, 0), (-5, 0), (-5, -10))
  characters["G"] = ((5, 10), (-5, 10), (-5, -10), (5, -10), (5, 0), (0, 0))
  characters["H"] = ((-5, 10), (-5, -10), (-5, 0), (5, 0), (5, 10), (5, -10))
  characters["I"] = ((-5, 10), (5, 10), (0, 10), (0, -10), (-5, -10), (5, -10))
  characters["J"] = ((5, 10), (5, -10), (-5, -10), (-5, 0))   
  characters["K"] = ((-5, 10), (-5, -10), (-5, 0), (5, 10), (-5, 0), (5, -10))
  characters["L"] = ((-5, 10), (-5, -10), (5, -10))
  characters["M"] = ((-5, -10), (-3, 10), (0, 0), (3, 10), (5, -10))
  characters["N"] = ((-5, -10), (-5, 10), (5, -10), (5, 10))
  characters["O"] = ((-5, 10), (5, 10), (5, -10), (-5, -10), (-5, 10))
  characters["P"] = ((-5, -10), (-5, 10), (5, 10), (5, 0), (-5, 0))
  characters["Q"] = ((5, -10), (-5, -10), (-5, 10), (5, 10), (5, -10), (2, -7), (6, -11))
  characters["R"] = ((-5, -10), (-5, 10), (5, 10), (5, 0), (-5, 0), (5, -10))
  characters["S"] = ((5, 8), (5, 10), (-5, 10), (-5, 0), (5, 0), (5, -10), (-5, -10), (-5, -8))
  characters["T"] = ((-5, 10), (5, 10), (0, 10), (0, -10)) 
  characters["V"] = ((-5, 10), (0, -10), (5, 10)) 
  characters["U"] = ((-5, 10), (-5, -10), (5, -10), (5, 10)) 
  characters["W"] = ((-5, 10), (-3, -10), (0, 0), (3, -10), (5, 10))   
  characters["Y"] = ((-5, 10), (0, 0), (5, 10), (0,0), (0, -10)) 
  characters["X"] = ((-5, 10), (5, -10), (0, 0), (-5, -10), (5, 10))
  characters["Z"] = ((-5, 10), (5, 10), (-5, -10), (5, -10))
  
  
  character = character.upper()
 
  # statement that finds and writes the character
  if character in characters:
    t1.penup()
    xy = characters[character][0]
    t1.goto(x+xy[0]*size, y +xy[1]*size)
    t1.pendown()
   
    for i in range(1,len(characters[character])):
      xy = characters[character][i]
      t1.goto(x+xy[0]*size, y +xy[1]*size)
    t1.penup()
    
  t1.hideturtle()
 
#function that writes an entire string/sentence instead of one character 
def draw_string(str,color,size,x, y):
  # Center text
  x -= 15 * size * ((len(str)-1) / 2)
  for character in str:
    draw_character(character,color,size, x, y)
    x += 15 *size    



#function that draws the startscreen, includes directions for the player
def draw_startscreen():
  
   #draws the title for the game
   draw_string("The Walking Fruit","light green",1.6,0,210)
   
   #Uses the image from the image gallery to show the player their character
   #Displays "player"
   #Displays blueberry
   screen = screen_stamps["turtle"].getscreen()
   screen.addshape("blueberry.png")
   screen_stamps["turtle"].shape(screen_stamps["shape"])
   t1 = screen_stamps["turtle"]
   t1.hideturtle()
   t1.penup()
   t1.goto(-200,135)
   t1.stamp()
   draw_string("Player","light green",1.0,-170,100)
   
   
   
   
   #Uses the image from the image gallery to show the player their enemy
   #Displays "ENEMY"
   #Displays zombie pomegrante
   screen = screen_stamps["turtle"].getscreen()
   screen.addshape("zombie_pomegranate.png")
   screen_stamps["turtle"].shape(screen_stamps["shape2"])
   t2 = screen_stamps["turtle"]
   t2.hideturtle()
   t2.penup()
   t2.goto(20,130)
   t2.stamp()
   draw_string("Enemy","light green",1.0,-5,100)
   
  
  
  
   #Uses the image from the image gallery to show the player their powerup/benefit object
   #Displays "POWERUP/BENEFIT"
   #Displays "cure"
   screen = screen_stamps["turtle"].getscreen()
   screen.addshape("powerup.png")
   screen_stamps["turtle"].shape(screen_stamps["shape3"])
   t3 = screen_stamps["turtle"]
   t3.hideturtle()
   t3.penup()
   t3.goto(170,160)
   t3.stamp()
   
   
   
   
   
   #Writes and displays instructions to the player
   draw_string("Powerup","light green",1.0,160,100)
   draw_string("Up Arrow","light green",1.0,-160,40)
   draw_string("Go up","light green",1.0,145,40)
   draw_string("Down Arrow","light green",1.0,-145,-20)
   draw_string("Go Down","light green",1.0,160,-20)
   draw_string("Beware of zombified fruit","#ff0000",1.0,-25,-80)
   draw_string("Press Space to start","light green",1.0,-25,-140)
  
   screen.tracer(0)
   screen.update()
   
  
#calls function to display start screen   
draw_startscreen()




#Function that writes and displays gameover message when player loses all 3 lives
def draw_gameoverscreen():
   draw_string("GAMEOVER","red ",3,0,160)
   screen.tracer(0)
   screen.update()
   t1.hideturtle()




# Player Up & Down Functions
def up():
  r1 = 10
  height = 500
  t2 = player["turtle"] # for convenience
  t2.penup()
  t2.tracer(0)
  t2.clear()
  current_y = t2.ycor()
 # adds the player's move distance to the current 
 #allows player to move up
  
  
  t2.sety(player["move_distance"] + current_y)
  #restricts the player from going off the screen when going up
  if (t2.ycor() > (height/2) + (r1)):
    t2.sety((height/2) + (r1))
    #If player tries to go off the screen when going up this sets the player back
    t2.sety((50))
  t2.update()
  t2.clear()
  

def down():
  r1 = 10
  height = 400
  t2 = player["turtle"] #for convenience
  t2.penup()
  t2.tracer(0)
  t2.clear()
  current_y = t2.ycor()
  # subtracts the player's move distance to the current 
 #allows player to move down
 
 
  t2.sety(player["move_distance"] * -1 + current_y)
   #restricts the player from going off the screen when going down
  if (t2.ycor() < -(height/2)+ (r1)):
    t2.sety((height/2) - (r1))
    #If player tries to go off the screen when going down this sets the player back 
    t2.sety((100))
  t2.update()
  t2.clear()

#USED THE FOLLOWING SOURCE:
# #https://github.com/wynand1004/Projects/blob/master/Space%20Arena/space_arena.py
#This function uses game_state as a global variable that changes the game from the start screen to the game screen 
def start_game():
    global game_state
    game_state = "game"



# Keyboard Bindings
screen.onkey(up, "Up")#player moves up
screen.onkey(down, "Down")#player moves down
screen.onkey(start_game, "Space")#starts the game
screen.listen()

game_state = "start_screen"



#collision test for player and enemy 
def collision_test(player, enemy):
  collision_detected = False;
  
     #implement collision detection 
    #https://developer.mozilla.org/en-US/docs/Games/Techniques/2D_collision_detection

  x_dist = (enemy["turtle"].xcor())-(player["turtle"].xcor())
  y_dist = (enemy["turtle"].ycor())-(player["turtle"].ycor())
  distance = math.sqrt((x_dist*x_dist) + (y_dist*y_dist))
  total_radius = (player["radius"] + enemy["radius"])
  
  if(distance <  total_radius):
    collision_detected = True;
  
  return collision_detected;




#collisin test for player and benefit object 
def collision_test(player, benefit_obj):
  collision_detected = False;
 
  #implement collision detection 
    #https://developer.mozilla.org/en-US/docs/Games/Techniques/2D_collision_detection
 
  x_dist = (benefit_obj ["turtle"].xcor())-(player["turtle"].xcor())
  y_dist = (benefit_obj ["turtle"].ycor())-(player["turtle"].ycor())
  distance = math.sqrt((x_dist*x_dist) + (y_dist*y_dist))
  total_radius = (player["radius"] + benefit_obj["radius"])
  
  if(distance <  total_radius):
    collision_detected = True;
  return collision_detected;
  



 #USED THE FOLLOWING SOURCE:
#https://stackoverflow.com/questions/55009976/python-turtle-collision-help-and-updating-score-lives
 
#Draws and displays the player's score
def draw_score():
    t4.undo()
    t4.write("Score: {}".format(player['score']), font=("Arial", 15, "normal"))
    

t4 = score_pen["turtle"]    
t4.speed(0)
t4.hideturtle()
t4.penup()
t4.goto(-210, 200)
t4.color("white")
t4.write("Score: {}".format(player['score']), font=("Arial", 14, "normal"))
  

#Draws and displays the player's lives
def draw_lives():
    t5.undo()
    t5.write("Lives: {}".format(player['lives']),  font=("Arial", 15, "normal"))


t5 = player_life_pen["turtle"]
t5.speed(0)
t5.hideturtle()
t5.penup()
t5.goto(-210, 223)
t5.color("white")
t5.write("Lives: {}".format(player['lives']), font=("Arial", 15, "normal"))


# Main Game Loop

def main():
  r1 = 25 #radius for enemy
  width = 500
  while True:
        
    # Clears the screen
    screen = splash_screen["turtle"].getscreen()
    screen.update()
    
  
    # When the game is at the start screen it removes the score and lives displayed
    if game_state == "start_screen":
       
       t4 = score_pen["turtle"]
       t5 = player_life_pen["turtle"]
       t4.hideturtle
       t4.clear()
       t5.hideturtle()
       t5.clear()
       screen.update()
       
   
   
     #when the game starts it displays the game background and characters   
   
    elif game_state == "game":
       #removes the images that were used on the start screen
       t8 = screen_stamps["turtle"]
       t8.clear()
       t1.clear()
       
       #Adds the character's player
       screen = player["turtle"].getscreen() 
       screen.bgpic("backgroun.jpeg")
       screen.addshape("Fruit_blueberry.png")
       player["turtle"].shape(player["shape"])
       
       #Adds the character's benefit object 
       screen = benefit_obj["turtle"].getscreen()
       screen.addshape("ben_obj.png")
       benefit_obj["turtle"].shape(benefit_obj["shape"])
       
       #Adds the character's enemy
       screen = enemy["turtle"].getscreen()
       screen.addshape("zombie_pom.png")
       enemy["turtle"].shape(enemy["shape"])
       
       #for convenience 
       t2 = player["turtle"]
       t3 = enemy["turtle"]
       t4 = score_pen["turtle"]
       t5 = player_life_pen["turtle"]
       t6 = benefit_obj["turtle"]
      
       
       t3.penup()
       t3.tracer(0)
       t3.clear()
       t2.penup()
       t6.penup()
     
       
     
     
      #HARM OBJECT
      #sets edge condition for enemy
       
       t3.setx(t3.xcor() - 1) #moves the enemy across the x-axis 
       if(t3.xcor() <= -(width/2) - (r1)):
         t3.setx((width/2) + (r1))
        #Gives randome y values 
         t3.sety(random.randint(-200,250))
         t3.update() #check this line again
      
    
       #player_life(lives)
       if collision_test(player, enemy):
        player["lives"] -=1 #reduces player's life by 1 when colliding with enemy
        
        #sets starting position for the player, harm and benefit object
        #set in close proximity because the draw lives and draw score start when the player collides with these objects 
        #Allows for early collison to start the player having 3 lives and a score of 0
        t2.setposition(-200,-140)
        t3.setposition(-300,50)#also moves the object when colliding to remove decreasing lives
        t6.setposition(-200,-140)
       
        #update player's life
        t5.clear()
        draw_lives()
         
     
     
     
      #BENEFIT OBJECT
      #sets edge condition
       r1 = 5
       t6.setx(t6.xcor() - 1) #moves the benefit object across the x-axis 
       if (t6.xcor() <= -(width/2) - (r1)):
          t6.setx((width/2) + (r1))
         #Gives random y values 
          t6.sety(random.randint(-200,300))
       t6.update()
         
      #updates score for player
       if collision_test(player, benefit_obj):
           player["score"] += 10 #increases score by 10 when colliding with benefit object
           t2.penup()
           t6.setposition(300,200) #moves the object when colliding to remove increasing score
           t4.clear()#prevents score from being overwritten
           draw_score() #updates the score
    
      
      
       #when player reaches 0 lives 
       #displays gamover message 
       if player["lives"] == 0:
          draw_gameoverscreen()
          #removes all objects off screen
          t1.hideturtle()
          t2.hideturtle()
          t3.hideturtle()
          t4.hideturtle()
          t5.hideturtle()
          t6.hideturtle()
          t1.clear()
          t2.clear()
          t3.clear()
          t4.clear()
          t5.clear()
          t6.clear()
          screen.update()
          screen.tracer(0)
          t5.done() 
       
      
      
      
         
          
        
          
 
    # Update the screen
 
    screen.update()
    
#calls the main function    
main()


