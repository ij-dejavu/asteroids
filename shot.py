import pygame
from circleshape import CircleShape
from constants import SHOT_RADIUS, PLAYER_SHOOT_SPEED

class Shot(CircleShape):

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

        if hasattr(self.__class__, "containers"):
            for group in self.__class__.containers:
                group.add(self)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", (int(self.position.x), int(self.position.y)), self.radius)

    def update(self, dt):
        self.position += self.velocity * dt
        
