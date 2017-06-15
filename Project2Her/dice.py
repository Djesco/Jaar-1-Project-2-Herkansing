import pygame
from time import sleep
from random import randint

class Dice:
    def roll(screen):
        for number in range(100):
            current = randint(1, 6)
            diceroll = pygame.image.load("Assets/Dice/" + str(current) + ".png")
            screen.blit(diceroll, (100, 100))
            pygame.display.update()
        final_roll = randint(1, 6)
        return final_roll

#nu er voor zorgen dat de final gooi langer in beeld blijft staan