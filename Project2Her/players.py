import pygame
import colors as c
import menu_items as m
from name_players import Names

class Player_amount:
    def __init__(self, screen, state, mute):
        self.screen = screen
        self.state = state
        self.mute = mute
    def update(self, events, mouse):
        self.screen.fill(c.white())
        titleText, titleRect = m.text_objects("Select player amount", "large", c.black())
        titleRect.center = ((self.screen.get_width()/2), (self.screen.get_height()/10))
        self.screen.blit(titleText, titleRect)
        if self.state == "win":
            back_button = m.Button(events, self.screen, mouse, c.dark_red(), c.bright_red(), "Back", "medium", c.white(), 0, (self.screen.get_height() - 50), 100, 50)
            p3_button = m.Button(events, self.screen, mouse, c.dark_red(), c.bright_red(), "3 Players", "medium", c.white(), ((self.screen.get_width()/2) - 100), ((self.screen.get_height()/3) - 25), 200, 50)
            p4_button = m.Button(events, self.screen, mouse, c.dark_blue(), c.bright_blue(), "4 Players", "medium", c.white(), ((self.screen.get_width()/2) - 100), ((self.screen.get_height()/2) - 25), 200, 50)
            p5_button = m.Button(events, self.screen, mouse, c.dark_green(), c.bright_green(), "5 Players", "medium", c.white(), ((self.screen.get_width()/2) - 100), (((self.screen.get_height()/3) * 2) - 25), 200, 50)
            p6_button = m.Button(events, self.screen, mouse, c.dark_yellow(), c.bright_yellow(), "6 Players", "medium", c.white(), ((self.screen.get_width()/2) - 100), (((self.screen.get_height()/6) * 5) - 25), 200, 50)
        elif self.state == "full":
            back_button = m.Button(events, self.screen, mouse, c.dark_red(), c.bright_red(), "Back", "medium", c.white(), 0, (self.screen.get_height() - (50 * 2.25)), (100 * 2.25), (50 * 2.25))
            p3_button = m.Button(events, self.screen, mouse, c.dark_red(), c.bright_red(), "3 Players", "medium", c.white(), ((self.screen.get_width()/2) - (100 * 2.25)), ((self.screen.get_height()/3) - (25 * 2.25)), (200 * 2.25), (50 * 2.25))
            p4_button = m.Button(events, self.screen, mouse, c.dark_blue(), c.bright_blue(), "4 Players", "medium", c.white(), ((self.screen.get_width()/2) - (100 * 2.25)), ((self.screen.get_height()/2) - (25 * 2.25)), (200 * 2.25), (50 * 2.25))
            p5_button = m.Button(events, self.screen, mouse, c.dark_green(), c.bright_green(), "5 Players", "medium", c.white(), ((self.screen.get_width()/2) - (100 * 2.25)), (((self.screen.get_height()/3) * 2) - (25 * 2.25)), (200 * 2.25), (50 * 2.25))
            p6_button = m.Button(events, self.screen, mouse, c.dark_yellow(), c.bright_yellow(), "6 Players", "medium", c.white(), ((self.screen.get_width()/2) - (100 * 2.25)), (((self.screen.get_height()/6) * 5) - (25 * 2.25)), (200 * 2.25), (50 * 2.25))
        if back_button.use():
            from main_menu import Main_menu
            new_screen = Main_menu(self.screen, self.state, self.mute)
            return new_screen
        if p3_button.use():
            new_screen = Names(self.screen, self.state, self.mute, 3)
            return new_screen
        if p4_button.use():
            new_screen = Names(self.screen, self.state, self.mute, 4)
            return new_screen
        if p5_button.use():
            new_screen = Names(self.screen, self.state, self.mute, 5)
            return new_screen
        if p6_button.use():
            new_screen = Names(self.screen, self.state, self.mute, 6)
            return new_screen
        return self