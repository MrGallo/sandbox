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
space.gravity = 0, 0
options = DrawOptions(screen)

mass = 1

radius = 30
circle_moment = pymunk.moment_for_circle(mass, 0, radius)

circle_body = pymunk.Body(mass, circle_moment)
circle_body.position = WIDTH//5, 100
circle_shape = pymunk.Circle(circle_body, radius)
space.add(circle_body, circle_shape)

poly_shape = pymunk.Poly.create_box(None, size=(50, 50))
poly_moment = pymunk.moment_for_poly(mass, poly_shape.get_vertices())
poly_body = pymunk.Body(mass, poly_moment)
poly_shape.body = poly_body
poly_body.position = 2*WIDTH//5, 100
space.add(poly_body, poly_shape)

segment_moment = pymunk.moment_for_segment(mass, (0, 0), (0, 400), 2)
segment_body = pymunk.Body(mass, segment_moment)
segment_shape = pymunk.Segment(segment_body, (0, 0), (0, 400), 2)
segment_body.position = 3*WIDTH//5, 100
space.add(segment_body, segment_shape)

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
    space.step(1/120)

    # DRAWING
    screen.fill((255, 255, 255))
    # Must be the last two lines
    # of the game loop
    space.debug_draw(options)

    pygame.display.update()
    clock.tick(120)
    #---------------------------


pygame.quit()