import time
import pymunk


space = pymunk.Space()
space.gravity = 0, -10

body = pymunk.Body(1, 1666)
space.add(body)

while True:
    space.step(1/50)
    print(body.position)
    time.sleep(0.5)