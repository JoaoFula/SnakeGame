import pygame as pg
pg.init()


class Tuner:
    def __init__(self, surface, x, y, sizex=50, sizey=50, init_value=5, caption="",
                 font_size=22, font_color=(0, 0, 0), text_offset=(-36, 1),
                 outline_color=(255,255,255), color_active=(25,25,25), color_inactive=(10,10,10)):
        self.surface = surface
        self.color_active = color_active
        self.color_inactive = color_inactive
        self.color = color_inactive
        self.x = x
        self.y = y
        self.value = init_value
        self.sizex = sizex
        self.sizey = sizey
        self.caption = caption
        self.outline_color = outline_color
        self.font_size = font_size
        self.font_color = font_color
        self.text_offset = text_offset
        self.checkbox_obj = pg.Rect(self.x, self.y, 12, 12)
        self.checkbox_outline = self.checkbox_obj.copy()
        self.checkbox_obj_plus = pg.Rect(self.x+18, self.y-4, 10, 10)
        self.checkbox_obj_minus = pg.Rect(self.x+18, self.y+9, 10, 10)

    def _draw_button_text(self):
        self.font = pg.font.Font(None, self.font_size)
        self.font_surf = self.font.render(self.caption, True, self.font_color)
        w, h = self.font.size(self.caption)
        self.font_pos = (
        self.x + 12 / 2 - w / 2 + self.text_offset[0], self.y + 12 / 2 - h / 2 + self.text_offset[1])
        self.surface.blit(self.font_surf, self.font_pos)

    def render_tuner(self):
        pg.draw.rect(self.surface, (255, 255, 255), self.checkbox_obj)
        pg.draw.rect(self.surface, self.outline_color, self.checkbox_outline, 1)
        font = pg.font.Font(None, self.font_size)
        txt_surface = font.render(str(self.value), True, self.color)
        width = max(10, txt_surface.get_width())
        self.checkbox_obj.w = width
        # Blit the text.
        self.surface.blit(txt_surface, (self.checkbox_obj.x + 5, self.checkbox_obj.y))
        self._draw_button_text()
        pg.draw.circle(self.surface, (200, 200, 250), self.checkbox_obj_plus.center, 6)
        pg.draw.circle(self.surface, (200, 200, 250), self.checkbox_obj_minus.center, 6)
        pg.draw.line(self.surface, (100, 100, 100),
                     (self.checkbox_obj_plus.center[0]-1,self.checkbox_obj_plus.center[1] + 4 ),
                     (self.checkbox_obj_plus.center[0]-1,self.checkbox_obj_plus.center[1] - 5 ), 2)
        pg.draw.line(self.surface, (100, 100, 100),
                     (self.checkbox_obj_plus.center[0]+4, self.checkbox_obj_plus.center[1]-1),
                     (self.checkbox_obj_plus.center[0]-5, self.checkbox_obj_plus.center[1]-1), 2)

        pg.draw.line(self.surface, (100, 100, 100),
                     (self.checkbox_obj_minus.center[0] + 4, self.checkbox_obj_minus.center[1] - 1),
                     (self.checkbox_obj_minus.center[0] - 5, self.checkbox_obj_minus.center[1] - 1), 2)

    def _update(self, event_object):
        x, y = event_object.pos
        # self.x, self.y, 12, 12
        px, py, w, h = self.checkbox_obj_plus  # getting check box dimensions
        px1, py1, w1, h1 = self.checkbox_obj_minus
        if px < x < px + w and py < y < py + h:
            self.active = True
        else:
            self.active = False
        if px1 < x < px1 + w1 and py1 < y < py1 + h1:
            self.active1 = True
        else:
            self.active1 = False

    def _mouse_up(self):
            if self.active and self.click:
                    self.value += 1
            elif self.active1 and self.click:
                self.value -= 1
            self.value = min(max(self.value, 1), 9)

    def update_tuner(self, event_object):
        if event_object.type == pg.MOUSEBUTTONDOWN:
            self.click = True
            # self._mouse_down()
        if event_object.type == pg.MOUSEBUTTONUP:
            self._mouse_up()
        if event_object.type == pg.MOUSEMOTION:
            self._update(event_object)

