import pygame

# init pygame
pygame.init()

# window dimensions
width = 1000
height = 850
screen = pygame.display.set_mode((width,height))

# set window title
pygame.display.set_caption("Snake")

# fps 
clock = pygame.time.Clock()
dt = 0 
speed = 10 

""" Game loop """
running = True 
while running:
  """Handle events"""
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
         running = False

  """ Update our game state"""

  """ Draw our screen """
  # Clear screen
  screen.fill("white")

  # draw rectangle
  pygame.draw.rect(
    screen, 
    "green", 
    pygame.Rect((0,750), (1000, 100))
  )

  # draw circle
  pygame.draw.circle(screen, "blue", (100,200), 40)
  pygame.draw.circle(screen, "black", (200,200), 100)

  # draw line
  pygame.draw.line(screen, "red", (100,100), (200,200), 5)

  pygame.draw.ellipse(surface=screen, color="red", rect=pygame.Rect((100,100), (100,500)))

  # Update screen
  pygame.display.flip()

  # FPS
  dt = clock.tick(speed)/1000

# quit game
pygame.quit()  