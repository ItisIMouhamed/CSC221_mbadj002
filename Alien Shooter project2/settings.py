class Settings:
    '''A class to store all settings for Alien Invasion.'''

    def __init__(self):
        '''Intiialize the game's settings.'''
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        #self.bg_color = (0,0,255) # TIY 12-1 (Blue Sky)
        self.bg_color = (85,163,230) # TIY 12-2 (I changed the color in order to try and match my new image)

        # Ship settings
        self.ship_speed = 1.5
        self.ship_limit = 3

        # Bullet settings
        self.bullet_speed = 2.5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 20

        # Alien settings
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10 
        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1

     

     