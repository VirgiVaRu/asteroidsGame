from circleshape import CircleShape
from constants import *
from logger import log_event
import pygame
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)
    
    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        angle = random.uniform(20, 50)
        first_asteroid_velocity = self.velocity.rotate(angle)
        second_asteroid_velocity = self.velocity.rotate(-angle)
        smaller_radius = self.radius - ASTEROID_MIN_RADIUS
        first_asteroid = Asteroid(self.position[0], self.position[1], smaller_radius)
        second_asteroid = Asteroid(self.position[0], self.position[1], smaller_radius)
        first_asteroid.velocity = first_asteroid_velocity * 1.2
        second_asteroid.velocity = second_asteroid_velocity * 1.2
