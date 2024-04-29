import pygame 

pygame.init()

FPS = 30

pygame.display.set_caption("Asteroids")
window = pygame.display.set_mode((720, 480))
clock = pygame.time.Clock()

def menu():
    pass

def game():
    # init vars
    allObjs = pygame.sprite.Group()
    background = pygame.Surface((720, 480), masks=(0,0,0,0))
    while True:
        window.fill((0,0,0,0))

        # handle game events
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                return


        allObjs.update()
        allObjs.draw(window)

        clock.tick(FPS)



game()





    