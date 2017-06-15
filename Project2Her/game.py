import pygame
import menu_items as m
import colors as c
from board import Board
from dice import Dice
from endscreen import Endscreen
from database import Database

class Game:
    def __init__(self, screen, state, mute, players, board):
        self.screen = screen
        self.state = state
        self.mute = mute
        self.players = players
        self.board = board
        self.current_player = 1
    def update(self, events, mouse):
        board = Board(self.screen, self.state, self.mute)
        board.draw()
        for player in self.players:
            player.draw(self.screen, self.state)
        try:
            playing = self.players[self.current_player - 1]
            currText, currRect = m.text_objects(str(playing.name) + "'s turn", "large", c.black())
            currRect.center = ((self.screen.get_width()/2), (self.screen.get_height() - 25))
            self.screen.blit(currText, currRect)
            if self.state == "win":
                dice_button = m.Button(events, self.screen, mouse, playing.scolor, playing.color, "Roll dice", "medium", c.white(), 0, self.screen.get_height() - 50, 200, 50)
            elif self.state == "full":
                dice_button = m.Button(events, self.screen, mouse, playing.scolor, playing.color, "Roll dice", "medium", c.white(), 0, self.screen.get_height() - (50 * 2.25), (200 * 2.25), (50 * 2.25))
            if playing.winner == True:
                if playing.win_count_down == 0:
                    new_screen = Endscreen(self.screen, self.state, self.mute, playing.name, playing.turns)
                    Database.upload_score(playing.name, playing.turns)
                    return new_screen
                else:
                    playing.win_count_down -= 1
            if not playing.has_rolled:
                if dice_button.use():
                    playing.has_rolled = True
                    playing.turns += 1
                    roll = Dice.roll(self.screen)
                    playing.moves = roll
            if playing.update(events, board):
                    self.current_player += 1
        except(IndexError):
            self.current_player = 1
        return self