class Settings():
  """存储《外星人入侵》的所有设置的类"""

  def __init__(self):
    """初始化游戏的设置"""
    # 屏幕设置
    self.screen_width = 1200
    self.screen_height = 800
    self.bg_color = (0, 0, 0)

    # 飞船速度
    self.ship_limit = 1

    # 子弹设置
    self.bullet_width = 300
    self.bullet_height = 30
    self.bullet_color = (0, 255, 255)
    self.bullets_allowed = 9999

    # fleet_drop_speed表示撞墙后向下移动的速度
    self.fleet_drop_speed = 10
    # fleet_direction为1表示向右移, -1表示向左
    self.fleet_direction = 1

    # 修饰用的星星
    self.stars_show = True
    self.stars_number = 5
    self.stars_speed_factor = 0.5

    # 游戏速度
    self.speedup_scale = 1.1
    # 分数速度
    self.score_scale = 1.5
    # 初始化游戏速度
    self.initialize_dynamic_settings()
  
  def initialize_dynamic_settings(self):
    """初始化随游戏进行儿变化"""
    # 飞船速度
    self.ship_speed_factor = 1.5
    # 子弹速度
    self.bullet_speed_factor = 3
    # 敌人左右速度
    self.alien_speed_factor = 1
    # 记分
    self.alien_points = 50

  def increase_speed(self):
    """提高速度"""
    self.ship_speed_factor *= self.speedup_scale
    self.bullet_speed_factor *= self.speedup_scale
    self.alien_speed_factor *= self.speedup_scale

    self.alien_points = int(self.alien_points * self.score_scale)