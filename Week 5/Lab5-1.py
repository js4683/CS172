import pygame
import random
from Drawable import Rectangle, Snowflake

pygame.init()
surface = pygame.display.set_mode((600,500))
pygame.display.set_caption("Lab 5")
drawables = []
green = Rectangle(0, 200 ,600 ,300 , (0,128,0))
sky = Rectangle(0, 0, 600, 300, (0,0,205))
snow = Snowflake()
drawables.append(green)
drawables.append(sky)
drawables.append(snow)
for i in range(0, 100):
    newSnow = Snowflake()
    newSnow.setLoc((random.randint(0, 600), random.randint(0,600)))
    drawables.append(newSnow)
counter = 0
while True:    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                counter += 1
    if counter %2 == 0:
        for drawable in drawables:
            if isinstance(drawable, Snowflake) == True:
                drawable.setLoc((random.randint(0, 600), random.randint(0, 600)))
                drawable.draw(surface)
            else:
                drawable.draw(surface)
    pygame.display.update()
