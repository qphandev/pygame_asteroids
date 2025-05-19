# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import Player

def main(): 
    pygame.init()
    
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    # instantiate clock object
    clock = pygame.time.Clock()

    # create empty groups (they're like the big venns), player is an item inside set
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    # added groups to static container property, needs to be before instantiation, makes me wonder why I can't do this inside the class itself.
    Player.containers = (updatable, drawable)

     # instantiate player
    player = Player(x = SCREEN_WIDTH / 2, 
           y = SCREEN_HEIGHT / 2)

    # initialize delta time
    dt = 0

    while True:
        # Makes close window on Mac work, else you can't close it.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        updatable.update(dt)
        screen.fill((0,0,0))
        
        for obj in drawable:
            obj.draw(screen)
        
        pygame.display.flip()

        # limit the framerate to 60 FPS
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()