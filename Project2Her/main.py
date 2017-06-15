import pygame
from main_menu import Main_menu
from sound import Sound
pygame.init()
pygame.display.set_caption("Ontsnapperdam")

clock = pygame.time.Clock()

class main:
    def __init__(self):
        self.width = 1280
        self.height = 720
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.state = "win"
    def exe(self):
        Sound.play_music()
        current_screen = Main_menu(self.screen, self.state, False)
        while True:
            dt = clock.tick(60)
            events = pygame.event.get()
            mouse = pygame.mouse.get_pos()
            for event in events:
                if event.type == pygame.QUIT:
                    exit()
            current_screen = current_screen.update(events, mouse)
            pygame.display.flip()
program = main()
program.exe()