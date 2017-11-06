from Class import *
global seconds, start_tick

def screen1():
    FPS=60
    fpsClock=pygame.time.Clock()
    screen=pygame.display.set_mode((450,450))
    pygame.display.set_caption('Car Simulation')
    background=pygame.image.load('street 3.png')
    streetblock1 = Streetblocks("wall 1.png", 13,0)
    streetblock2 = Streetblocks("wall 1.png", 13,80)
    streetblock3 = Streetblocks("wall 1.png", 13,200)
    streetblock4 = Streetblocks("wall 2.png", 13,422)
    streetblock5 = Streetblocks("wall 2.png", 200,422)
    streetblock6 = Streetblocks("wall 1.png", 420,0)
    streetblock7 = Streetblocks("wall 1.png", 420,200)
    streetblock8 = Streetblocks("wall 2.png", 98,0)
    streetblock9 = Streetblocks("wall 1.png", 88,10)
    streetblock10 = Streetblocks("wall 1.png", 88,97)
    streetblock11 = Streetblocks("wall 1.png", 112,10)
    streetblock12 = Streetblocks("wall 1.png", 112,97)
    streetblock13 = Streetblocks("wall 1.png", 180,100)
    streetblock14 = Streetblocks("wall 1.png", 180,160)
    streetblock15 = Streetblocks("wall 1.png", 237, 95)
    streetblock16 = Streetblocks("wall 1.png", 237, 180)
    streetblock17 = Streetblocks("wall 1.png", 305, 30)
    streetblock18 = Streetblocks("wall 1.png", 305, 96)
    streetblock19 = Streetblocks("wall 1.png", 351, 10)
    streetblock20 = Streetblocks("wall 1.png", 351, 96)
    finish1 = Finish("wall 6.png",350,10)
    quit1= Finish("wall 6.png",20,15)
    sprite= Car1("car down.png",50,30)
    direction=None
    streetblocks = Group(streetblock1,streetblock2,streetblock3,
                         streetblock4,streetblock5,streetblock6,
                         streetblock7,streetblock8,streetblock9,
                         streetblock10,streetblock11,streetblock12,
                         streetblock13,streetblock14,streetblock15,
                         streetblock16,streetblock17,streetblock18,
                         streetblock19,streetblock20)
    everything = Group(sprite)
    global start_tick, seconds
    start_tick=pygame.time.get_ticks()
    running = True
    while running:
        seconds=(pygame.time.get_ticks() - start_tick)/1000
        streetblocks.draw(screen)
        screen.fill((0,0,0))
        screen.blit(background,(0,0))
        if seconds >= 0:
            font = pygame.font.SysFont("Times New Roman", 24)
            timesurface=font.render("Timer:" +str(seconds), False,(0,255,0))
            screen.blit(timesurface,(170,0))
        everything.draw(screen)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                direction = event.key
            if event.type == KEYUP:
                if (event.key == direction):
                    direction = None
        if (sprite.rect.colliderect(streetblock1) == False and sprite.rect.colliderect(streetblock2) == False
            and sprite.rect.colliderect(streetblock3) == False and sprite.rect.colliderect(streetblock4) == False
            and sprite.rect.colliderect(streetblock5) == False and sprite.rect.colliderect(streetblock6) == False
            and sprite.rect.colliderect(streetblock7) == False and sprite.rect.colliderect(streetblock8) == False
            and sprite.rect.colliderect(streetblock9) == False and sprite.rect.colliderect(streetblock10) == False
            and sprite.rect.colliderect(streetblock11) == False and sprite.rect.colliderect(streetblock12) == False
            and sprite.rect.colliderect(streetblock13) == False and sprite.rect.colliderect(streetblock14) == False
            and sprite.rect.colliderect(streetblock15) == False and sprite.rect.colliderect(streetblock16) == False
            and sprite.rect.colliderect(streetblock17) == False and sprite.rect.colliderect(streetblock18) == False
            and sprite.rect.colliderect(streetblock19) == False and sprite.rect.colliderect(streetblock20) == False):
            sprite.move(direction)
        if sprite.rect.colliderect(finish1):
            running = False
            screen2()
        if sprite.rect.colliderect(quit1):
            import Main; Main.menu()
        if spritecollide(sprite,streetblocks,dokill=False):
            end()
        fpsClock.tick(FPS)


def screen2():
    FPS=60
    fpsClock=pygame.time.Clock()
    screen=pygame.display.set_mode((450,450))
    pygame.display.set_caption('Car Simulation')
    background=pygame.image.load('another street.png')
    streetblock1 = Streetblocks("wall 1.png", 0,28)
    streetblock2 = Streetblocks("wall 1.png", 0,200)
    streetblock3 = Streetblocks("wall 1.png", 420,180)
    streetblock4 = Streetblocks("wall 1.png", 420,20)
    streetblock5 = Streetblocks("wall 7.png", 85,357)
    streetblock6 = Streetblocks("wall 7.png", 165,357)
    streetblock7 = Streetblocks("wall 2.png", 15,435)
    streetblock8 = Streetblocks("wall 2.png", 90,435)
    streetblock9 = Streetblocks("wall 2.png", 252,182)
    streetblock10 = Streetblocks("wall 1.png", 252,113)
    streetblock11 = Streetblocks("wall 2.png", -75,239)
    streetblock12 = Streetblocks("wall 2.png", -75,215)
    streetblock13 = Streetblocks("wall 7.png", 70,130)
    streetblock14 = Streetblocks("wall 7.png", 150,130)
    streetblock15 = Streetblocks("wall 7.png", 150,120)
    streetblock16 = Streetblocks("wall 7.png", 70,120)
    streetblock17 = Streetblocks("wall 7.png", 85,330)
    streetblock18 = Streetblocks("wall 7.png", 165,330)
    streetblock19 = Streetblocks("wall 1.png", 350,275)
    streetblock20 = Streetblocks("wall 1.png", 325,275)
    streetblock21 = Streetblocks("wall 2.png", 0,25)
    streetblock22 = Streetblocks("wall 2.png", 80,25)
    streetblock23 = Streetblocks("wall 1.png", 350,-142)
    streetblock24 = Streetblocks("wall 1.png", 320,-142)
    finish1 = Finish("wall 6.png",360,6)
    back = Finish("wall 6.png",380,420)
    sprite= Car2("car up.png",390,380)
    direction=None

    streetblocks = Group(streetblock1,streetblock2,streetblock3,
                         streetblock4,streetblock5,streetblock6,
                         streetblock7,streetblock8,streetblock9,
                         streetblock10,streetblock11,streetblock12,
                         streetblock13,streetblock14,streetblock15,
                         streetblock16,streetblock17,streetblock18,
                         streetblock19,streetblock20,streetblock21,
                         streetblock22,streetblock23,streetblock24)
    everything = Group(sprite)
    running = True
    global seconds
    while running:
        seconds=(pygame.time.get_ticks() - start_tick)/1000
        streetblocks.draw(screen)
        screen.fill((0,0,0))
        screen.blit(background,(0,0))
        if seconds >= 0:
            font = pygame.font.SysFont("Times New Roman", 24)
            timesurface=font.render("Timer:" +str(seconds), False,(0,255,0))
            screen.blit(timesurface,(170,0))
        everything.draw(screen)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                direction = event.key
            if event.type == KEYUP:
                if (event.key == direction):
                    direction = None
        if (sprite.rect.colliderect(streetblock1) == False and sprite.rect.colliderect(streetblock2) == False and
            sprite.rect.colliderect(streetblock3) == False and sprite.rect.colliderect(streetblock4) == False and
            sprite.rect.colliderect(streetblock5) == False and sprite.rect.colliderect(streetblock6) == False and
            sprite.rect.colliderect(streetblock7) == False and sprite.rect.colliderect(streetblock8) == False and
            sprite.rect.colliderect(streetblock9) == False and sprite.rect.colliderect(streetblock10) == False and
            sprite.rect.colliderect(streetblock11) == False and sprite.rect.colliderect(streetblock12) == False and
            sprite.rect.colliderect(streetblock13) == False and sprite.rect.colliderect(streetblock14) == False and
            sprite.rect.colliderect(streetblock15) == False and sprite.rect.colliderect(streetblock16) == False and
            sprite.rect.colliderect(streetblock17) == False and sprite.rect.colliderect(streetblock18) == False and
            sprite.rect.colliderect(streetblock19) == False and sprite.rect.colliderect(streetblock20) == False and
            sprite.rect.colliderect(streetblock21) == False and sprite.rect.colliderect(streetblock22) == False and
            sprite.rect.colliderect(streetblock23) == False and sprite.rect.colliderect(streetblock24) == False):
            sprite.move(direction)
        if sprite.rect.colliderect(finish1):
            running = False
            finish()
        if sprite.rect.colliderect(back):
            import Main; Main.menu()
        if spritecollide(sprite,streetblocks,dokill=False):
            end()
        fpsClock.tick(FPS)

def end():
    GO = textrect("Times New Roman","GAME OVER",20,170,200,255,255,255)
    RE = textrect("Times New Roman","RESTART",20,180,240,255,255,255)
    quit = textrect("Times New Roman", "Quit", 20, 200, 260, 255, 255, 255)
    pygame.mixer.music.load("Death.wav")
    pygame.mixer.music.play()
    screen = pygame.display.set_mode((450,450))
    while True:
        screen.fill((0,0,0))
        everything = Group(GO,RE,quit)
        everything.draw(screen)
        if seconds >= 0:
            font = pygame.font.SysFont("Times New Roman", 24)
            timesurface=font.render("Timer:" +str(seconds), False,(255,255,255))
            screen.blit(timesurface,(163,160))
        display.update()
        e = event.wait()
        if RE.rect.collidepoint(mouse.get_pos()):
            RE = textrect("Times New Roman", "RESTART", 20, 180, 240, 0, 0, 255)
            if e.type == MOUSEBUTTONDOWN:
                screen1()
        else:
            RE = textrect("Times New Roman", "RESTART", 20, 180, 240, 255, 255,255)
        if quit.rect.collidepoint(mouse.get_pos()):
            quit = textrect("Times New Roman", "QUIT",20,200,260,255,0,0)
            if e.type == MOUSEBUTTONDOWN:
                pygame.quit()
                break
        else:
            quit = textrect("Times New Roman", "QUIT",20,200,260,255,255,255)

def finish():
    CO = textrect("Times New Roman","CONGRATULATION",20,140,200,255,255,255)
    RE = textrect("Times New Roman","RESTART",20,180,240,255,255,255)
    quit = textrect("Times New Roman", "Quit", 20, 200, 260, 255, 255, 255)
    pygame.mixer.music.load("Ta Da.wav")
    pygame.mixer.music.play()
    screen = pygame.display.set_mode((450,450))
    while True:
        screen.fill((0,0,0))
        everything = Group(CO,RE,quit)
        everything.draw(screen)
        if seconds >= 0:
            font = pygame.font.SysFont("Times New Roman", 24)
            timesurface=font.render("Timer:" +str(seconds), False,(255,255,255))
            screen.blit(timesurface,(163,160))
        display.update()
        e = event.wait()
        if RE.rect.collidepoint(mouse.get_pos()):
            RE = textrect("Times New Roman", "RESTART", 20, 180, 240, 0, 0, 255)
            if e.type == MOUSEBUTTONDOWN:
                screen1()
        else:
            RE = textrect("Times New Roman", "RESTART", 20, 180, 240, 255, 255,255)
        if quit.rect.collidepoint(mouse.get_pos()):
            quit = textrect("Times New Roman", "QUIT",20,200,260,255,0,0)
            if e.type == MOUSEBUTTONDOWN:
                pygame.quit()
                break
        else:
            quit = textrect("Times New Roman", "QUIT",20,200,260,255,255,255)
