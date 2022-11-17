from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GL import shaders

import freetype as ft

class UIText():
    def __init__(self, text = None):
        face = ft.Face("Vera.ttf")
        face.set_char_size(48*64)
        # Add Stroke
        # stroker = ft.Stroker()
        # stroker.set(1, ft.FT_STROKER_LINECAPS['FT_STROKER_LINECAP_ROUND'], ft.FT_STROKER_LINEJOINS['FT_STROKER_LINEJOIN_ROUND'], 0)
        # override default load flags to avoid rendering the character during loading
        face.load_char('S', ft.FT_LOAD_FLAGS['FT_LOAD_DEFAULT'])
        # initialize C FreeType Glyph object
        # glyph = ft.FT_Glyph()
        # # get every glyph from the face
        # ft.FT_Get_Glyph(face.glyph._FT_GlyphSlot, ft.byref(glyph))
        # # initialize Python FreeType Glyph object
        # glyph = ft.Glyph(glyph)
        # # stroke border and check errors
        # error = ft.FT_Glyph_StrokeBorder(ft.byref(glyph._FT_Glyph), stroker._FT_Stroker, False, False)
        # if error:
        #     raise ft.FT_Exception(error)
        # # bitmapGlyph is the rendered glyph that we want
        # bitmapGlyph = glyph.to_bitmap(ft.FT_RENDER_MODES['FT_RENDER_MODE_NORMAL'], 0)
        bitmap = face.glyph.bitmap
        print (bitmap.buffer)

        pass

    def Update(self, deltaTime):
        pass
        #super().Update(deltaTime)

    def Render(self, screen):
        pass
        #super().Render(screen)