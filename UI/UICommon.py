import pygame

ScreenSize = [0, 0]
TogglePause = False
Paused = False

Blocks = []
Score = 0
keypressed = {
    pygame.K_ESCAPE: False,
    pygame.K_a: False,
    pygame.K_s: False,
    pygame.K_d: False,
    pygame.K_UP: False,
    pygame.K_DOWN: False,
    pygame.K_LEFT: False,
    pygame.K_RIGHT: False}
