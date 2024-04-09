import pygame
import sys

class Shooter:
    def __init__(self):
        pygame.init()
        self.SCREEN_WIDTH = 800
        self.SCREEN_HEIGHT = 600
        self.screen = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        pygame.display.set_caption("Sideways shooter (TIY # 12-6)")

        # Set background color
        self.bg_color = (230, 230, 230)

        # Ship settings
        self.SHIP_WIDTH = 50
        self.SHIP_HEIGHT = 30
        self.ship_speed = 5

        # Bullet settings
        self.BULLET_WIDTH = 10
        self.BULLET_HEIGHT = 5
        self.bullet_speed = 7
        self.bullet_color = (255, 0, 0)

        # Load the ship image
        self.ship_image = pygame.image.load("images/rocket.jpg")
        self.ship_rect = self.ship_image.get_rect()
        self.ship_rect.y = self.SCREEN_HEIGHT // 2 - self.SHIP_HEIGHT // 2

        # List to hold bullets
        self.bullets = []

        # Clock
        self.clock = pygame.time.Clock()

        # Running flag
        self.running = True

    def run_game(self):
        while self.running:
            self._check_events()
            self._update_screen()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    # Fire bullet
                    bullet = pygame.Rect(self.ship_rect.right, self.ship_rect.centery - self.BULLET_HEIGHT // 2, self.BULLET_WIDTH, self.BULLET_HEIGHT)
                    self.bullets.append(bullet)

        # Move ship up and down
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and self.ship_rect.top > 0:
            self.ship_rect.y -= self.ship_speed
        elif keys[pygame.K_DOWN] and self.ship_rect.bottom < self.SCREEN_HEIGHT:
            self.ship_rect.y += self.ship_speed

        # Move bullets and delete bullets that go off-screen
        for bullet in self.bullets:
            bullet.x += self.bullet_speed
            if bullet.right > self.SCREEN_WIDTH:
                self.bullets.remove(bullet)

    def _update_screen(self):
        self.screen.fill(self.bg_color)
        self.screen.blit(self.ship_image, self.ship_rect)
        for bullet in self.bullets:
            pygame.draw.rect(self.screen, self.bullet_color, bullet)
        pygame.display.flip()
        self.clock.tick(60)

if __name__ == "__main__":
    shooter_game = Shooter()
    shooter_game.run_game()
    pygame.quit()
    sys.exit()











"""import pygame
import sys

class Shooter:
    def __init__(self):
        pygame.init()
        self.SCREEN_WIDTH = 800
        self.SCREEN_HEIGHT = 600
        self.screen = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        pygame.display.set_caption("Sideways shooter (TIY # 12-6)")

        # Set background color
        self.bg_color = (230, 230, 230)

        # Ship settings
        self.SHIP_WIDTH = 50
        self.SHIP_HEIGHT = 30
        self.ship_speed = 5

        # Bullet settings
        self.BULLET_WIDTH = 10
        self.BULLET_HEIGHT = 5
        self.bullet_speed = 7
        self.bullet_color = (255, 0, 0)

        # Create the ship
        self.rocket_image = pygame.image.load("images/rocket.jpg")
        #self.ship = pygame.Rect(50, self.SCREEN_HEIGHT // 2 - self.SHIP_HEIGHT // 2, self.SHIP_WIDTH, self.SHIP_HEIGHT)

        # List to hold bullets
        self.bullets = []

        # Clock
        self.clock = pygame.time.Clock()

        # Running flag
        self.running = True

    def run_game(self):
        while self.running:
            self._check_events()
            self._update_screen()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    # Fire bullet
                    bullet = pygame.Rect(self.ship.right, self.ship.centery - self.BULLET_HEIGHT // 2, self.BULLET_WIDTH, self.BULLET_HEIGHT)
                    self.bullets.append(bullet)

        # Move ship up and down
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and self.ship.top > 0:
            self.ship.y -= self.ship_speed
        elif keys[pygame.K_DOWN] and self.ship.bottom < self.SCREEN_HEIGHT:
            self.ship.y += self.ship_speed

        # Move bullets and delete bullets that go off-screen
        for bullet in self.bullets:
            bullet.x += self.bullet_speed
            if bullet.right > self.SCREEN_WIDTH:
                self.bullets.remove(bullet)

    def _update_screen(self):
        self.screen.fill(self.bg_color)
        pygame.draw.rect(self.screen, (255, 255, 255), self.ship)
        for bullet in self.bullets:
            pygame.draw.rect(self.screen, self.bullet_color, bullet)
        pygame.display.flip()
        self.clock.tick(60)

if __name__ == "__main__":
    shooter_game = Shooter()
    shooter_game.run_game()
    pygame.quit()
    sys.exit()"""



"""import pygame

import sys

class Shooter:
    def __init__(self):
        pygame.init()
        self.SCREEN_WIDTH = 800
        self.SCREEN_HEIGHT = 600
        self.screen = pygame.display.set_mode((self.SCREEN_WIDTH,self.SCREEN_HEIGHT))
        pygame.display.set_caption("Sideways shooter (TIY # 12-6)")

        # Set background color
        self.bg_color = (230,230,230)

    def ship(self):
        # Ship settings
        self.SHIP_WIDTH = 50
        self.SHIP_HEIGHT = 30
        self.ship_speed = 5

    def bullet(self):
        # Bullet settings
        self.BULLET_WIDTH = 10
        self.BULLET_HEIGHT = 5
        self.bullet_speed = 7
        self.bullet_color = (255, 0, 0)

# Create the ship
ship = pygame.Rect(50, SCREEN_HEIGHT // 2 - SHIP_HEIGHT // 2, SHIP_WIDTH, SHIP_HEIGHT)

# List to hold bullets
bullets = []

clock = pygame.time.Clock()

# Main game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                # Fire bullet
                bullet = pygame.Rect(ship.right, ship.centery - BULLET_HEIGHT // 2, BULLET_WIDTH, BULLET_HEIGHT)
                bullets.append(bullet)

    # Move ship up and down
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and ship.top > 0:
        ship.y -= ship_speed
    elif keys[pygame.K_DOWN] and ship.bottom < SCREEN_HEIGHT:
        ship.y += ship_speed

    # Move bullets and delete bullets that go off-screen
    for bullet in bullets:
        bullet.x += bullet_speed
        if bullet.right > SCREEN_WIDTH:
            bullets.remove(bullet)

    # Draw everything
    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, ship)
    for bullet in bullets:
        pygame.draw.rect(screen, bullet_color, bullet)
    
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()
sys.exit()"""