import pygame

pygame.init()
screen=pygame.display.set_mode(700,700)
pygame.display.set_caption('Dog')
dog=pygame.image.load('dog_picture')
screen.blit(dog,(0,0))
pygame.display.flip()
while True:
    for event in pygame.event.get:
        if event.type==pygame.QUIT:
            pygame.quit()
            exit()


