"""
    Nathan Abrantes 
    Homework 9
    12 March 2025
"""

# Importing variables and defining them
import pygame
width = 1000
height = 850
screen = pygame.display.set_mode((width, height))
cur_posx = 485
cur_posy = 790
score = 0 
lightning_car_coords = [[225,520], [230,560], [250,540], [260,570]]
lightning = pygame.draw.polygon(screen, "violet", lightning_car_coords)
frog = pygame.draw.rect(screen, "green", pygame.Rect(cur_posx, cur_posy, 50, 50))

# Function to draw text
def draw_text(text, coordinate, text_color, my_font, screen):
  
  """
  This function draws text to the screen
  text: variable that holds our text
  coordinate: holds our coordiante values
  text_color: holds the color of text, string of list
  """

  text_image = my_font.render(text, True, text_color)
  text_rect = text_image.get_rect()
  text_rect.topleft = coordinate
  screen.blit(text_image, text_rect)

# Tried to do collision but idk how functions work right
def collision(frogx, frogy, lightningx, lightningy):
  if abs(frogx - lightningx) < 45 and abs(frogy - lightningy) < 55:
    global cur_posx
    global cur_posy
    global lightning_car_coords
    cur_pos = 0 
    lightning_car_coords = 0


collision(frog.centerx, frog.centery, lightning.centerx, lightning.centery)  
        