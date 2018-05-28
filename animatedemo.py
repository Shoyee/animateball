#!/usr/bin/env python3
import pygame

def main():
    pygame.init()

    screen = pygame.display.set_mode((1000,700))

    x,y = 50,50
    sx,sy = 5,5

    pygame.display.set_caption("弹弹球")
    running_flag = True

    while running_flag:
        for even in pygame.event.get():
            if even.type == pygame.QUIT:
                running_flag = False

        screen.fill((255,255,255))
        pygame.draw.circle(screen,(255,0,0),(x,y),50)
        pygame.display.flip()

        pygame.time.delay(10)

        x += sx
        y += sy

        if x - 50 <= 0 or x + 50 >= screen.get_width():
            sx = -sx

        if y - 50 <= 0 or y + 50 >= screen.get_height():
            sy = -sy

if __name__ == "__main__":
    main()
