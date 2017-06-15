import pygame

class Sound:
    def play_music():
        pygame.mixer.music.set_volume(0.2)
        pygame.mixer.music.load("Assets/Music/menumusic.mp3")
        pygame.mixer.music.play(loops = 999, start = 0)
    def stop_music():
        pygame.mixer.music.pause()