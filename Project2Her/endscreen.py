import pygame
import colors as c
import menu_items as m

class Endscreen:
    def __init__(self, screen, state, mute, winner, turns):
        self.screen = screen
        self.state = state
        self.mute = mute
        self.winner = winner
        self.turns = turns
    def update(self, events, mouse):
        self.screen.fill(c.white())
        titleText, titleRect = m.text_objects("Player: " + str(self.winner) + " has won!", "large", c.black())
        titleRect.center = ((self.screen.get_width()/2), (self.screen.get_height()/10))
        turnsText, turnsRect = m.text_objects("The game took " + str(self.turns) + " turns.", "large", c.black())
        turnsRect.center = ((self.screen.get_width()/2), ((self.screen.get_height()/10) * 2))
        self.screen.blit(titleText, titleRect)
        self.screen.blit(turnsText, turnsRect)
        if self.state == "win":
            home_button = m.Button(events, self.screen, mouse, c.dark_green(), c.bright_green(), "Main menu", "medium", c.white(), ((self.screen.get_width()/2) - 100), (((self.screen.get_height()/5) * 2) - 25), 200, 50)
            exit_button = m.Button(events, self.screen, mouse, c.dark_red(), c.bright_red(), "Quit", "medium", c.white(), ((self.screen.get_width()/2) - 100), (((self.screen.get_height()/5) * 3) - 25), 200, 50)
        elif self.state == "full":
            home_button = m.Button(events, self.screen, mouse, c.dark_green(), c.bright_green(), "Main menu", "medium", c.white(), ((self.screen.get_width()/2) - (100 * 2.25)), (((self.screen.get_height()/5) * 2) - (25 * 2.25)), (200 * 2.25), (50 * 2.25))
            exit_button = m.Button(events, self.screen, mouse, c.dark_red(), c.bright_red(), "Quit", "medium", c.white(), ((self.screen.get_width()/2) - (100 * 2.25)), (((self.screen.get_height()/5) * 3) - (25 * 2.25)), (200 * 2.25), (50 * 2.25))
        if home_button.use():
            from main_menu import Main_menu
            new_screen = Main_menu(self.screen, self.state, self.mute)
            return new_screen
        if exit_button.use():
            exit()
        return self 