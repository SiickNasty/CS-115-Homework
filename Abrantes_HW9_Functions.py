"""
      Nathan Abrantes
      Homework 9
      12 March 2025
"""

import pygame
from pygame.constants import KEYDOWN
from pygame.display import update
import Helper_Functions # Imports functions from other file
import time

# init pygame
pygame.init()

# window dimensions
width = 1000
height = 850
screen = pygame.display.set_mode((width,height))

# Set window title
pygame.display.set_caption("Snek")

# FPS 
clock = pygame.time.Clock()
dt = 0 
speed = 10 

# Create font
system_fonts = pygame.font.get_fonts()
print(system_fonts)
my_font = pygame.font.SysFont(system_fonts[0], size=48, bold=True, italic=False)
score = 0

# Frog current position
cur_pos = [485,790]
direction = "up"

# Cars coordinates
lightning_car_coords = [[225,520], [230,560], [250,540], [260,570]]
Square_car_coords = [350,715]
triangle_coords = [[100,590], [100,640], [200,615]]
ellipse_coords = [655, 655]
truck_coords = [[500,460], [120,50]]

""" Game loop """
running = True 
while running:
  
  """ Handle events """
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
         running = False
    if event.type == KEYDOWN:
        if event.key == pygame.K_ESCAPE: # escape key
            running = False

          # Movement of the frog, use WASD! 
        if event.key == pygame.K_w: # up direction (w)
              cur_pos[1] -= 20    #y-coor
        if event.key == pygame.K_s: # down direction (s)
              cur_pos[1] += 20    #y-coor
        if event.key == pygame.K_a: # left direction (a)
              cur_pos[0] -= 20    # x-coor
        if event.key == pygame.K_d: # right direction (d)
              cur_pos[0] += 20    # x-coor

  # automatic movement of cars
  if direction == "up":
    lightning_car_coords[0][0] -= 10
    lightning_car_coords[1][0] -= 10
    lightning_car_coords[2][0] -= 10
    lightning_car_coords[3][0] -= 10
    Square_car_coords[0] += 10
    triangle_coords[0][0] += 10
    triangle_coords[1][0] += 10
    triangle_coords[2][0] += 10
    ellipse_coords[0] -= 10
    truck_coords[0][0] += 10

  # cars bounce back to create the illusion that they go on forever
  if ellipse_coords[0] < 0:
    ellipse_coords[0] += 1000 

  if lightning_car_coords[0][0] < 0:
    lightning_car_coords[0][0] += 1000 
    lightning_car_coords[1][0] += 1000
    lightning_car_coords[2][0] += 1000
    lightning_car_coords[3][0] += 1000

  if Square_car_coords[0] > 1000:
    Square_car_coords[0] = 0

  if triangle_coords[0][0] > 1100:
    triangle_coords[0][0] = 0 
    triangle_coords[1][0] = 0
    triangle_coords[2][0] = 100 

  if truck_coords[0][0] > 1000:
    truck_coords[0][0] = 0

  """ Update game state"""

  # boundaries of screen
  if cur_pos[0] < 0: # x-direction boundaries
    cur_pos[0] = 0 

  if cur_pos[0] > width-20:  
    cur_pos[0] = width-20

  if cur_pos[1] < 0: # y-direction boundaries
    cur_pos[1] = 0

  if cur_pos[1] > height-20:
    cur_pos[1] = height-20

  # Identifying the shapes/cars
  square_car = pygame.Rect(Square_car_coords[0], Square_car_coords[1], 50,50)
  frog = pygame.Rect(cur_pos[0], cur_pos[1], 50, 50)
  semi_truck = pygame.Rect(truck_coords[0], truck_coords[1])

  """ Draw screen """
  # Clear screen
  screen.fill("white")

  # Draw start area
  pygame.draw.rect(screen, "purple", pygame.Rect((0,775), (1000,75)))

  # Draw win area before water section 
  pygame.draw.rect(screen, "purple", pygame.Rect((0,375), (1000,75)))

  # Draw water
  pygame.draw.rect(screen, "blue", pygame.Rect((0,0), (1000,375)))

  # Draw road
  pygame.draw.rect(screen, "black", pygame.Rect((0,450), (1000,325)))

  # Draw frog
  pygame.draw.rect(screen, "green", frog)

  # Draw square car
  pygame.draw.rect(screen, "red", square_car)

  # Draw lightning car
  pygame.draw.polygon(screen, "violet", lightning_car_coords)

  # Draw triangle car
  pygame.draw.polygon(screen, "cyan", triangle_coords)

  # Draw ellipse car
  pygame.draw.ellipse(screen, "yellow", pygame.Rect(ellipse_coords, (80,50)))

  # Draw semi truck
  pygame.draw.rect(screen, "white", semi_truck)

  # Collision between frog and square car
  if square_car.colliderect(frog):
     Helper_Functions.draw_text(f"You Lose! Score: {score}", (350,375), "white", my_font, screen)

  if semi_truck.colliderect(frog):
     Helper_Functions.draw_text(f"You Lose! Score: {score}", (350,375), "white", my_font, screen)

  Helper_Functions.draw_text(f"Score", (435,0), "white", my_font, screen)
  Helper_Functions.draw_text(f"{score}", (480,40), "red", my_font, screen)     

  if cur_pos[1] < 400:  
     screen.fill("green")
     score += 1
     Helper_Functions.draw_text(f"You win! Score: {score}", (350,375), "blue", my_font, screen)

  if cur_pos[1] < 400:
     time.sleep(3)
     cur_pos = [485,790]
     
  # Update screen
  pygame.display.flip()
  
  # FPS
  dt = clock.tick(speed)/1000

# End game
pygame.QUIT()