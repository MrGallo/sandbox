# -*- coding: utf-8 -*-
"""Testing

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1rguQZyss_l6yrhbYWDQZgCVrDFgeHjZD

>[Testing](#folderId=0B6R8LoXsF8F6Z203N1ZFM0xOWjQ&updateTitle=true&scrollTo=4NWzTHAz_ZNm)

>>[Section 1](#folderId=0B6R8LoXsF8F6Z203N1ZFM0xOWjQ&updateTitle=true&scrollTo=vlk08ruDAJPZ)

# Testing
Testing 123

- one
- two
- three
"""

a = 5
b = 7
print("hello world")
print(f"the sum of {a} and {b} is {a+b}")

"""## Section 1
Blah blah
"""

!pip install pygame

import sys, pygame


pygame.init()

size = width, height = 320, 240
speed = [2, 2]
black = 0, 0, 0

screen = pygame.display.set_mode(size)

ball = pygame.image.load("intro_ball.gif")
ballrect = ball.get_rect()

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    ballrect = ballrect.move(speed)
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]

    screen.fill(black)
    screen.blit(ball, ballrect)
    pygame.display.flip()
