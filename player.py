from circleshape import CircleShape
from constants import *


class Player(CircleShape):
    def __init__(self,x, y, radius):
      super().__init__(x, y, PLAYER_RADIUS)
      self.roation = 0

    # in the player class
    def triangle(self):
      forward = pygame.Vector2(0, 1).rotate(self.rotation)
      right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
      a = self.position + forward * self.radius
      b = self.position - forward * self.radius - right
      c = self.position - forward * self.radius + right
      return [a, b, c]
  
  