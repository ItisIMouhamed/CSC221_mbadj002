# TIY 12-4
import pygame
import sys

class Rocket:
    def __init__(self):
        pygame.init()
        SCREEN_WIDTH = 800
        SCREEN_HEIGHT = 600
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Rocket Game")

        # Set background color
        self.bg_color = (230,230,230)

        # Create Rocket
        self.rocket_image = pygame.image.load("images/rocket.jpg")
        self.rocket_rect = self.rocket_image.get_rect()
        self.rocket_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

        # Create clock
        self.clock = pygame.time.Clock()

    def gameloop(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            # Rocket movements
            keys = pygame.key.get_pressed()
            if keys[pygame.K_UP] and self.rocket_rect.top > 0:
                self.rocket_rect.y -= 5
            if keys[pygame.K_DOWN] and self.rocket_rect.bottom < 600:
                self.rocket_rect.y += 5
            if keys[pygame.K_LEFT] and self.rocket_rect.left > 0:
                self.rocket_rect.x -= 5
            if keys[pygame.K_RIGHT] and self.rocket_rect.right < 800:
                self.rocket_rect.x += 5

            # Clear the screen
            self.screen.fill(self.bg_color)

            # Draw the rocket
            self.screen.blit(self.rocket_image, self.rocket_rect)

            # Update the display
            pygame.display.flip()

            # Cap the frame rate
            self.clock.tick(60)

        # Quit Pygame
        pygame.quit()
        sys.exit()

# Create and run the game
rocket_game = Rocket()
rocket_game.gameloop()


        
