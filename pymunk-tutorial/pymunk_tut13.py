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
space.damping = 0.5
options = DrawOptions(screen)

mass = 1

radius = 30
circle_moment = pymunk.moment_for_circle(mass, 0, radius)

circle_body = pymunk.Body(mass, circle_moment, body_type=pymunk.Body.KINEMATIC)
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
segment_shape.sensor = True
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
        elif event.type == pygame.locals.MOUSEBUTTONDOWN:
            query = space.point_query_nearest(event.pos, 0, pymunk.ShapeFilter())
            if query is not None:
                body = query.shape.body
                diff = body.position - query.point
                body.apply_impulse_at_local_point(diff.normalized() * 200, diff)
        elif event.type == pygame.locals.QUIT:
            running = False
    
    # GAME STATE UPDATES
    speed = 200
    keys = pygame.key.get_pressed()
    if keys[pygame.locals.K_d] and not keys[pygame.locals.K_a]:
        circle_body.velocity = (speed, circle_body.velocity.y)
    elif keys[pygame.locals.K_a] and not keys[pygame.locals.K_d]:
        circle_body.velocity = (-speed, circle_body.velocity.y)
    else:
        circle_body.velocity *= 0.95

    if keys[pygame.locals.K_w] and not keys[pygame.locals.K_s]:
        circle_body.velocity = (circle_body.velocity.x, -speed)
    elif keys[pygame.locals.K_s] and not keys[pygame.locals.K_w]:
        circle_body.velocity = (circle_body.velocity.x, speed)
    else:
        circle_body.velocity *= 0.95


    space.step(1/120)

    shape_query_list = space.shape_query(segment_shape)
    if len(shape_query_list) > 0:
        for shape_query in shape_query_list:
            shape = shape_query.shape
            body = shape.body

    # DRAWING
    screen.fill((255, 255, 255))
    # Must be the last two lines
    # of the game loop
    space.debug_draw(options)

    pygame.display.update()
    clock.tick(120)
    #---------------------------


pygame.quit()