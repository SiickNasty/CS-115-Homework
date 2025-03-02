"""
      Nathan Abrantes
      Homework 7
      01 March 2025 
"""

import pygame

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

""" Game loop """
running = True 
while running:
  
  """ Handle events """
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
         running = False

  """ Update game state"""

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
  pygame.draw.circle(screen, "green", (500,812), 25)

  # Draw square car
  pygame.draw.rect(screen, "red", pygame.Rect((350,715), (50,50)))

  # Draw lightning car
  pygame.draw.polygon(screen, "violet", ((230,520), (230,560), (250,540), (260,570)))

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

# You win
def game_over():
  global game_over
  display_game_over = game_over_font.render("You Win!", True, red, black)
screen.blit(display_game_over, (70, 300))

# End game
game_over = True
pygame.quit()  