import math

import pymunk
from pymunk.pygame_util import DrawOptions

import pygame
import pygame.locals


class Candy(pygame.sprite.Sprite):
    def __init__(self, x, y, space):
        super().__init__(self.groups)
        mass = 1
        radius = 30
        circle_moment = pymunk.moment_for_circle(mass, 0, radius)

        circle_body = pymunk.Body(mass, circle_moment)
        circle_body.position = x, y
        circle_shape = pymunk.Circle(circle_body, radius)
        circle_shape.elasticity = 0.9
        circle_shape.friction = 1.0
        space.add(circle_body, circle_shape)

        self._image =  self.images[0]
        self.image = self._image
        self.rect = self.image.get_rect()
        self.body = circle_body
        self.rect.center = self.body.position
    
    def update(self) -> None:
        self.rect.center = self.body.position
        self.image = rot_center(self._image, math.degrees(-self.body.angle))


def rot_center(image, angle):
    """Rotate an image while keeping its center and size
    
    Credit: http://www.pygame.org/wiki/RotateCenter?parent=CookBook
    """
    orig_rect = image.get_rect()
    rot_image = pygame.transform.rotate(image, angle)
    rot_rect = orig_rect.copy()
    rot_rect.center = rot_image.get_rect().center
    rot_image = rot_image.subsurface(rot_rect).copy()
    return rot_image


WIDTH = 800
HEIGHT = 600
SIZE = (WIDTH, HEIGHT)


pygame.init()

screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()

space = pymunk.Space()
space.gravity = 0, 0
space.gravity = 0, 2000
options = DrawOptions(screen)

radius = 30

all = pygame.sprite.Group()
Candy.groups = [all]
red_lolli_img = pygame.image.load("sandbox/lollipopRed.png")
red_lolli_img = pygame.transform.smoothscale(red_lolli_img, (radius*2, radius*2))
Candy.images = [red_lolli_img]

candy = Candy(3*WIDTH//4, 50, space)

segment_shape1 = pymunk.Segment(space.static_body, (0, 0), (800, 80), 2)
segment_shape1.body.position = 0, HEIGHT // 2
segment_shape1.elasticity = 0.6
segment_shape1.friction = 1.0
space.add(segment_shape1)

segment_shape2 = pymunk.Segment(space.static_body, (0, 60), (800, 0), 2)
segment_shape2.body.position = 2*WIDTH//5, 100
segment_shape2.elasticity = 0.6
segment_shape2.friction = 1.0
space.add(segment_shape2)


running = True
while running:
    print(len(all))
    # WINDOW-WIDE EVENT HANDLING
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.locals.KEYDOWN:
            if event.key == pygame.locals.K_ESCAPE:
                running = False
            elif event.key == pygame.locals.K_RETURN and event.mod & pygame.locals.KMOD_ALT:
                pygame.display.toggle_fullscreen()
        elif event.type == pygame.locals.MOUSEBUTTONDOWN:
            Candy(*event.pos, space)
        elif event.type == pygame.locals.QUIT:
            running = False
    
    # GAME STATE UPDATES
    steps = 10
    for _ in range(steps):
        space.step(1/120 / steps)
    
    all.update()

    # DRAWING
    screen.fill((255, 255, 255))
    # Must be the last two lines
    # of the game loop
    space.debug_draw(options)
    all.draw(screen)

    pygame.display.update()
    clock.tick(120)
    #---------------------------


pygame.quit()