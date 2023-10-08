import pygame
from pygame.sprite import Sprite


class Ailen(Sprite):
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # 存储外星人的精确位置
        self.x = float(self.rect.x)

    def update(self) -> None:
        """向右或向左移动外星人"""
        self.x += self.settings.alien_speed * self.settings.fleet_direction
        self.rect.x = self.x

    def check_edges(self):
        """如果碰到边缘，返回true"""
        screen_rect = self.screen.get_rect()
        return (self.rect.right > screen_rect.right) or (self.rect.left < 0)


