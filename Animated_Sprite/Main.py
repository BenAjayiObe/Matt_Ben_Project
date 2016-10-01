import pygame
import sys

def load_image(name):
    image = pygame.image.load(name)
    return image

class SpriteSheet(object):
    def __init__(self, file_name):
         self.sprite_sheet = pygame.image.load(file_name).convert()

    def get_image(self, x, y, width, height):
        """ Grab a single image out of a larger spritesheet
            Pass in the x, y location of the sprite
            and the width and height of the sprite. """
 
        # Create a new blank image
        image = pygame.Surface([width, height]).convert()
 
        # Copy the sprite from the large sheet onto the smaller image
        image.blit(self.sprite_sheet, (0, 0), (x, y, width, height))
 
        # Assuming black works as the transparent color
        image.set_colorkey((   0,   255,   255))
 
        # Return the image
        return image

class Player(pygame.sprite.Sprite):
    """ This class represents the bar at the bottom that the player
    controls. """

    # -- Methods
    def __init__(self):
        """ Constructor function """
 
        # Call the parent's constructor
        super(Player,self).__init__()
 
        # This holds all the images for the animated walk left/right
        # of our player
        self.thrust_frame = []

        self.thrust_index = 0;
 
        sprite_sheet = SpriteSheet("Sprites/Formated_Thrust_Up_Right.png")
        for x in range(5):
		    # Load all the right facing images into a list
		    image = sprite_sheet.get_image(x*176, 0, 161, 176)
		    self.thrust_frame.append(image)
 
        # Set the image the player starts with
        self.image = self.thrust_frame[0]
 
        # Set a reference to the image rect.
        self.rect = self.image.get_rect()
 
    def update(self):

    	if self.thrust_index==len(self.thrust_frame):
    		self.thrust_index=0

        self.image = self.thrust_frame[self.thrust_index]
        self.thrust_index+=1
        
        
        self.rect.x += 7
        if self.rect.x > 800:
            self.rect.x = -161


def main():
    """ Main Program """
    pygame.init()
 
    # Set the height and width of the screen
    size = [800, 600]
    screen = pygame.display.set_mode(size)
 
    pygame.display.set_caption("Platformer with sprite sheets")

    # Create the player
    player = Player()

    active_sprite_list = pygame.sprite.Group()
    player.rect.x = 340
    player.rect.y = 500 - player.rect.height
    active_sprite_list.add(player)
 
    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()

    screen = pygame.display.set_mode(size)

    while True:

        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)

        # Update the player.
        active_sprite_list.update()

        screen.fill((0,0,0))

        active_sprite_list.draw(screen)

        # Limit to 60 frames per second
        clock.tick(12)
 
        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()

if __name__ == '__main__':
    main()