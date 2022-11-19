import numpy as np
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

from freetype import *
import UI.UICommon as UICommon


class UIText():
    def __init__(self, text = "", x = 0, y = UICommon.ScreenSize[1], align = "left", valign = "top", visible = True, font = 'arial'):
        self.text = text
        # origin in bottom left
        self.align, self.valign = align, valign
        self.x, self.y = x, y
        self.visible = visible
        self.font = pygame.font.SysFont(font, 64)
        self.textSurface = self.font.render(self.text, True, (255, 255, 255, 255), (0, 0, 0, 0))
        # text color, bg color
        # Get width and height
        self.width, self.height = self.textSurface.get_width(), self.textSurface.get_height()
        self.textData = pygame.image.tostring(self.textSurface, "RGBA", True)
        
        

    def _DrawText(self):
        glDrawPixels(self.width, self.height, GL_RGBA, GL_UNSIGNED_BYTE, self.textData)

    def Update(self, deltaTime):
        pass
        #super().Update(deltaTime)

    def Render(self):
        if self.align == "left":
            self.x = 0
        elif self.align == "center":
            self.x = UICommon.ScreenSize[0]/2-self.textSurface.get_width()/2
        elif self.align == "right":
            self.x = UICommon.ScreenSize[0] - self.textSurface.get_width()
        if self.valign == "top":
            self.y = UICommon.ScreenSize[1] - self.textSurface.get_height()
        elif self.valign == "center":
            self.y = UICommon.ScreenSize[1]/2-self.textSurface.get_height()/2
        elif self.valign == "bottom":
            self.y = 0
        glWindowPos2d(self.x, self.y)
        if self.visible:
            self._DrawText()
        #super().Render(screen)

    

   



        

        

