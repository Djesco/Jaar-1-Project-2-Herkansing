import pygame
import menu_items as m
import colors as c

class Board:
    def __init__(self, screen, state, mute):
        self.screen = screen
        self.state = state
        self.mute = mute
        self.margin = 2
        self.columns = 32
        self.rows = 20
        self.width = int((screen.get_width()/self.columns) - self.margin)
        if state == "win":
            self.height = int((screen.get_height()/self.rows) - self.margin - 2.5)
        elif state == "full":
            self.height = int((screen.get_height()/self.rows) - self.margin - (2.5 * 2.25))
        #lists
        self.whitetiles = [(1,10), (2,0), (2,1), (2,2), (2,3), (2,4), (2,6), (2,7), (2,12), (2,13), (2,14), (2,15), (2,17), (2,18), (2,19), (3,0), (3,10), (3,19), (4,10), (4,19), (5,0), (5,9), (6,0), (6,9), (7,0), (7,8), (7,9), (7,10), (7,11), (7,12), (7,14), (7,15), (8,0), (8, 1), (8,6), (8,11), (8,15), (8,17), (9,0), (9,11), (9,15), (9,16), (10,0), (10,7), (10,8), (10,19), (11,0), (11,15), (11,19), (12,1), (12, 2), (12, 3), (12,5), (12,6), (12,8), (12,15), (12,19), (13,0), (13, 3), (13,6), (13,7), (13,13), (13,19), (14,0), (14,13), (14,4), (15,3), (15,19), (17,0), (17,13), (17,16), (17,17), (17,19), (18,0), (18,3), (18,16), (18,19), (19,0), (19,3), (19,12), (19,13), (19,16), (19,19), (20,0), (20,6), (20,10), (20,13), (20,14), (20,15), (20,16), (21,6), (21,10), (21,17), (21,19), (22,0), (22,6), (22,7), (22,9), (22,17), (22,19), (23,14), (23,16), (23,17), (23,19), (24,0), (24,4), (24,5), (24,6), (24,13), (24,19), (25,0), (25,13), (25,19), (26,4), (26,5), (26,7), (26,9), (26,10), (26,12), (26,13), (26,19), (27,0), (27,4), (27,11), (27,17), (27,18), (28,0), (28,5), (28,11),(29,0), (30,0), (30,11), (31,0), (31,2), (31,4), (31,5), (31,10), (31,11), (31,12), (31,13), (31,14), (31,15)]
        self.landmarks = [(4,0), (8,2), (7,17), (11,8), (12,14), (14,19), (27,19), (29,16), (31,3), (25,4), (26,8), (21,0), (14,3), (23,15), (19,11), (19,4), (29,11)]
        self.policelandmark = [(16,11)]
        self.policeline = [(16,2), (16,3), (16,7), (16,9), (16,10), (16,12), (16,19)]
        self.pu3 = [(16,1)] #policeline
        self.policelinetile = [(16,0)] #policeline
        self.policelinechance = [(16, 8)]
        self.policetiles = [(7,6), (10,15), (20,17), (28,4), (19,10)]
        self.chancecards = [(2,5), (2,16), (4,9), (7,7), (7,13), (9,17), (12,0), (12,4), (12,13), (13,8), (15,0), (17,3), (18,13), (20,19), (22,8), (23,6), (23,13), (26,0), (26,6), (26,11), (31,1), (31,9), (31,16)]
        self.arena1 = [(9,2), (10,4), (10,5), (9,6)]
        self.pu9 = [(10,3)] #arena1
        self.arena1chance = [(10,2), (10,6)] #arena1
        self.arena2 = [(11,11), (12,11), (12,12)]
        self.pu1 = [(10,11)] #arena2
        self.arena3 = [(5,19), (6,19), (7,18), (8,19)]
        self.pu8 = [(9,19)] #arena3
        self.arena3chance = [(7,19)] #arena3
        self.arena4 = [(14,5), (14,6), (15,6), (18,6), (19,5)]
        self.pu4 = [(17,6)] #arena4
        self.policelinearena4 = [(16,6)] #arena4
        self.arena4chance = [(19,6)] #arena4
        self.arena5 = [(15,13), (15,14), (15,15)]
        self.policelinearena5 = [(16,13), (16,16)] #arena5
        self.arena5chance = [(15,16)] #arena5
        self.arena6 = [(28,6), (29,6), (30,6), (31,6), (31,7)]
        self.pu6 = [(31,8)] #arena6
        self.arena7 = [(27,14), (27,15), (28,16)]
        self.pu7 = [(27,13)] #arena7
        self.arena7chance = [(27,16)] #arena7
        self.pu2 = [(22,10)]
        self.pu5 = [(17,18)]
        self.pu10 = [(23,0)]
        self.final_tile = [(30,16)]
        self.finish = [(30,17)]
        self.rotterdam_centraal = [(2,8), (2,9), (2,10), (2,11)]
        self.p1start = (0,7)
        self.p2start = (0,8)
        self.p3start = (0,9)
        self.p4start = (0,10)
        self.p5start = (0,11)
        self.p6start = (0,12)
        self.starts = [(0,7), (0,8), (0,9), (0,10), (0,11), (0,12)]
        self.all_tiles = [(16,11),(16,2), (16,3), (16,7), (16,9), (16,10), (16,12), (16,19),(16,1),(16,0),(16, 8),(7,6), (10,15), (20,17), (28,4), (19,10),(2,5), (2,16), (4,9), (7,7), (7,13), (9,17), (12,0), (12,4), (12,13), (13,8), (15,0), (17,3), (18,13), (20,19), (22,8), (23,6), (23,13), (26,0), (26,6), (26,11), (31,1), (31,9), (31,16),(9,2), (10,4), (10,5), (9,6),(10,3),(10,2), (10,6),(11,11), (12,11), (12,12),(10,11),(5,19), (6,19), (7,18), (8,19), (9,19), (7,19), (14,5), (14,6), (15,6), (18,6), (19,5), (17,6), (16,6), (19,6), (15,13), (15,14), (15,15), (16,13), (16,16), (4,0), (8,2), (7,17), (11,8), (12,14), (14,19), (27,19), (29,16), (31,3), (25,4), (26,8), (21,0), (14,3), (23,15), (19,11), (19,4), (29,11), (15,16), (28,6), (29,6), (30,6), (31,6), (31,7), (31,8), (27,14), (27,15), (28,16), (27,13), (27,16), (22,10), (17,18), (23,0), (30,16), (30,17), (0,7), (0,8), (0,9), (0,10), (0,11), (0,12), (2,8), (2,9), (2,10), (2,11), (1,10), (2,0), (2,1), (2,2), (2,3), (2,4), (2,6), (2,7), (2,12), (2,13), (2,14), (2,15), (2,17), (2,18), (2,19), (3,0), (3,10), (3,19), (4,10), (4,19), (5,0), (5,9), (6,0), (6,9), (7,0), (7,8), (7,9), (7,10), (7,11), (7,12), (7,14), (7,15), (8,0), (8, 1), (8,6), (8,11), (8,15), (8,17), (9,0), (9,11), (9,15), (9,16), (10,0), (10,7), (10,8), (10,19), (11,0), (11,15), (11,19), (12,1), (12, 2), (12, 3), (12,5), (12,6), (12,8), (12,15), (12,19), (13,0), (13, 3), (13,6), (13,7), (13,13), (13,19), (14,0), (14,13), (14,4), (15,3), (15,19), (17,0), (17,13), (17,16), (17,17), (17,19), (18,0), (18,3), (18,16), (18,19), (19,0), (19,3), (19,12), (19,13), (19,16), (19,19), (20,0), (20,6), (20,10), (20,13), (20,14), (20,15), (20,16), (21,6), (21,10), (21,17), (21,19), (22,0), (22,6), (22,7), (22,9), (22,17), (22,19), (23,14), (23,16), (23,17), (23,19), (24,0), (24,4), (24,5), (24,6), (24,13), (24,19), (25,0), (25,13), (25,19), (26,4), (26,5), (26,7), (26,9), (26,10), (26,12), (26,13), (26,19), (27,0), (27,4), (27,11), (27,17), (27,18), (28,0), (28,5), (28,11),(29,0), (30,0), (30,11), (31,0), (31,2), (31,4), (31,5), (31,10), (31,11), (31,12), (31,13), (31,14), (31,15), (16,11)]
    def draw(self):
        white_tile = pygame.transform.scale(pygame.image.load("Assets/Tiles/WhiteTile.png"), (self.width, self.height))
        normal_landmark = pygame.transform.scale(pygame.image.load("Assets/Tiles/Landmark.png"), (self.width, self.height))
        police_landmark = pygame.transform.scale(pygame.image.load("Assets/Tiles/PoliceLandmark.png"), (self.width, self.height))
        police_line = pygame.transform.scale(pygame.image.load("Assets/Tiles/PoliceLine.png"), (self.width, self.height))
        police_tile = pygame.transform.scale(pygame.image.load("Assets/Tiles/PoliceTile.png"), (self.width, self.height))
        police_line_tile = pygame.transform.scale(pygame.image.load("Assets/Tiles/PoliceLineTile.png"), (self.width, self.height))
        police_line_chance = pygame.transform.scale(pygame.image.load("Assets/Tiles/PoliceChance.png"), (self.width, self.height))
        chance_card = pygame.transform.scale(pygame.image.load("Assets/Tiles/ChanceCard.png"), (self.width, self.height))
        arena_tile = pygame.transform.scale(pygame.image.load("Assets/Tiles/Arena.png"), (self.width, self.height))
        arena_chance = pygame.transform.scale(pygame.image.load("Assets/Tiles/ChanceArena.png"), (self.width, self.height))
        police_line_arena = pygame.transform.scale(pygame.image.load("Assets/Tiles/PoliceArena.png"), (self.width, self.height))
        pu1bike = pygame.transform.scale(pygame.image.load("Assets/Tiles/Bike.png"), (self.width, self.height))
        pu2taxi = pygame.transform.scale(pygame.image.load("Assets/Tiles/Taxi.png"), (self.width, self.height))
        pu3sniper = pygame.transform.scale(pygame.image.load("Assets/Tiles/Sniper.png"), (self.width, self.height))
        pu4ufo = pygame.transform.scale(pygame.image.load("Assets/Tiles/Ufo.png"), (self.width, self.height))
        pu5camo = pygame.transform.scale(pygame.image.load("Assets/Tiles/Camo.png"), (self.width, self.height))
        pu6plusultra = pygame.transform.scale(pygame.image.load("Assets/Tiles/PlusUltra.png"), (self.width, self.height))
        pu7slowdown = pygame.transform.scale(pygame.image.load("Assets/Tiles/SlowDownTime.png"), (self.width, self.height))
        pu8fusrodah = pygame.transform.scale(pygame.image.load("Assets/Tiles/FusRoDah.png"), (self.width, self.height))
        pu9wildfire = pygame.transform.scale(pygame.image.load("Assets/Tiles/WildFire.png"), (self.width, self.height))
        pu10respu = pygame.transform.scale(pygame.image.load("Assets/Tiles/ResurrectEssence.png"), (self.width, self.height))
        final_tile = pygame.transform.scale(pygame.image.load("Assets/Tiles/End.png"), (self.width, self.height))
        rcc1 = pygame.transform.scale(pygame.image.load("Assets/Tiles/RCcorner1.png"), (self.width, self.height))
        rcc2 = pygame.transform.scale(pygame.image.load("Assets/Tiles/RCcorner2.png"), (self.width, self.height))
        rcc = pygame.transform.scale(pygame.image.load("Assets/Tiles/RCcenter.png"), (self.width, self.height))
        if self.state == "win":
            boat = pygame.transform.scale(pygame.image.load("Assets/Tiles/Boat.png"), (self.width * 3 - 8, self.height * 4 + 22))
        elif self.state == "full":
            boat = pygame.transform.scale(pygame.image.load("Assets/Tiles/Boat.png"), (self.width * 3 - 25, self.height * 4 + 22))
        boat = pygame.transform.rotate(boat, 90)
        self.screen.fill(c.white())
        for column in range(self.columns):
            for row in range(self.rows):
                tile_size = (((self.margin + self.width) * column + self.margin), ((self.margin + self.height) * row + self.margin))
                if (column, row) in self.whitetiles or (column, row) in self.starts: 
                    self.screen.blit(white_tile, tile_size)
                elif (column, row) in self.landmarks:
                    self.screen.blit(normal_landmark, tile_size)
                elif (column, row) in self.policelandmark:
                    self.screen.blit(police_landmark, tile_size)
                elif (column, row) in self.policeline:
                    self.screen.blit(police_line, tile_size)
                elif (column, row) in self.policetiles:
                    self.screen.blit(police_tile, tile_size)
                elif (column, row) in self.chancecards:
                    self.screen.blit(chance_card, tile_size)
                elif (column, row) in self.arena1 or (column, row) in self.arena2 or (column, row) in self.arena3 or (column, row) in self.arena4 or (column, row) in self.arena5 or (column, row) in self.arena6 or (column, row) in self.arena7:
                    self.screen.blit(arena_tile, tile_size)
                elif (column, row) in self.pu1:
                    self.screen.blit(pu1bike, tile_size)
                elif (column, row) in self.pu2:
                    self.screen.blit(pu2taxi, tile_size)
                elif (column, row) in self.pu3:
                    self.screen.blit(pu3sniper, tile_size)
                elif (column, row) in self.pu4:
                    self.screen.blit(pu4ufo, tile_size)
                elif (column, row) in self.pu5:
                    self.screen.blit(pu5camo, tile_size)
                elif (column, row) in self.pu6:
                    self.screen.blit(pu6plusultra, tile_size)
                elif (column, row) in self.pu7:
                    self.screen.blit(pu7slowdown, tile_size)
                elif (column, row) in self.pu8:
                    self.screen.blit(pu8fusrodah, tile_size)
                elif (column, row) in self.pu9:
                    self.screen.blit(pu9wildfire, tile_size)
                elif (column, row) in self.pu10:
                    self.screen.blit(pu10respu, tile_size)
                elif (column, row) in self.policelinearena4 or (column, row) in self.policelinearena5:
                    self.screen.blit(police_line_arena, tile_size)
                elif (column, row) in self.policelinetile:
                    self.screen.blit(police_line_tile, tile_size)
                elif (column, row) in self.arena1chance or (column, row) in self.arena3chance or (column, row) in self.arena4chance or (column, row) in self.arena5chance or (column, row) in self.arena7chance:
                    self.screen.blit(arena_chance, tile_size)
                elif (column, row) in self.final_tile:
                    self.screen.blit(final_tile, tile_size)
                elif (column, row) in self.policelinechance:
                    self.screen.blit(police_line_chance, tile_size)
                elif (column, row) in self.rotterdam_centraal:
                    if (column, row) == (2,8):
                        self.screen.blit(rcc1, tile_size)
                    elif (column, row) == (2,11):
                        self.screen.blit(rcc2, tile_size)
                    else:
                        self.screen.blit(rcc, tile_size)
                else:
                    pass
        if self.state == "win":
            self.screen.blit(boat, ((self.screen.get_width() - boat.get_width()), (self.screen.get_height() - boat.get_height() - 50)))
        elif self.state == "full":
            self.screen.blit(boat, ((self.screen.get_width() - boat.get_width()), (self.screen.get_height() - boat.get_height()- (50 * 2.25))))