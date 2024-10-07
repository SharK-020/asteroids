from circleshape import CircleShape
import pygame
import random
from constants import *
class Asteroid(CircleShape):
  def __init__(self,x,y,radius):
    super().__init__(x,y,radius)
  
  def draw(self, screen):
    pygame.draw.circle(screen,color="white",radius=self.radius,width=2,center=self.position)
  
  def update(self, dt):
    self.position+=(self.velocity*dt)

  def split(self):
    self.kill()

    if self.radius<=ASTEROID_MIN_RADIUS:
      return

    else:
      random_angle=random.uniform(20,50)
      v1=self.velocity.rotate(random_angle)
      v2=self.velocity.rotate(-random_angle)

      new_radius=self.radius-ASTEROID_MIN_RADIUS

      a1=Asteroid(self.position.x,self.position.y,new_radius)
      a1.velocity=v1*1.2
      a2=Asteroid(self.position.x,self.position.y,new_radius)
      a2.velocity=v2*1.2