import pygame
from pygame.sprite import Group

import game_functions as gf

from settings import Settings
from ship import Ship
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard

def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption('Alien Invasion')

    # 创建Play按钮
    play_button = Button(ai_settings, screen, 'Play')

    # 创建状态管理
    stats = GameStats(ai_settings)
    # 创建计分器
    sb = Scoreboard(ai_settings, screen, stats)
    # 创建一艘飞船
    ship = Ship(ai_settings, screen)
    # 创建一个用于存储子弹的编组
    bullets = Group()
    # 创建一群外星人
    aliens = Group()
    # 创建星星
    stars = Group()
    # 创建外星人群
    gf.create_fleet(ai_settings, screen, ship, aliens)
    # 创建星星群
    gf.create_stars(ai_settings, screen, stars)

    # 开始游戏的主循环
    while True:
        # 监听键盘和鼠标事件
        gf.check_events(ai_settings, screen, ship, bullets, aliens, stats, 
          play_button, sb)

        if stats.game_active:
          ship.update()
          gf.update_stars(ai_settings, stars)
          gf.update_bullets(ai_settings, screen, ship, bullets, aliens, stats, sb)
          gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets, sb)

        gf.update_screen(ai_settings, screen, ship, bullets, aliens, stars, stats,
          play_button, sb)
        
run_game()
