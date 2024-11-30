import pygame
import sys
import random

screen1 = pygame.display.set_mode((700, 700))
pygame.display.set_caption("Shapes")

class Circle:
    def __init__(self, color, position, radi, width):
        self.color = pygame.Color(color)
        self.postion = position
        self.radi = radi
        self.width = width

    def draw(self):
        pygame.draw.circle(screen1, self.color, self.postion, self.radi, self.width)
    def grow(self, nuy):
        self.radi = self.radi + nuy
    def changecolor(self):
        self.color = pygame.Color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

corcle = Circle("white", (500, 500), 50, 0)
cercle = Circle("yellow", (500, 40), 20, 6)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            corcle.changecolor()
            cercle.changecolor()
            corcle.draw()
            cercle.draw()
        if event.type == pygame.MOUSEWHEEL:
            corcle.grow(2)
            cercle.grow(1)
    pygame.display.update()
