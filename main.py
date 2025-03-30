import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    updatable_group = pygame.sprite.Group()
    drawable_group = pygame.sprite.Group()
    asteroids_group = pygame.sprite.Group()

    Player.containers = (updatable_group, drawable_group)
    Asteroid.containers = (asteroids_group, updatable_group, drawable_group)
    AsteroidField.containers = (updatable_group,)

    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    asteroid_field = AsteroidField()


    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")   
    

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        updatable_group.update(dt)
        for i in drawable_group:
            i.draw(screen)
        pygame.display.flip()
        time_passed = clock.tick(60)
        dt = time_passed/1000

if __name__ == "__main__":
    main()
