#!usr/local/bin python3

import pygame
import random
import tkinter as tk
from tkinter import messagebox

pygame.init()
green = (0, 200, 0)
red = (200, 0, 0)

bright_green = (0, 255, 0)
bright_red = (255, 0, 0)


class cube(object):
    rows = 20
    w = 500
    def __init__(self, start, dirnx=1, dirny=0, color=(0,255,0)):
        self.pos = start
        self.dirnx = dirnx
        self.dirny = dirny
        self.color = color

    def move(self, dirnx, dirny):
        self.dirnx = dirnx
        self.dirny = dirny
        self.pos = (self.pos[0] + self.dirnx, self.pos[1] + self.dirny)

    def draw(self, surface, eyes=False):
        dis = self.w // self.rows
        i = self.pos[0]
        j = self.pos[1]

        pygame.draw.rect(surface, self.color, (i*dis+1, j*dis+1, dis-2, dis-2))
        if eyes:
            center = dis//2
            radius = 3
            circle_middle = (i*dis+center-radius, j*dis+8)
            circle_middle_2 = (i * dis + dis - radius*2, j * dis + 8)
            pygame.draw.circle(surface, (0, 0, 0), circle_middle, radius)
            pygame.draw.circle(surface, (0, 0, 0), circle_middle_2, radius)


class snake(object):
    body = []
    turns = {}
    def __init__(self, color, pos):
        self.color = color
        self.head = cube(pos)
        self.body.append(self.head)
        self.dirnx = 0
        self.dirny = 1

    def move(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            keys = pygame.key.get_pressed()
            for key in keys:
                if keys[pygame.K_LEFT]:
                    if self.dirnx == 0:
                        self.dirnx = -1
                        self.dirny = 0
                        self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]

                elif keys[pygame.K_RIGHT]:
                    if self.dirnx == 0:
                        self.dirnx = 1
                        self.dirny = 0
                        self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]

                elif keys[pygame.K_UP]:
                    if self.dirny == 0:
                        self.dirnx = 0
                        self.dirny = -1
                        self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]

                elif keys[pygame.K_DOWN]:
                    if self.dirny == 0:
                        self.dirnx = 0
                        self.dirny = 1
                        self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]

        for i, c in enumerate(self.body):
            p = c.pos[:]
            if p in self.turns:
                turn = self.turns[p]
                c.move(turn[0], turn[1])
                if i == len(self.body)-1:
                    self.turns.pop(p)
            else:
                # Check hitboxes with the screen edges
                if c.dirnx == -1 and c.pos[0] <= 0: c.pos = (c.rows-1, c.pos[1])
                elif c.dirnx == 1 and c.pos[0] >= c.rows-1: c.pos = (0, c.pos[1])
                elif c.dirny == 1 and c.pos[1] >= c.rows-1: c.pos = (c.pos[0], 0)
                elif c.dirny == -1 and c.pos[1] <= 0: c.pos = (c.pos[0], c.rows-1)
                else: c.move(c.dirnx, c.dirny)

    def reset(self, pos):
        self.body = []
        self.turns = {}
        self.head = cube(pos)
        self.body.append(self.head)
        self.dirnx = 0
        self.dirny = 1



    def add_cube(self):
        tail = self.body[-1]
        dx, dy = tail.dirnx, tail.dirny

        if dx == 1 and dy == 0:
            self.body.append(cube((tail.pos[0] - 1, tail.pos[1])))
        elif dx == -1 and dy == 0:
            self.body.append(cube((tail.pos[0] + 1, tail.pos[1])))
        elif dx == 0 and dy == 1:
            self.body.append(cube((tail.pos[0], tail.pos[1] - 1)))
        elif dx == 0 and dy == -1:
            self.body.append(cube((tail.pos[0], tail.pos[1] + 1)))

        self.body[-1].dirnx = dx
        self.body[-1].dirny = dy

    def draw(self, surface):
        for i, c in enumerate(self.body):
            if i == 0:
                c.draw(surface, True)
            else:
                c.draw(surface)


def draw_grid(w, rows, surface):
    size_between = width // rows
    x, y = 0, 0
    for l in range(rows):
        x = x + size_between
        y = y + size_between
        pygame.draw.line(surface, (255, 255, 255), (x,0), (x,w))
        pygame.draw.line(surface, (255, 255, 255), (0,y), (w, y))


def redraw_window(surface):
    global rows, width, s, snack
    surface.fill((0,0,0))
    s.draw(surface)
    snack.draw(surface)
    draw_grid(width, rows, surface)
    pygame.display.update()


def random_snack(rows, snake):
    positions = snake.body

    while True:
        x = random.randrange(rows)
        y = random.randrange(rows)
        if len(list(filter(lambda z:z.pos == (x,y), positions))) > 0:
            continue
        else:
            break
    return (x,y)


def message_box(subject, content):
    root = tk.Tk()
    root.resizable(0, 0)
    root.geometry('250x100')
    root.attributes("-topmost", True)
    root.withdraw()
    messagebox.showinfo(subject, content)
    try:
        root.destroy()
    except:
        pass

def text_objects(text, font):
    text_surface = font.render(text, True, (0, 0, 0))
    return text_surface, text_surface.get_rect()

def button(surface, msg, inactive_color, active_color, position, clock, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if position[0] + position[2] > mouse[0] > position[0] and position[1] + position[3] > mouse[1] > position[1]:
        pygame.draw.rect(surface, active_color, position)
        if click[0] == 1 and action is not None:
            if action == "play":
                game_loop(True, surface, clock)
            else:
                pygame.quit()
    else:
        pygame.draw.rect(surface, inactive_color, position)

    small_text = pygame.font.Font('freesansbold.ttf', 20)
    text_surf, text_rect = text_objects(msg, small_text)
    text_rect.center = (position[0] + position[2] // 2, (position[1] + position[3] // 2))
    surface.blit(text_surf, text_rect)


def game_intro(surface, clock):
    global width
    intro = True

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        surface.fill((255, 255, 255))
        large_text = pygame.font.Font('freesansbold.ttf', 50)
        text_surf, text_rect = text_objects("A Snake clone", large_text)
        text_rect.center = ((width//2), (width//2)-50)
        surface.blit(text_surf, text_rect)
        button(surface, 'PLAY', green, bright_green, (2 * width // 10, 2 * width // 3, 100, 50), clock, "play")
        button(surface, 'EXIT', red, bright_red,  (8 * width // 10 - 100, 2 * width // 3, 100, 50), clock, "quit" )
        pygame.display.update()
        clock.tick(15)

def game_loop(flag, win, clock):
    global width, rows, s, snack
    s = snake((0, 255, 0), (10, 10))
    snack = cube(random_snack(rows, s), color=(255, 0, 0))
    flag = True
    while flag:
        pygame.time.delay(50)
        clock.tick(10) # limit to 10 FPS
        s.move()
        if s.body[0].pos == snack.pos:
            s.add_cube()
            snack = cube(random_snack(rows, s), color = (255, 0, 0))

        for x in range(len(s.body)):
            if s.body[x].pos in list(map(lambda z:z.pos, s.body[x+1:])):
                print('Score: '+ str(len(s.body)))
                message_box('You Lost!', 'Your score was: '+ str(len(s.body))+ '\nPlay again?')
                s.reset((10,10))
                break

        redraw_window(win)

def main():
    global width, rows, s, snack
    width = 500
    height = width
    rows = 20
    win = pygame.display.set_mode((width, height))


    clock = pygame.time.Clock()
    game_intro(win, clock)
    '''
    while flag:
        pygame.time.delay(50)
        clock.tick(10) # limit to 10 FPS
        s.move()
        if s.body[0].pos == snack.pos:
            s.add_cube()
            snack = cube(random_snack(rows, s), color = (255, 0, 0))

        for x in range(len(s.body)):
            if s.body[x].pos in list(map(lambda z:z.pos, s.body[x+1:])):
                print('Score: '+ str(len(s.body)))
                message_box('You Lost!', 'Your score was: '+ str(len(s.body))+ '\nPlay again?')
                s.reset((10,10))
                break

        redraw_window(win)
'''
if __name__ == "__main__":
    main()