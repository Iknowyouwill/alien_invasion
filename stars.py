import pygame
from pygame.sprite import Sprite
from random import randint

class Star(Sprite):
  """表示单个星星的类"""

  def __init__(self, ai_settings, screen):
    """初始化星星并设置位置"""
    super(Star, self).__init__()
    self.screen = screen
    self.ai_settings = ai_settings

    # 加载星星图像
    self.image = pygame.image.load('images/star2.png')
    self.rect = self.image.get_rect()

    self.x = randint(0, self.ai_settings.screen_width - self.rect.width)
    self.y = randint(0, self.ai_settings.screen_height - self.rect.height)

    self.rect.x = self.x
    self.rect.y = self.y

  def blitme(self):
    """绘制星星"""
    self.screen.blit(self.image, self.rect)
    
  def check_bottom(self):
    """到达底部"""
    screen_rect = self.screen.get_rect()
    if self.rect.y >= screen_rect.height:
      return True
    else: 
      return False

  def update(self):
    """向下移动星星, 模拟飞船向前飞行"""
    if self.check_bottom():
      self.y = 0
      self.x = randint(0, self.ai_settings.screen_width - self.rect.width)
    else:
      self.y += self.ai_settings.stars_speed_factor
    self.rect.y = self.y
    self.rect.x = self.x

  def get_random_x(self):
    """获取随机数x"""
    x = randint(0, self.ai_settings.screen_width - self.rect.width)
    return x
