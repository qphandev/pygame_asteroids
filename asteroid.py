import circleshape
import pygame
import random
from constants import *

class Asteroid(circleshape.CircleShape):
    width = 2
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, Asteroid.width)

    def split(self):
        if self.radius <= ASTEROID_MIN_RADIUS:
            self.kill()
            return
        random_angle = random.uniform(20, 50)
        vector_1 = self.velocity.rotate(-random_angle)
        vector_2 = self.velocity.rotate(random_angle)

        new_radius = self.radius - ASTEROID_MIN_RADIUS

        asteroid_split_1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid_split_1.velocity = vector_1 * 1.2

        asteroid_split_2 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid_split_2.velocity = vector_2 * 1.2

        self.kill()
        

    def update(self, dt):
        self.position += (self.velocity * dt)