import pygame
import menu_items as m
import colors as c
from options_menu import Options_menu
from tutorial import Tutorial
from players import Player_amount
from highscores import Highscores
from dice import Dice
from database import Database

class Main_menu:
    def __init__(self, screen, state, mute):
        self.screen = screen
        self.state = state
        self.mute = mute
    def update(self, events, mouse):
        self.screen.fill(c.white())
        titleText, titleRect = m.text_objects("Ontsnapperdam", "large", c.black())
        titleRect.center = ((self.screen.get_width()/2), (self.screen.get_height()/10))
        self.screen.blit(titleText, titleRect)
        if self.state == "win":
            start_button = m.Button(events, self.screen, mouse, c.dark_green(), c.bright_green(), "Start game", "medium", c.white(), ((self.screen.get_width()/2) - 100), (((self.screen.get_height()/7) * 2)- 25), 200, 50)
            options_button = m.Button(events, self.screen, mouse, c.dark_blue(), c.bright_blue(), "Options", "medium", c.white(), ((self.screen.get_width()/2) - 100), (((self.screen.get_height()/7) * 3) - 25), 200, 50)
            tutorial_button = m.Button(events, self.screen, mouse, c.dark_yellow(), c.bright_yellow(), "Tutorial", "medium", c.white(), ((self.screen.get_width()/2) - 100), (((self.screen.get_height()/7) * 4) - 25), 200, 50)
            highscore_button = m.Button(events, self.screen, mouse, c.dark_pink(), c.bright_pink(), "Highscores", "medium", c.white(), ((self.screen.get_width()/2) - 100), (((self.screen.get_height()/7) * 5) - 25), 200, 50)
            exit_button = m.Button(events, self.screen, mouse, c.dark_red(), c.bright_red(), "Quit", "medium", c.white(), ((self.screen.get_width()/2) - 100), (((self.screen.get_height()/7) * 6) - 25), 200, 50)
        elif self.state == "full":
            start_button = m.Button(events, self.screen, mouse, c.dark_green(), c.bright_green(), "Start game", "medium", c.white(), ((self.screen.get_width()/2) - (100 * 2.25)), (((self.screen.get_height()/7) * 2) - (25 * 2.25)), (200 * 2.25), (50 * 2.25))
            options_button = m.Button(events, self.screen, mouse, c.dark_blue(), c.bright_blue(), "Options", "medium", c.white(), ((self.screen.get_width()/2) - (100 * 2.25)), (((self.screen.get_height()/7) * 3) - (25 * 2.25)), (200 * 2.25), (50 * 2.25))
            tutorial_button = m.Button(events, self.screen, mouse, c.dark_yellow(), c.bright_yellow(), "Tutorial", "medium", c.white(), ((self.screen.get_width()/2) - (100 * 2.25)), (((self.screen.get_height()/7) * 4) - (25 * 2.25)), (200 * 2.25), (50 * 2.25))
            highscore_button = m.Button(events, self.screen, mouse, c.dark_pink(), c.bright_pink(), "Highscores", "medium", c.white(), ((self.screen.get_width()/2) - (100 * 2.25)), (((self.screen.get_height()/7) * 5) - (25 * 2.25)), (200 * 2.25), (50 * 2.25))
            exit_button = m.Button(events, self.screen, mouse, c.dark_red(), c.bright_red(), "Quit", "medium", c.white(), ((self.screen.get_width()/2) - (100 * 2.25)), (((self.screen.get_height()/7) * 6) - (25 * 2.25)), (200 * 2.25), (50 * 2.25))
        if start_button.use():
            new_screen = Player_amount(self.screen, self.state, self.mute)
            return new_screen
        if options_button.use():
            new_screen = Options_menu(self.screen, self.state, self.mute)
            return new_screen
        if tutorial_button.use():
            new_screen = Tutorial(self.screen, self.state, self.mute)
            return new_screen
        if highscore_button.use():
            new_screen = Highscores(self.screen, self.state, self.mute)
            return new_screen
        if exit_button.use():
            exit()
        return self

#1080p = 2.25 keer zo groot