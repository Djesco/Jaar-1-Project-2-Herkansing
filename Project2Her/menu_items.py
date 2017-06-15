import pygame
import colors as c

def text_objects(text, size, color):
    largeText = pygame.font.Font(None, 75)
    mediumText = pygame.font.Font(None, 50)
    smallText = pygame.font.Font(None, 37)
    if size == "large":
        font = largeText
    elif size == "medium":
        font = mediumText
    elif size == "small":
        font = smallText
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()

class Button:
    def __init__(self, events, screen, mouse, primary_button_color, secondary_button_color, button_text, text_size, text_color, x, y, x_size, y_size):
        self.events = events
        self.screen = screen
        self.mouse = mouse
        self.primary_button_color = primary_button_color
        self.secondary_button_color = secondary_button_color
        self.button_text = button_text
        self.text_size = text_size
        self.text_color = text_color
        self.x = x
        self.y = y
        self.x_size = x_size
        self.y_size = y_size
    def use(self):
        buttonText, buttonRect = text_objects(str(self.button_text), self.text_size, self.text_color) 
        buttonRect.center = ((self.x + (self.x_size/2)), (self.y + (self.y_size/2)))  
        pygame.draw.rect(self.screen, c.black(), ((self.x - 2), (self.y - 2), (self.x_size + 4), self.y_size + 4))  
        if (self.x + self.x_size > self.mouse[0] > self.x) and (self.y + self.y_size > self.mouse[1] > self.y):
            pygame.draw.rect(self.screen, self.secondary_button_color, (self.x, self.y, self.x_size, self.y_size))
            for event in self.events:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    return True
        else:
            pygame.draw.rect(self.screen, self.primary_button_color, (self.x, self.y, self.x_size, self.y_size))
        self.screen.blit(buttonText, buttonRect)

class Vector2:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def is_same(self, v2):
        return self.x == v2.x and self.y == v2.y