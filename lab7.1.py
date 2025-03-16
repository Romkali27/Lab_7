import pygame
import os

pygame.init()

# Music Player Setup
music_files = ["song1.mp3", "song2.mp3", "song3.mp3"]
current_track = 0

def play_music():
    pygame.mixer.music.load(music_files[current_track])
    pygame.mixer.music.play()

if os.path.exists(music_files[current_track]):
    play_music()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if pygame.mixer.music.get_busy():
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.unpause()
            elif event.key == pygame.K_s:
                pygame.mixer.music.stop()
            elif event.key == pygame.K_n:
                current_track = (current_track + 1) % len(music_files)
                play_music()
            elif event.key == pygame.K_p:
                current_track = (current_track - 1) % len(music_files)
                play_music()

pygame.quit()
