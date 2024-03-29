import math
import os
import pygame
from pygame.locals import *

class Resources:
  @staticmethod
  def load_png(name):
    """Load image and return image object"""
    fullname = os.path.join('data', name)
    try:
      image = pygame.image.load(fullname)
      if image.get_alpha() is None:
        image = image.convert()
      else:
        image = image.convert_alpha()
    except pygame.error, message:
      print 'Cannot load image:', fullname
      raise SystemExit, message
    return image, image.get_rect()

  @staticmethod
  def calcdistance(p1, p2):
    return math.hypot(p2[0] - p1[0], p2[1] - p1[1])
