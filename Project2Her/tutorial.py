import pygame
import colors as c
import menu_items as m

class Tutorial:
    def __init__(self, screen, state, mute):
        self.screen = screen
        self.state = state
        self.mute = mute
        self.current = 1
    def update(self, events, mouse):
        self.screen.fill(c.white())
        titleText, titleRect = m.text_objects("Tutorial", "large", c.black())
        titleRect.center = ((self.screen.get_width()/2), (self.screen.get_height()/10))
        ctText, ctRect = m.text_objects("Tutorial " + str(self.current), "medium", c.black())
        ctRect.center = (100, (self.screen.get_height()/2))
        self.screen.blit(titleText, titleRect)
        self.screen.blit(ctText, ctRect)
        image = pygame.image.load("Assets/Tutorial/" + str(self.current) + ".png")
        self.screen.blit(image, (((self.screen.get_width()/2) - image.get_width()/2), ((self.screen.get_height()/2) - image.get_height()/2)))
        if self.state == "win":
            back_button = m.Button(events, self.screen, mouse, c.dark_red(), c.bright_red(), "Back", "medium", c.white(), 0, (self.screen.get_height() - 50), 100, 50)
            next_button = m.Button(events, self.screen, mouse, c.dark_yellow(), c.bright_yellow(), ">", "medium", c.white(), (self.screen.get_width() - 50), (self.screen.get_height() - 50), 50, 50)
            prev_button = m.Button(events, self.screen, mouse, c.dark_yellow(), c.bright_yellow(), "<", "medium", c.white(), (self.screen.get_width() - 102), (self.screen.get_height() - 50), 50, 50)
        elif self.state == "full":
            back_button = m.Button(events, self.screen, mouse, c.dark_red(), c.bright_red(), "Back", "medium", c.white(), 0, (self.screen.get_height() - (50 * 2.25)), (100 * 2.25), (50 * 2.25))
            next_button = m.Button(events, self.screen, mouse, c.dark_yellow(), c.bright_yellow(), ">", "medium", c.white(), (self.screen.get_width() - (50 * 2.25)), (self.screen.get_height() - (50 * 2.25)), (50 * 2.25), (50 * 2.25))
            prev_button = m.Button(events, self.screen, mouse, c.dark_yellow(), c.bright_yellow(), "<", "medium", c.white(), (self.screen.get_width() - ((102 * 2.25) - 3)), (self.screen.get_height() - (50 * 2.25)), (50 * 2.25), (50 * 2.25))
        if back_button.use():
            from main_menu import Main_menu
            new_screen = Main_menu(self.screen, self.state, self.mute)
            return new_screen
        if next_button.use():
            self.current += 1
            if self.current >= 11:
                self.current = 1
        if prev_button.use():
            self.current -= 1
            if self.current <= 0:
                self.current = 10
        return self