import pymunk
from pymunk.pygame_util import DrawOptions

import pygame
import pygame.locals
 
WIDTH = 800
HEIGHT = 600
SIZE = (WIDTH, HEIGHT)


pygame.init()

screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()

space = pymunk.Space()
space.gravity = 0, 2000
options = DrawOptions(screen)

mass = 1

radius = 30
circle_moment = pymunk.moment_for_circle(mass, 0, radius)

circle_body = pymunk.Body(mass, circle_moment)
circle_body.position = 3*WIDTH//4, 50
circle_shape = pymunk.Circle(circle_body, radius)
circle_shape.elasticity = 0.8
circle_shape.friction = 1.0
space.add(circle_body, circle_shape)


segment_shape1 = pymunk.Segment(space.static_body, (0, 0), (800, 80), 2)
segment_shape1.body.position = 0, HEIGHT // 2
segment_shape1.elasticity = 0.8
segment_shape1.friction = 1.0
space.add(segment_shape1)

segment_shape2 = pymunk.Segment(space.static_body, (0, 60), (800, 0), 2)
segment_shape2.body.position = 2*WIDTH//5, 100
segment_shape2.elasticity = 0.8
segment_shape2.friction = 1.0
space.add(segment_shape2)


running = True
while running:
    # WINDOW-WIDE EVENT HANDLING
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.locals.KEYDOWN:
            if event.key == pygame.locals.K_ESCAPE:
                running = False
            elif event.key == pygame.locals.K_RETURN and event.mod & pygame.locals.KMOD_ALT:
                pygame.display.toggle_fullscreen()
        elif event.type == pygame.locals.QUIT:
            running = False
    
    # GAME STATE UPDATES
    steps = 10
    for _ in range(steps):
        space.step(1/120 / steps)

    # DRAWING
    screen.fill((255, 255, 255))
    # Must be the last two lines
    # of the game loop
    space.debug_draw(options)

    pygame.display.update()
    clock.tick(120)
    #---------------------------


pygame.quit()