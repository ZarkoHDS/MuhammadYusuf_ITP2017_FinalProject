from Class import *

def menu():
    pygame.init()
    screen=pygame.display.set_mode((450,450))
    pygame.display.set_caption('Car Simulation')
    title = pygame.image.load("Title.png")
    screen.fill((0, 0, 0))
    play = textrect("Times New Roman", "Play", 30, 200, 200, 255, 255, 255)
    quit = textrect("Times New Roman", "Quit", 30, 200, 250, 255, 255, 255)
    while True:
        screen.fill((0, 0, 0))
        screen.blit(title, (155,100))
        text = Group(play,quit)
        text.draw(screen)
        e = event.wait()
        if play.rect.collidepoint(mouse.get_pos()):
            play = textrect("Times New Roman", "Play", 30, 200, 200, 0, 0, 255)
            if e.type == MOUSEBUTTONDOWN:
                import Screen; Screen.screen1()
                import Screen; Screen.screen2()
                import Screen; Screen.finish()
        else:
            play = textrect("Times New Roman", "Play", 30, 200, 200, 255, 255,255)

        if quit.rect.collidepoint(mouse.get_pos()):
            quit = textrect("Times New Roman", "Quit",30,200,250,255,0,0)
            if e.type == MOUSEBUTTONDOWN:
                pygame.quit()
                break
        else:
            quit = textrect("Times New Roman", "Quit",30,200,250,255,255,255)

        pygame.display.update()
menu()
