def draw_text(text, coordinate, text_color, my_font, screen):
  
  """
  This function draws text to the screen
  text: variable that holds our text
  coordinate: holds our coordiante values
  text_color: holds the color of text, string of list
  """
  
  # global my_font # defined outside of function that can be used inside of function
  # global screen
  text_image = my_font.render(text, True, text_color)
  text_rect = text_image.get_rect()
  text_rect.topleft = coordinate
  screen.blit(text_image, text_rect)
