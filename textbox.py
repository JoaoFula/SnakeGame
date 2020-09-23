import pygame as pg
pg.init()


class Textbox:
    def __init__(self, surface, x, y, sizex=50, sizey=50, caption="",
                 text="", font_size=22, font_color=(0, 0, 0), text_offset=(-35, 1),
                 outline_color=(255,255,255), color_active=(25,25,25), color_inactive=(10,10,10)):
        self.surface = surface
        self.color_active = color_active
        self.color_inactive = color_inactive
        self.color = color_inactive
        self.x = x
        self.y = y
        self.text = text
        self.sizex = sizex
        self.sizey = sizey
        self.caption = caption
        self.outline_color = outline_color
        self.font_size = font_size
        self.font_color = font_color
        self.text_offset = text_offset
        self.checkbox_obj = pg.Rect(self.x, self.y, 12, 12)
        self.checkbox_outline = self.checkbox_obj.copy()
        self.active = False



    def _draw_button_text(self):
        self.font = pg.font.Font(None, self.font_size)
        self.font_surf = self.font.render(self.caption, True, self.font_color)
        w, h = self.font.size(self.caption)
        self.font_pos = (self.x + 12 / 2 - w / 2 + self.text_offset[0], self.y + 12 / 2 - h / 2 + self.text_offset[1])
        self.surface.blit(self.font_surf, self.font_pos)

    def render_textbox(self):
        pg.draw.rect(self.surface, (255,255,255), self.checkbox_obj)
        pg.draw.rect(self.surface, self.outline_color, self.checkbox_outline, 1)
        font = pg.font.Font(None, self.font_size)
        txt_surface = font.render(self.text, True, self.color)
        width = max(200, txt_surface.get_width() + 10)
        self.checkbox_obj.w = width
        # Blit the text.
        self.surface.blit(txt_surface, (self.checkbox_obj.x + 5, self.checkbox_obj.y ))
        # Blit the input_box rect.
        #pg.draw.rect( self.surface, self.color, self.checkbox_obj, 2)
        self._draw_button_text()

    def update_textbox(self, event_object):
        if event_object.type == pg.MOUSEBUTTONDOWN:
            if self.checkbox_obj.collidepoint(event_object.pos):
                self.active = True
            else:
                self.active = False
            self.color = self.color_active if self.active else self.color_inactive

        if event_object.type == pg.KEYDOWN:
            if self.active:
                if event_object.key == pg.K_RETURN:
                    print(self.text)

                elif event_object.key == pg.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event_object.unicode