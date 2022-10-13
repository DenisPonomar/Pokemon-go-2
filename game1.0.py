# -*- coding: utf-8 -*-
import pygame, pygame_gui, random
pygame.init()
#pygame.mixer.music.load('menu.ogg')
#pygame.mixer.music.play()
sound0 = pygame.mixer.Sound('menu.ogg')
sound1 = pygame.mixer.Sound('bonus.ogg')
sound2 = pygame.mixer.Sound('vistrel.ogg')
sound3 = pygame.mixer.Sound('stolknoveniezmey.ogg')
sound4 = pygame.mixer.Sound('stolknoveniedrakon.ogg')
sound5 = pygame.mixer.Sound('gameover.ogg')
sound0.play()


size = width, height = 600, 400
screen = pygame.display.set_mode(size)
manager = pygame_gui.UIManager((600, 400), 'button_theming_test_theme.json')
fon_png = pygame.transform.scale((pygame.image.load('1wartortle-983x1024.png')),(600, 400))
start = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((200, 150),(200, 100)), text="Start!", manager=manager, object_id='#11')
game = False

def fon():
    screen.blit(fon_png, (0,0))
pers = pygame.transform.scale((pygame.image.load('wartortle-983x1024.png')), (75, 75))
vrag1 = pygame.transform.scale((pygame.image.load('vrag.png')), (50, 50))
boss = pygame.transform.scale((pygame.image.load('boss.png')), (100, 200))
hp = pygame.transform.scale((pygame.image.load('hp.png')), (25, 25))
laser = pygame.transform.scale((pygame.image.load('laser.png')), (50, 25))
x_persona = 10
y_persona = 300
mas_vrag = []
def persona():
    global x_persona
    global y_persona
    if x_persona <0:
        x_persona = 0
    if y_persona <0:
        y_persona = 0
    if x_persona >500:
        x_persona = 500
    if y_persona >325:
        y_persona = 325
    screen.blit(pers, (x_persona, y_persona))
    if las_patron > 0:
        screen.blit(laser, (x_persona+50, y_persona+25))
def vrag():
    global live
    global mas_vrag
    global las_patron
    for i in range(16):

        mas_vrag[i][0] = mas_vrag[i][0] - 5
        #Коллизия
        if i == 5:
            if x_persona-25 < mas_vrag[i][0] < x_persona+75:
                if y_persona-25 < mas_vrag[i][1] < y_persona+75:
                    mas_vrag[i][0] = mas_vrag[i][0]+200*(len(mas_vrag))
                    mas_vrag[i][1] = random.choice([25, 125, 225, 325])
                    live = live + 1
                    sound1.play()
            else:
                if mas_vrag[i][0] <-100:
                    mas_vrag[i][0] = mas_vrag[i][0]+200*(len(mas_vrag))
                    mas_vrag[i][1] = random.choice([25, 125, 225, 325])
        elif i == 10:
            if x_persona-100    < mas_vrag[i][0] < x_persona+75:
                if y_persona-200 < mas_vrag[i][1] < y_persona+75:
                    mas_vrag[i][0] = mas_vrag[i][0]+200*(len(mas_vrag))
                    mas_vrag[i][1] = random.choice([0, 200])
                    live = live - 3
                    sound4.play()
            else:
                if mas_vrag[i][0] <-100:
                    mas_vrag[i][0] = mas_vrag[i][0]+200*(len(mas_vrag))
                    mas_vrag[i][1] = random.choice([0, 200])
        #Лазер
        elif i == 15:
            if x_persona-50 < mas_vrag[i][0] < x_persona+75:
                if y_persona-25 < mas_vrag[i][1] < y_persona+75:
                    mas_vrag[i][0] = mas_vrag[i][0]+200*(len(mas_vrag))
                    mas_vrag[i][1] = random.choice([25, 125, 225, 325])
                    las_patron = las_patron + 1
                    sound1.play()
            else:
                if mas_vrag[i][0] <-100:
                    mas_vrag[i][0] = mas_vrag[i][0]+200*(len(mas_vrag))
                    mas_vrag[i][1] = random.choice([25, 125, 225, 325])

        else:
            if x_persona-50 < mas_vrag[i][0] < x_persona+75:
                if y_persona-50 < mas_vrag[i][1] < y_persona+75:
                    mas_vrag[i][0] = mas_vrag[i][0]+200*(len(mas_vrag))
                    mas_vrag[i][1] = random.choice([0, 100, 200, 300])
                    live = live - 1
                    sound3.play()
            else:
                if mas_vrag[i][0] <-100:
                    mas_vrag[i][0] = mas_vrag[i][0]+200*(len(mas_vrag))
                    mas_vrag[i][1] = random.choice([0, 100, 200, 300])
        if i == 5:
            screen.blit(hp, (mas_vrag[i][0], mas_vrag[i][1]))
        elif i == 10:
            screen.blit(boss, (mas_vrag[i][0], mas_vrag[i][1]))
        elif i == 15:
            screen.blit(laser, (mas_vrag[i][0], mas_vrag[i][1]))
        else:
            screen.blit(vrag1, (mas_vrag[i][0], mas_vrag[i][1]))
vystrel = False
coor_pul = [0, 0]
def ubit():
    global coor_pul
    global vystrel
    global las_patron
    if vystrel:
        sound2.play()
        coor_pul[0] = coor_pul[0] + 25
        pygame.draw.circle(screen, (255, 255, 255), coor_pul, 2, 2)
        if coor_pul[0] > 600:
            vystrel = False
        for i in range(16):
            if i == 5:
                pass
            elif i == 10:
                if coor_pul[0]-100 < mas_vrag[i][0] < coor_pul[0]:
                    if coor_pul[0]-200 < mas_vrag[i][1] < coor_pul[1]:
                        mas_vrag[i][0] = mas_vrag[i][0]+200*(len(mas_vrag))
                        mas_vrag[i][1] = random.choice([0, 200])
                        vystrel = False
                        break
            elif i == 15:
                pass

            else:
                if coor_pul[0]-50 < mas_vrag[i][0] < coor_pul[0]:
                    if coor_pul[1]-50 < mas_vrag[i][1] < coor_pul[0]:
                        mas_vrag[i][0] = mas_vrag[i][0]+200*(len(mas_vrag))
                        mas_vrag[i][1] = random.choice([0, 100, 200, 300])
                        vystrel = False
                        break

score = 0
las_patron = 3
live = 3
def time_pers():
    global game
    global score
    if game:
        f2 = pygame.font.Font(None, 48)
        text2 = f2.render("Laser: "+str(las_patron), False, (255, 255, 255))
        screen.blit(text2, (0, 0))

        score = score + 4/60
        f2 = pygame.font.Font(None, 48)
        text2 = f2.render("Score: "+str(int((score))), False, (255, 255, 255))
        screen.blit(text2, (400, 00))

        f2 = pygame.font.Font(None, 48)
        text2 = f2.render(str(live), False, (255, 255, 255))
        screen.blit(text2, (200, 0))

    if live < 1:
        f2 = pygame.font.Font(None, 48)
        text2 = f2.render("Game Over", False, (255, 255, 255))
        screen.blit(text2, (200, 100))
        start.show()
        game = False
        #for i in range(1):
        #    sound0.stop()
        #    sound5.play()
clock = pygame.time.Clock()
running = True
while running:
    time_delta = clock.tick(60)/1000.0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if las_patron > 0 and vystrel == False:
                    vystrel = True
                    las_patron = las_patron - 1
                    coor_pul = [x_persona+50, y_persona+32]
        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == start:
                live = 10
                mas_vrag = []
                for i in range(16):
                    if i == 5:
                        mas_vrag.append([700+(i*200), random.choice([25, 125, 225, 325])])
                    elif i == 10:
                        mas_vrag.append([700+(i*200), random.choice([0, 200])])
                    elif i == 15:
                        mas_vrag.append([700+(i*200), random.choice([25, 125, 225, 325])])
                    else:
                        mas_vrag.append([700+(i*200), random.choice([0, 100, 200, 300])])
                score = 0
                game = True
                start.hide()
        manager.process_events(event)
    keystate = pygame.key.get_pressed()
    if keystate[pygame.K_LEFT]:
                x_persona = x_persona - 5
    keystate = pygame.key.get_pressed()
    if keystate[pygame.K_RIGHT]:
                x_persona = x_persona + 5
    keystate = pygame.key.get_pressed()
    if keystate[pygame.K_DOWN]:
                y_persona = y_persona + 5
    keystate = pygame.key.get_pressed()
    if keystate[pygame.K_UP]:
                y_persona = y_persona - 5


    screen.fill([0, 0, 0])
    fon()
    manager.update(time_delta)
    manager.draw_ui(screen)
    if game:
        persona()
        vrag()
        ubit()
    time_pers()

    pygame.display.flip()
    clock.tick(60)
    #print int(1/(time.time()-ty))
pygame.quit()
