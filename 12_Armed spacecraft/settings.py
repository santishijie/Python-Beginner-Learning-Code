class Settings:
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        self.ship_speed = 1.0
        self.ship_limit = 3
        self.bullet_speed = 0.5
        self.bullet_width = 300
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullet_allowed = 3
        self.alien_speed = 0.2
        self.fleet_drop_speed = 48.0
        # fleet_direction为1表示向右，-1表示向左
        self.fleet_direction = 1
