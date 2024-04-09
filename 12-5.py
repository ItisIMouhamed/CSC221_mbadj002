
import pygame
import sys

class Keys:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800,600))

    def check_keydown_event(self,event):
        if event.type == pygame.KEYDOWN:
            print("Key pressed:", event.key)


def main():
    keys = Keys()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            else:
               keys.check_keydown_event(event)

        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()