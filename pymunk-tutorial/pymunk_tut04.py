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
space.gravity = 0, 3000
options = DrawOptions(screen)

body = pymunk.Body(mass=1, body_type=pymunk.Body.DYNAMIC)
body.position = 50, 100
poly = pymunk.Poly.create_box(body, size=(50, 50))
moment = pymunk.moment_for_poly(body.mass, poly.get_vertices())
body.moment = moment
print(body.moment)

space.add(body, poly)


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