import pygame
import sys
import matplotlib
matplotlib.use("Agg")
from pygame.locals import *

import matplotlib.backends.backend_agg as agg

import pylab

fig = pylab.figure(figsize=[4, 4], # Inches
                   dpi=100,        # 100 dots per inch, so the resulting buffer is 400x400 pixels
                   )
ax = fig.gca()
ax.plot([1, 2, 4])

canvas = agg.FigureCanvasAgg(fig)
canvas.draw()
renderer = canvas.get_renderer()
raw_data = renderer.tostring_rgb()


# Initialize Pygame
pygame.init()

clock=pygame.time.Clock()

# Create a Pygame window
window_size = (415, 600)
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption('Interface')

size = canvas.get_width_height()
surf = pygame.image.fromstring(raw_data, size, "RGB")
screen.blit(surf, (0,200))

# Create a font object
font = pygame.font.Font(None, 24)

# Create a surface for the button
button_surface = pygame.Surface((150, 25))

# Render text on the button
base_font = pygame.font.Font(None, 32) 
text = font.render("Recalcular", True, (0, 0, 0))
text_rect = text.get_rect(center=(button_surface.get_width()/2, button_surface.get_height()/2))


# Create a pygame.Rect object that represents the button's boundaries
button_rect = pygame.Rect(75, 75, 75, 50)  # Adjust the position as needed

user_text = '' 
  
# create rectangle 
input_rect_1 = pygame.Rect(1, 10, 10, 35) 

input_rect_2 = pygame.Rect(110, 10, 10, 35) 

input_rect_3 = pygame.Rect(220, 10, 10, 35) 

input_rect_4 = pygame.Rect(330, 10, 10, 35) 
  
# color_active stores color(lightskyblue3) which 
# gets active when input box is clicked by user 
color_active = pygame.Color('lightskyblue3') 
  
# color_passive store color(chartreuse4) which is 
# color of input box. 
color_passive = pygame.Color('chartreuse4') 
color_1 = color_passive 
color_2 = color_passive 
color_3 = color_passive 
color_4 = color_passive 
  
active_1 = False
active_2 = False
active_3 = False
active_4 = False

# Start the main loop
while True:

 # Get events from the event queue
 for event in pygame.event.get():
  # Check for the quit event
  if event.type == pygame.QUIT:
   # Quit the game
   pygame.quit()
   sys.exit()
  if event.type == pygame.MOUSEBUTTONDOWN: 
            if input_rect_1.collidepoint(event.pos): 
                active_1 = True
            else: 
                active_1 = False

            if input_rect_2.collidepoint(event.pos): 
                active_2 = True
            else: 
                active_2 = False

            if input_rect_3.collidepoint(event.pos): 
                active_3 = True
            else: 
                active_3 = False

            if input_rect_4.collidepoint(event.pos): 
                active_4 = True
            else: 
                active_4 = False
  
            if event.type == pygame.KEYDOWN: 
                if active_1:
                    if event.key == pygame.K_RETURN:
                        user_text = user_text  # Alternativa: apertar Enter para atualizar o texto
                    elif event.key == pygame.K_BACKSPACE:
                        user_text = user_text[:-1]
                    else:
                        user_text += event.unicode
  if active_1: 
        color_1 = color_active
  else: 
        color_1 = color_passive 

  if active_2: 
        color_2 = color_active
  else: 
        color_2 = color_passive 

  if active_3: 
        color_3 = color_active
  else: 
        color_3 = color_passive 

  if active_4: 
        color_4 = color_active
  else: 
        color_4 = color_passive 
          
    # draw rectangle and argument passed which should 
    # be on screen 

  # Check for the mouse button down event
  if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
   # Call the on_mouse_button_down() function
   if button_rect.collidepoint(event.pos):
    text = font.render("Recalcular", True, (0, 0, 0))

 # Check if the mouse is over the button. This will create the button hover effect
 if button_rect.collidepoint(pygame.mouse.get_pos()):
  pygame.draw.rect(button_surface, (127, 255, 212), (1, 1, 148, 48))
 else:
  pygame.draw.rect(button_surface, (0, 0, 0), (0, 0, 150, 50))
  pygame.draw.rect(button_surface, (255, 255, 255), (1, 1, 148, 48))
  pygame.draw.rect(button_surface, (0, 0, 0), (1, 1, 148, 1), 2)
  pygame.draw.rect(button_surface, (0, 100, 0), (1, 48, 148, 10), 2)
  
  
 pygame.draw.rect(screen, color_1, input_rect_1) 

 pygame.draw.rect(screen, color_2, input_rect_2) 

 pygame.draw.rect(screen, color_3, input_rect_3) 

 pygame.draw.rect(screen, color_4, input_rect_4) 

 text_surface = base_font.render(user_text, True, (0, 0, 0)) 

 # Shwo the button text
 button_surface.blit(text, text_rect)


    # render at position stated in arguments 
 screen.blit(text_surface, (input_rect_1.x+5, input_rect_1.y+5)) 

 screen.blit(text_surface, (input_rect_2.x+5, input_rect_2.y+5)) 

 screen.blit(text_surface, (input_rect_3.x+5, input_rect_3.y+5)) 

 screen.blit(text_surface, (input_rect_4.x+5, input_rect_4.y+5)) 
 # Draw the button on the screen
 screen.blit(button_surface, (button_rect.x, button_rect.y))

       
 # set width of textfield so that text cannot get 
 # outside of user's text input 
 input_rect_1.w = max(100, text_surface.get_width()+10) 
 input_rect_2.w = max(100, text_surface.get_width()+10) 
 input_rect_3.w = max(100, text_surface.get_width()+10) 
 input_rect_4.w = max(100, text_surface.get_width()+10) 

 # Update the game state
 pygame.display.flip()

 # Set the frame rate
 clock.tick(60)