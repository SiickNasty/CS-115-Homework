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

def game_over():
  global screen
  global my_font
  global score
  display_draw_text = (f"Game Over!", (350,375), "black", my_font, screen)
  