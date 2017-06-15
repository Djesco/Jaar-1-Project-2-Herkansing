import pygame
import colors as c
import menu_items as m
from sound import Sound

class Options_menu:
    def __init__(self, screen, state, mute):
        self.screen = screen
        self.state = state
        self.mute = mute
    def update(self, events, mouse):
        self.screen.fill(c.white())
        titleText, titleRect = m.text_objects("Options", "large", c.black())
        titleRect.center = ((self.screen.get_width()/2), (self.screen.get_height()/10))
        self.screen.blit(titleText, titleRect)
        if self.state == "win":
            fullscreen_button = m.Button(events, self.screen, mouse, c.dark_blue(), c.bright_blue(), "Fullscreen", "medium", c.white(), ((self.screen.get_width()/2) - 100), (((self.screen.get_height()/5) * 2) - 25), 200, 50)
            back_button = m.Button(events, self.screen, mouse, c.dark_red(), c.bright_red(), "Back", "medium", c.white(), 0, (self.screen.get_height() - 50), 100, 50)
            if self.mute == False:
                mute_button = m.Button(events, self.screen, mouse, c.dark_blue(), c.bright_blue(), "Mute", "medium", c.white(), ((self.screen.get_width()/2) - 100), (((self.screen.get_height()/5) * 3) - 25), 200, 50)
            elif self.mute == True:
                mute_button = m.Button(events, self.screen, mouse, c.dark_blue(), c.bright_blue(), "Unmute", "medium", c.white(), ((self.screen.get_width()/2) - 100), (((self.screen.get_height()/5) * 3) - 25), 200, 50)
        elif self.state == "full":
            fullscreen_button = m.Button(events, self.screen, mouse, c.dark_blue(), c.bright_blue(), "Windowed", "medium", c.white(), ((self.screen.get_width()/2) - (100 * 2.25)), (((self.screen.get_height()/5) * 2) - (25 * 2.25)), (200 * 2.25), (50 * 2.25))
            back_button = m.Button(events, self.screen, mouse, c.dark_red(), c.bright_red(), "Back", "medium", c.white(), 0, (self.screen.get_height() - (50 * 2.25)), (100 * 2.25), (50 * 2.25))
            if self.mute == False:
                mute_button = m.Button(events, self.screen, mouse, c.dark_blue(), c.bright_blue(), "Mute", "medium", c.white(), ((self.screen.get_width()/2) - (100 * 2.25)), (((self.screen.get_height()/5) * 3) - (25 * 2.25)), (200 * 2.25), (50 * 2.25))
            elif self.mute == True:
                mute_button = m.Button(events, self.screen, mouse, c.dark_blue(), c.bright_blue(), "Unmute", "medium", c.white(), ((self.screen.get_width()/2) - (100 * 2.25)), (((self.screen.get_height()/5) * 3) - (25 * 2.25)), (200 * 2.25), (50 * 2.25))
        if fullscreen_button.use():
            if self.state == "win":
                self.screen = pygame.display.set_mode((1920, 1080), pygame.FULLSCREEN)
                self.state = "full"
            elif self.state == "full":
                self.screen = pygame.display.set_mode((1280, 720))
                self.state = "win"
        if back_button.use():
            from main_menu import Main_menu
            new_screen = Main_menu(self.screen, self.state, self.mute)
            return new_screen
        if mute_button.use():
            if self.mute == False:
                Sound.stop_music()
                self.mute = True
            elif self.mute == True:
                Sound.play_music()
                self.mute = False
        return self