import pygame
import colors as c
import menu_items as m
from database import Database

class Highscores:
    def __init__(self, screen, state, mute):
        self.screen = screen
        self.state = state
        self.mute = mute
    def update(self, events, mouse):
        self.screen.fill(c.white())
        titleText, titleRect = m.text_objects("Highscores", "large", c.black())
        titleRect.center = ((self.screen.get_width()/2), (self.screen.get_height()/15))
        self.screen.blit(titleText, titleRect)
        self.result_table()
        if self.state == "win":
            back_button = m.Button(events, self.screen, mouse, c.dark_red(), c.bright_red(), "Back", "medium", c.white(), 0, (self.screen.get_height() - 50), 100, 50)
            newest_winner_button = m.Button(events, self.screen, mouse, c.dark_yellow(), c.bright_yellow(), "Latest score", "small", c.white(), (self.screen.get_width() - 200), (self.screen.get_height() - 50), 200, 50)
        elif self.state == "full":
            back_button = m.Button(events, self.screen, mouse, c.dark_red(), c.bright_red(), "Back", "medium", c.white(), 0, (self.screen.get_height() - (50 * 2.25)), (100 * 2.25), (50 * 2.25))
            newest_winner_button = m.Button(events, self.screen, mouse, c.dark_yellow(), c.bright_yellow(), "Latest score", "medium", c.white(), (self.screen.get_width() - (200 * 2.25)), (self.screen.get_height() - (50 * 2.25)), (200 * 2.25), (50 * 2.25))
        if back_button.use():
            from main_menu import Main_menu
            new_screen = Main_menu(self.screen, self.state, self.mute)
            return new_screen
        if newest_winner_button.use():
            from endscreen import Endscreen
            newest_winner_id = Database.get_newest_id()
            newest_winner_name = Database.get_player(newest_winner_id)[0][0]
            newest_winner_turns = Database.get_player(newest_winner_id)[0][1]
            new_screen = Endscreen(self.screen, self.state, self.mute, newest_winner_name, newest_winner_turns)
            return new_screen
        return self
    def result_table(self):
        top_5 = Database.get_top_5()
        #top of table
        placeText, placeRect = m.text_objects("Place", "large", c.black())
        placeRect.topleft = (10, ((self.screen.get_height()/7) - 28))
        nameText, nameRect = m.text_objects("Name", "large", c.black())
        nameRect.center = ((self.screen.get_width()/2), (self.screen.get_height()/7))
        scoreText, scoreRect = m.text_objects("Score", "large", c.black())
        scoreRect.topright = ((self.screen.get_width() - 10), ((self.screen.get_height()/7) - 28))
        self.screen.blit(placeText, placeRect)
        self.screen.blit(nameText, nameRect)
        self.screen.blit(scoreText, scoreRect)
        try:
            #place 1
            pygame.draw.rect(self.screen, c.black(),(0,(((self.screen.get_height()/7) * 2) - 27),self.screen.get_width(),54))
            pygame.draw.rect(self.screen, c.gold(),(0,(((self.screen.get_height()/7) * 2) - 25),self.screen.get_width(),50))
            place1Text, place1Rect = m.text_objects("1st:", "medium", c.black())
            place1Rect.topleft = (10, (((self.screen.get_height()/7) * 2) - 19))
            name1Text, name1Rect = m.text_objects(str(top_5[0][0]), "medium", c.black())
            name1Rect.center = ((self.screen.get_width()/2), ((self.screen.get_height()/7) * 2))
            score1Text, score1Rect = m.text_objects(str(top_5[0][1]) + " turns", "medium", c.black())
            score1Rect.topright = ((self.screen.get_width() - 10), (((self.screen.get_height()/7) * 2) - 19))
            self.screen.blit(place1Text, place1Rect)
            self.screen.blit(name1Text, name1Rect)
            self.screen.blit(score1Text, score1Rect)
            #place 2
            pygame.draw.rect(self.screen, c.black(),(0,(((self.screen.get_height()/7) * 3) - 27),self.screen.get_width(),54))
            pygame.draw.rect(self.screen, c.silver(),(0,(((self.screen.get_height()/7) * 3) - 25),self.screen.get_width(),50))
            place2Text, place2Rect = m.text_objects("2nd:", "medium", c.black())
            place2Rect.topleft = (10, (((self.screen.get_height()/7) * 3) - 19))
            name2Text, name2Rect = m.text_objects(str(top_5[1][0]), "medium", c.black())
            name2Rect.center = ((self.screen.get_width()/2), ((self.screen.get_height()/7) * 3))
            score2Text, score2Rect = m.text_objects(str(top_5[1][1]) + " turns", "medium", c.black())
            score2Rect.topright = ((self.screen.get_width() - 10), (((self.screen.get_height()/7) * 3) - 19))
            self.screen.blit(place2Text, place2Rect)
            self.screen.blit(name2Text, name2Rect)
            self.screen.blit(score2Text, score2Rect)
            #place 3
            pygame.draw.rect(self.screen, c.black(),(0,(((self.screen.get_height()/7) * 4) - 27),self.screen.get_width(),54))
            pygame.draw.rect(self.screen, c.bronze(),(0,(((self.screen.get_height()/7) * 4) - 25),self.screen.get_width(),50))
            place3Text, place3Rect = m.text_objects("3rd:", "medium", c.black())
            place3Rect.topleft = (10, (((self.screen.get_height()/7) * 4) - 19))
            name3Text, name3Rect = m.text_objects(str(top_5[2][0]), "medium", c.black())
            name3Rect.center = ((self.screen.get_width()/2), ((self.screen.get_height()/7) * 4))
            score3Text, score3Rect = m.text_objects(str(top_5[2][1]) + " turns", "medium", c.black())
            score3Rect.topright = ((self.screen.get_width() - 10), (((self.screen.get_height()/7) * 4) - 19))
            self.screen.blit(place3Text, place3Rect)
            self.screen.blit(name3Text, name3Rect)
            self.screen.blit(score3Text, score3Rect)
            #place 4
            place4Text, place4Rect = m.text_objects("4th:", "medium", c.black())
            place4Rect.topleft = (10, (((self.screen.get_height()/7) * 5) - 19))
            name4Text, name4Rect = m.text_objects(str(top_5[3][0]), "medium", c.black())
            name4Rect.center = ((self.screen.get_width()/2), ((self.screen.get_height()/7) * 5))
            score4Text, score4Rect = m.text_objects(str(top_5[3][1]) + " turns", "medium", c.black())
            score4Rect.topright = ((self.screen.get_width() - 10), (((self.screen.get_height()/7) * 5) - 19))
            self.screen.blit(place4Text, place4Rect)
            self.screen.blit(name4Text, name4Rect)
            self.screen.blit(score4Text, score4Rect)
            #place 5
            place5Text, place5Rect = m.text_objects("5th:", "medium", c.black())
            place5Rect.topleft = (10, (((self.screen.get_height()/7) * 6) - 28))
            name5Text, name5Rect = m.text_objects(str(top_5[4][0]), "medium", c.black())
            name5Rect.center = ((self.screen.get_width()/2), ((self.screen.get_height()/7) * 6))
            score5Text, score5Rect = m.text_objects(str(top_5[4][1]) + " turns", "medium", c.black())
            score5Rect.topright = ((self.screen.get_width() - 10), (((self.screen.get_height()/7) * 6) - 19))
            self.screen.blit(place5Text, place5Rect)
            self.screen.blit(name5Text, name5Rect)
            self.screen.blit(score5Text, score5Rect)
        except IndexError:
            pass