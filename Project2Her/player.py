import pygame
import menu_items as m
from database import Database

class Player:
    def __init__(self, name, color, scolor, pos, id):
        self.name = name
        self.color = color
        self.scolor = scolor
        self.pos = pos
        self.id = id
        self.previous_tile = None
        self.victory = False
        self.turns = 0
        self.moves = 0
        self.has_rolled = False
        self.win_count_down = 3
    def winner(self):
        if self.victory == True:
            Database.upload_score(self.name, self.turns)
    def draw(self, screen, state):
        if state == "win":
            width = int((screen.get_width()/32) - 2)
            height = int((screen.get_height()/20) - 4.5)
            pygame.draw.circle(screen, self.color, (int(((2 + width) * self.pos[0] + 2) + width/2), int(((2 + height) * self.pos[1] + 2) + height/2)), int(0.3 * width))
        elif state == "full":
            width = int((screen.get_width()/32) - (2 * 2.25))
            height = int((screen.get_height()/20) - (4.5 * 2.25))
            pygame.draw.circle(screen, self.color, (int((((2 * 2.25) + width) * self.pos[0] + (2 * 2.25)) + width/2), int((((2 * 2.25) + height) * self.pos[1] + (2 * 2.25)) + height/2 + 2)), int(0.3 * width))
        if self.moves > 0:
            if state == "win":
                movesimg = pygame.transform.scale(pygame.image.load("Assets/Dice/" + str(self.moves) + ".png"), (50, 50))
                screen.blit(movesimg, (0, screen.get_height() - 50))
            elif state == "full":
                movesimg = pygame.transform.scale(pygame.image.load("Assets/Dice/" + str(self.moves) + ".png"), (int(50 * 2.25), int(50 * 2.25)))
                screen.blit(movesimg, (0, screen.get_height() - (50 * 2.25)))
    def update(self, events, board):
        if self.moves > 0:
            if self.pos == (30,17):
                self.winner = True
                self.moves = 0
                return True
            for event in events:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        new_pos = (self.pos[0] + 1, self.pos[1])
                    elif event.key == pygame.K_LEFT:
                        new_pos = (self.pos[0] - 1, self.pos[1])
                    elif event.key == pygame.K_UP:
                        new_pos = (self.pos[0], self.pos[1] - 1)
                    elif event.key == pygame.K_DOWN:
                        new_pos = (self.pos[0], self.pos[1] + 1)
                    for item in board.all_tiles:
                        if item != new_pos:
                            if new_pos == (1,7) or new_pos == (1,8) or new_pos == (1,9) or new_pos == (1,11) or new_pos == (1,12):
                                if self.pos == (1,10):
                                    pass
                                else:
                                    new_pos = (1,10)
                            else:
                                pass
                        elif new_pos == (0,7) or new_pos == (0,8) or new_pos == (0,9) or new_pos == (0,10) or new_pos == (0,11) or new_pos == (0,12):
                            pass                    
                        elif self.pos == (0,7) or self.pos == (0,8) or self.pos == (0,9) or self.pos == (0,10) or self.pos == (0,11) or self.pos == (0,12) and self.has_rolled:  
                            if self.moves < 4:
                                self.moves = 0
                                self.has_rolled = False
                                return True
                            else:
                                self.pos = new_pos
                                self.moves -= 1
                        elif self.pos == (30,16) and self.has_rolled:
                            if self.moves < 5:
                                self.moves = 0
                                self.has_rolled = False
                                return True
                            elif new_pos != (30,17):
                                pass
                            else:
                                self.pos = new_pos
                                self.moves = 0
                        else:
                            self.pos = new_pos
                            self.moves -= 1
        elif self.moves <= 0 and self.has_rolled:
            self.has_rolled = False
            return True
        return False