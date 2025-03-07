"""
      Nathan Abrantes
      Homework 8
      03 March 2025 
"""

import pygame
from pygame.constants import KEYDOWN
from pygame.display import update

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

# Frog current position
cur_pos = [500,812]
direction = "up"

# Cars coordinates
lightning_car_coords = [[230,520], [230,560], [250,540], [260,570]]
# for loop, update x pos for coordinate in lightning car coords

Square_car_coords = [350,715]

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

        
  if direction == "up":
    lightning_car_coords[0][0] += 100

  if direction == "up":
    Square_car_coords[0] += 20

  """ Update game state"""

  # boundaries of screen
  if cur_pos[0] < 0: # x-direction boundaries
    cur_pos[0] = 0 
    # running = False
  if cur_pos[0] > width-20:  
    cur_pos[0] = width-20
    # running = False

  if cur_pos[1] < 0: # y-direction boundaries
    cur_pos[1] = 0
    # running = False
  if cur_pos[1] > height-20:
    cur_pos[1] = height-20
    # running = False

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
  pygame.draw.circle(screen, "green", cur_pos, 25)

  # Draw square car
  pygame.draw.rect(screen, "red", pygame.Rect(Square_car_coords[0], Square_car_coords[1], 50,50))
  # pygame.draw.rect(screen, "red", pygame.Rect((350,715), (50,50)))
  
  # Draw lightning car
  pygame.draw.polygon(screen, "violet", lightning_car_coords[0][0], lightning_car_coords[1][1])
  # [[230,520], [230,560], [250,540], [260,570]]

  # Draw triangle car
  pygame.draw.polygon(screen, "cyan", ((100,600), (100,650), (200,625)))

  # Draw ellipse car
  pygame.draw.ellipse(screen, "yellow", pygame.Rect((645,645), (80,50)))

  # Draw semi truck
  pygame.draw.rect(screen, "white", pygame.Rect((500,460), (120,50)))

  # Update screen
  pygame.display.flip()

  # FPS
  dt = clock.tick(speed)/1000

# End game
game_over = True
pygame.QUIT()  

