# 1.4.6 A simple test program

# Now that pygame is finally accessible, we can try to use it in a very simple test program:

import pygame

run = True
width = 400
height = 100
pygame.init()
screen = pygame.display.set_mode((width, height))
font = pygame.font.SysFont(None, 48)
text = font.render("Welcome to pygame", True, (255, 255, 255))
screen.blit(text, ((width - text.get_width()) // 2, (height - text.get_height()) // 2))
pygame.display.flip()
while run:
  for event in pygame.event.get():
   if event.type == pygame.QUIT\
   or event.type == pygame.MOUSEBUTTONUP\
   or event.type == pygame.KEYUP:
    run = False

# Let’s comment on it briefly.

# line 1: import pygame and let it serve us;
# line 3: the program will run as long as the run variable is True;
# lines 4 and 5: determine the window's size;
# line 6: initialize the pygame environment;
# line 7: prepare the application window and set its size;
# line 8: make an object representing the default font of size 48 points;
# line 9: make an object representing a given text – the text will be anti-aliased (True) and white (255,255,255)
# line 10: insert the text into the (currently invisible) screen buffer;
# line 11: flip the screen buffers to make the text visible;
# line 12: the pygame main loop starts here;
# line 13: get a list of all pending pygame events;
# lines 14 through 16: check whether the user has closed the window or clicked somewhere inside it or pressed any key;
# line 15: if yes, stop executing the code.
# This is what we expect from our impressive code:

      # Welcome to pygame

# The pip install has two important additional abilities:

  # it is able to update a locally installed package – e.g., if you want to make sure that you’re using the latest version of a particular package, 
    # you can run the following command:

# pip install -U package_name


# where -U means update. Note: this form of the command makes use of the --user option for the same purpose as presented previously;

  # it is able to install a user-selected version of a package (pip installs the newest available version by default); 
    # to achieve this goal you should use the following syntax:
    
# pip install package_name==package_version

# (note the double equals sign) e.g.,

# pip install pygame==1.9.2

# If any of the currently installed packages are no longer needed and you want to get rid of them, pip will be useful, too. 
# Its uninstall command will execute all the needed steps.

# The required syntax is clear and simple:

# pip uninstall package_name

# so if you don't want pygame anymore, you can execute the following command:

# pip uninstall pygame

# Pip will want to know if you’re sure about the choice you're making – be prepared to give the right answer.

# The process looks like this:

