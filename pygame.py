#import pygame
#pygame.init()
#pygame.display.set_mode(700,700)
#while True:
    #for i in pygame.event.get():
        #if i.type == pygame.QUIT:
            #py
import pygame
pygame.init()
pygame.display.set_caption('Change color!')

window = pygame.display.set_mode((500, 500))

background = pygame.Surface((500, 500))
background.fill(pygame.Color('#000000'))

colors = [
    pygame.Color('#9EEB16'),
    pygame.Color('#0EEEBF'),
    pygame.Color('#0B7A62'),
    pygame.Color('#1C6AB3'),
    pygame.Color('#F11169'),
    pygame.Color('#F96307'),
]

current_color_index = 0

button_font = pygame.font.SysFont(
    'Verdana', 15)  # используем шрифт Verdana
button_text_color = pygame.Color("black")
button_color = pygame.Color("gray")
button_rect = pygame.Rect(100, 115, 100, 50)
button_text = button_font.render('Tap!', True, button_text_color)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if button_rect.collidepoint(event.pos):
                current_color_index = (current_color_index + 1) % len(colors)
                background.fill(colors[current_color_index])

        window.blit(background, (0, 0))
        pygame.draw.rect(window, button_color, button_rect)
        button_rect_center = button_text.get_rect(center=button_rect.center)
        window.blit(button_text, button_rect_center)
        pygame.display.update()
