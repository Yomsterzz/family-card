import pygame
import time
pygame.init()
screen = pygame.display.set_mode((600,600))
pygame.display.set_caption("Family Card!")

background_img = pygame.image.load("images/arnov.png")
img = pygame.transform.scale(background_img, (600,600))

while True:
    font = pygame.font.SysFont("Arial", 60)
    text = font.render("Me:", True, (0,0,0))
    text2 = font.render("Arnov Ghosh", True, (0,0,0))
    screen.fill("white")
    screen.blit(background_img, (0,0))
    screen.blit(text, (160,180))
    screen.blit(text2, (270,280))
    pygame.display.update()
    time.sleep(3)

    img2 = pygame.image.load("images/aaron.png")
    font2 = pygame.font.SysFont("Verdana", 30)
    text3 = font2.render("Here's my brother: Aaron", True, (0,0,0))
    screen.fill("white")
    screen.blit(img2, (0,0))
    screen.blit(text3, (140,450))
    pygame.display.update()
    time.sleep(3)

    img3 = pygame.image.load("images/mom.png")
    font3 = pygame.font.SysFont("Verdana", 30)
    text4 = font2.render("My mother: Arya", True, (0,0,0))
    screen.fill("white")
    screen.blit(img3, (0,0))
    pygame.display.update()
    time.sleep(3)

    img4 = pygame.image.load("images/dad.png")
    font4 = pygame.font.SysFont("Verdana", 30)
    text5 = font2.render("My father: Surajeet", True, (0,0,0))
    screen.fill("white")
    screen.blit(img3, (0,0))
    pygame.display.update()
    time.sleep(3)