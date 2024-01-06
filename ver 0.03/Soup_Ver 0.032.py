import pygame, time

# Initialising Pygame
pygame.init()


# Variables for the program
clock = pygame.time.Clock()
fps = 60

width = 1600
height = 900

black = (0, 0, 0)
white = (225, 225, 225)
blue = (0, 91, 150)
green = (46, 143, 63)
rose = (234, 61, 98)
dusty_pink = (184, 84, 106)
brown = (133, 88, 97)

# Displaying screen
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("JOURNEY OF SOUP")

# Images
# Menu images
title_img = pygame.image.load('./sprites/Title.png').convert_alpha()
load_save_img = pygame.image.load('./sprites/LoadSave.png').convert_alpha()
new_save_img = pygame.image.load('./sprites/NewSave.png').convert_alpha()
quit_img = pygame.image.load('./sprites/Quit.png').convert_alpha()

    # Menu images list
menu_images = [
    [title_img, (450, 150)], 
    [load_save_img, (625, 450)], 
    [new_save_img, (625, 510)], 
    [quit_img, (625, 570)]
]

# Save Screen images/rects
background_rect = pygame.Rect(200, 100, 1200, 700)

emptysave_1_rect = pygame.Rect(220, 120, 1160, 157.5)
emptysave_2_rect = pygame.Rect(220, 287.5, 1160, 157.5)
emptysave_3_rect = pygame.Rect(220, 455, 1160, 157.5)
emptysave_4_rect = pygame.Rect(220, 627.5, 1160, 157.5)

save_1_rect = pygame.Rect(220, 120, 1160, 157.5)
save_2_rect = pygame.Rect(220, 287.5, 1160, 157.5)
save_3_rect = pygame.Rect(220, 455, 1160, 157.5)
save_4_rect = pygame.Rect(220, 627.5, 1160, 157.5)

back_rect = pygame.Rect(200, 825, 237.5, 37.5 )
select_rect = pygame.Rect(462.5, 825, 237.5 ,37.5 )

    # lists of rects all the same colour
smenu_rose_rects = (
    save_1_rect, 
    save_2_rect, 
    save_3_rect, 
    save_4_rect)
    
smenu_dusty_pink_rects = (
    emptysave_1_rect, 
    emptysave_2_rect,
    emptysave_3_rect, 
    emptysave_4_rect, 
    back_rect, 
    select_rect)

# Class for all player information
#class player():

# Class for all boss information
#class boss():
        
# Class to display the rect around the selected button
class Show_Selection():
    def __init__ (self, my_x, my_y, my_width, my_height):

        # Attributes for size and location of the highlight
        self.x = my_x -4
        self.y = my_y -4
        self.width = my_width +8
        self.height =  my_height +8
        self.highlight = pygame.Rect(self.x, self.y ,self.width, self.height)

    # drawing the button
    def draw_highlight(self):
        pygame.draw.rect(screen, green, self.highlight)

 
# Class to change selection and stop users from going past the set limits for selection
class Menu_Selection():
    def __init__ (self, my_upper_lim, my_lower_lim):
        self.upper_lim = my_upper_lim
        self.lower_lim = my_lower_lim
	
    # Select the next button upwards
    def select_up(self, selected):
        if selected > self.lower_lim:
            selected -= 1
        return selected

    # Select the next button downwards
    def select_down(self, selected):
        if selected < self.upper_lim:
            selected += 1
        return selected

# Creating objects for the menu
main_menu_s = Menu_Selection(2, 0)

l_save_highlight = Show_Selection(625, 450, 350, 50)
n_save_highlight = Show_Selection(625, 510, 350, 50)
quit_highlight = Show_Selection(625, 570, 350, 50)


# Display rects on screen
def draw_rects(list, colour):
    for i in list:
        pygame.draw.rect(screen, colour, i)

# Display images on screen
def blit_images(list):
    for i in range(len(list)):
        screen.blit(list[i][0], list[i][1])
  
# Screens
# All methods of the game screen
def game():
    run = True
    while run:

        screen.fill(white)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                raise SystemExit

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    run = False
                    
        pygame.display.update()
        clock.tick(60)
                
# All methods of the new save screen
def new_save():
    run = True
    while run:

        screen.fill(white)
        pygame.draw.rect(screen, brown, background_rect)
        draw_rects(smenu_dusty_pink_rects, dusty_pink)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                raise SystemExit

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    run = False

        pygame.display.update()
        clock.tick(60)

# All methods of the options screen
def options():
    run = True
    while run:

        screen.fill(white)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                raise SystemExit
                
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    run = False
                    #
        pygame.display.update()
        clock.tick(60)

# All methods of the main menu
def main_menu():
    # setting selection as a variable to check which button the user is selecting
    selection = 0
    while True:

        screen.fill(white)
    
        # using the selection variable to show which button is selected
        if selection == 0:
            l_save_highlight.draw_highlight()
        elif selection == 1:
            n_save_highlight.draw_highlight() 
        elif selection == 2:
            quit_highlight.draw_highlight()
          
        # Displaying all images for the main menu
        blit_images(menu_images)

        # Event handling
        for event in pygame.event.get():
            # To quit game
            if event.type == pygame.QUIT:
                pygame.quit()
                raise SystemExit
                
            # check if keys are pressed and act accordingly
            elif event.type == pygame.KEYDOWN:
            
                if event.key == pygame.K_w:
                    selection = main_menu_s.select_up(selection)
                    print(selection)

                elif event.key == pygame.K_s:
                    selection = main_menu_s.select_down(selection)
                    print(selection)

                elif event.key == pygame.K_e:
                    if selection == 0:
                        game()
                    elif selection == 1:
                        new_save()
                    elif selection == 2:
                        pygame.quit()
                        raise SystemExit


        
        pygame.display.update()
        clock.tick(60)

# Main
run = True
while run:

    main_menu()

# next commit please work 
