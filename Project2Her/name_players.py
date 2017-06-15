import pygame
import menu_items as m
import colors as c
from player import Player
from board import Board

class Names:
    def __init__(self, screen, state, mute, player_amount):
        self.screen = screen
        self.state = state
        self.mute = mute
        self.player_amount = player_amount
        self.key_to_alphabet = {pygame.K_a: "a", pygame.K_b: "b", pygame.K_c: "c", pygame.K_d: "d", pygame.K_e: "e",
                             pygame.K_f: "f", pygame.K_g: "g", pygame.K_h: "h", pygame.K_i: "i", pygame.K_j: "j",
                             pygame.K_k: "k", pygame.K_l: "l", pygame.K_m: "m", pygame.K_n: "n", pygame.K_o: "o",
                             pygame.K_p: "p", pygame.K_q: "q", pygame.K_r: "r", pygame.K_s: "s", pygame.K_t: "t",
                             pygame.K_u: "u", pygame.K_v: "v", pygame.K_w: "w", pygame.K_x: "x", pygame.K_y: "y",
                             pygame.K_z: "z", pygame.K_SPACE: " ", pygame.K_BACKSPACE: "", pygame.K_RETURN: ""}
        self.max_length = 10
        self.names = []
        self.counter = 1
        self.current_name = ""
    def update(self, events, mouse):
        board = Board(self.screen, self.state, self.mute)
        players = []
        self.screen.fill(c.white())
        if len(self.names) < self.player_amount: 
            titleText, titleRect = m.text_objects("Enter player " + str(self.counter) + "'s names", "large", c.black())
            titleRect.center = ((self.screen.get_width()/2), (self.screen.get_height()/10))
            if len(self.current_name) < self.max_length:
                for event in events:
                    if event.type == pygame.KEYDOWN:
                        if event.key in self.key_to_alphabet:
                            self.current_name += self.key_to_alphabet[event.key]
                            if event.key == pygame.K_BACKSPACE:
                                self.current_name = self.current_name[:-1]
                            if event.key == pygame.K_RETURN:
                                if self.current_name == "amber":
                                    self.current_name = "dombo"
                                self.names.append(self.current_name)
                                self.current_name = ""
                                self.counter += 1
            nameText, nameRect = m.text_objects(self.current_name, "large", c.black())
            nameRect.center = ((self.screen.get_width()/2), (self.screen.get_height()/2))
            self.screen.blit(nameText, nameRect)
            self.screen.blit(titleText, titleRect)
        else:
            titleText, titleRect = m.text_objects("Press start", "large", c.black())
            titleRect.center = ((self.screen.get_width()/2), (self.screen.get_height()/10))
            self.screen.blit(titleText, titleRect)
            if self.state == "win":
                start_button = m.Button(events, self.screen, mouse, c.dark_green(), c.bright_green(), "Start game", "medium", c.white(), (self.screen.get_width()/2 - 100), (self.screen.get_height()/2 - 25), 200, 50)
            elif self.state == "full":
                start_button = m.Button(events, self.screen, mouse, c.dark_green(), c.bright_green(), "Start game", "medium", c.white(), (self.screen.get_width()/2 - (100 * 2.25)), (self.screen.get_height()/2 - (25 * 2.25)), (200 * 2.25), (50 * 2.25))
            if self.player_amount == 3:
                player_1 = Player(self.names[0], c.bright_red(), c.dark_red(), board.p1start, 1)
                player_2 = Player(self.names[1], c.bright_blue(), c.dark_blue(), board.p2start, 2)
                player_3 = Player(self.names[2], c.bright_green(), c.dark_green(), board.p3start, 3)
                players.append(player_1)
                players.append(player_2)
                players.append(player_3)
            elif self.player_amount == 4:
                player_1 = Player(self.names[0], c.bright_red(), c.dark_red(), board.p1start, 1)
                player_2 = Player(self.names[1], c.bright_blue(), c.dark_blue(), board.p2start, 2)
                player_3 = Player(self.names[2], c.bright_green(), c.dark_green(), board.p3start, 3)
                player_4 = Player(self.names[3], c.bright_yellow(), c.dark_yellow(), board.p4start, 4)
                players.append(player_1)
                players.append(player_2)
                players.append(player_3)
                players.append(player_4)
            elif self.player_amount == 5:
                player_1 = Player(self.names[0], c.bright_red(), c.dark_red(), board.p1start, 1)
                player_2 = Player(self.names[1], c.bright_blue(), c.dark_blue(), board.p2start, 2)
                player_3 = Player(self.names[2], c.bright_green(), c.dark_green(), board.p3start, 3)
                player_4 = Player(self.names[3], c.bright_yellow(), c.dark_yellow(), board.p4start, 4)
                player_5 = Player(self.names[4], c.bright_purple(), c.dark_purple(), board.p5start, 5)
                players.append(player_1)
                players.append(player_2)
                players.append(player_3)
                players.append(player_4)
                players.append(player_5)
            elif self.player_amount == 6:
                player_1 = Player(self.names[0], c.bright_red(), c.dark_red(), board.p1start, 1)
                player_2 = Player(self.names[1], c.bright_blue(), c.dark_blue(), board.p2start, 2)
                player_3 = Player(self.names[2], c.bright_green(), c.dark_green(), board.p3start, 3)
                player_4 = Player(self.names[3], c.bright_yellow(), c.dark_yellow(), board.p4start, 4)
                player_5 = Player(self.names[4], c.bright_purple(), c.dark_purple(), board.p5start, 5)
                player_6 = Player(self.names[5], c.bright_pink(), c.dark_pink(), board.p6start, 6)
                players.append(player_1)
                players.append(player_2)
                players.append(player_3)
                players.append(player_4)
                players.append(player_5)
                players.append(player_6)
            if start_button.use():
                from game import Game
                new_screen = Game(self.screen, self.state, self.mute, players, board)
                return new_screen
        return self