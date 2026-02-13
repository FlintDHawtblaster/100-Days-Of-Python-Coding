import pygame
import time
import os

def play():
    audio_file = r'C:\Users\7390\Downloads\audio.mp3'

    pygame.mixer.init()
    pygame.mixer.music.load(audio_file)
    pygame.mixer.music.play()
    print()
    print("Playing some proper tunes!")
    
    while True:
        input()
        
while True:
    print("🎵MyPOD Music Player🎵")
    print()
    print("Press 1 to Play")
    print("Press 2 to Exit")
    print("Press anything else to see the menu again")
    print()
    user = int(input())
    
    if user == 1:
        play()
    elif user == 2:
        exit()
    else:
        os.system("cls")
    
    
    
