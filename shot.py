from circleshape import *
from constants import *

class Shot(CircleShape):
    width = 2
    def __init__(self, x, y, SHOT_RADIUS):
        super().__init__(x, y, SHOT_RADIUS)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, Shot.width)

    def update(self, dt):
        self.position += self.velocity * dt

        