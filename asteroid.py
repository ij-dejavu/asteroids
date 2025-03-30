import pygame
from circleshape import CircleShape

class Asteroid(CircleShape):

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

        if hasattr(self.__class__, "containers"):
            for group in self.__class__.containers:
                group.add(self)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", (self.position.x, self.position.y), self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt