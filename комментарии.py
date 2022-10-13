# -*- coding: utf-8 -*-

#Импорт pygame и библиотек
import pygame, pygame_gui, random

#Инициализация pygame
pygame.init()

#Размер окна
size = width, height = 600, 400
screen = pygame.display.set_mode(size)

#Создание приветственного меню (фон с кнопкой)
manager = pygame_gui.UIManager((600, 400), 'button_theming_test_theme.json')
fon_png = pygame.transform.scale((pygame.image.load('1wartortle-983x1024.png')),(600, 400))
start = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((200, 150),(200, 100)), text="Start!", manager=manager,object_id='#11')

game = False

#Размеры персонажей, предметов
def fon():
    screen.blit(fon_png, (0,0))
pers = pygame.transform.scale((pygame.image.load('wartortle-983x1024.png')), (75, 75))
vrag1 = pygame.transform.scale((pygame.image.load('vrag.png')), (50, 50))
boss = pygame.transform.scale((pygame.image.load('boss.png')), (100, 200))
hp = pygame.transform.scale((pygame.image.load('hp.png')), (25, 25))
laser = pygame.transform.scale((pygame.image.load('laser.png')), (50, 25))

#Координата ГГ
x_persona = 10
y_persona = 300
mas_vrag = []

#Создание границ для ГГ
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
	
	#Отображение лазера
    if las_patron > 0:
        screen.blit(laser, (x_persona+50, y_persona+25))
		

def vrag():
    global live
    global mas_vrag
    global las_patron
	
	
    for i in range(16):
	
		#Перемещение врагов на 5 пикселей влево
        mas_vrag[i][0] = mas_vrag[i][0] - 5
		
        #Коллизия со здоровьем
        if i == 5:
            if x_persona-25 < mas_vrag[i][0] < x_persona+75:
                if y_persona-25 < mas_vrag[i][1] < y_persona+75:
                    mas_vrag[i][0] = mas_vrag[i][0]+200*(len(mas_vrag))
                    mas_vrag[i][1] = random.choice([25, 125, 225, 325])
                    live = live + 1
            else:
                if mas_vrag[i][0] <-100:
                    mas_vrag[i][0] = mas_vrag[i][0]+200*(len(mas_vrag))
                    mas_vrag[i][1] = random.choice([25, 125, 225, 325])
					
        #Коллизия с боссом
		elif i == 10:
            if x_persona-100    < mas_vrag[i][0] < x_persona+75:
                if y_persona-200 < mas_vrag[i][1] < y_persona+75:
                    mas_vrag[i][0] = mas_vrag[i][0]+200*(len(mas_vrag))
                    mas_vrag[i][1] = random.choice([0, 200])
                    live = live - 3
            else:
                if mas_vrag[i][0] <-100:
                    mas_vrag[i][0] = mas_vrag[i][0]+200*(len(mas_vrag))
                    mas_vrag[i][1] = random.choice([0, 200])
					
        #Коллизия с лазером
        elif i == 15:
            if x_persona-50 < mas_vrag[i][0] < x_persona+75:
                if y_persona-25 < mas_vrag[i][1] < y_persona+75:
                    mas_vrag[i][0] = mas_vrag[i][0]+200*(len(mas_vrag))
                    mas_vrag[i][1] = random.choice([25, 125, 225, 325])
                    las_patron = las_patron + 1
            else:
                if mas_vrag[i][0] <-100:
                    mas_vrag[i][0] = mas_vrag[i][0]+200*(len(mas_vrag))
                    mas_vrag[i][1] = random.choice([25, 125, 225, 325])
					
		#Коллизия со змеями
        else:
            if x_persona-50 < mas_vrag[i][0] < x_persona+75:
                if y_persona-50 < mas_vrag[i][1] < y_persona+75:
                    mas_vrag[i][0] = mas_vrag[i][0]+200*(len(mas_vrag))
                    mas_vrag[i][1] = random.choice([0, 100, 200, 300])
                    live = live - 1
            else:
                if mas_vrag[i][0] <-100:
                    mas_vrag[i][0] = mas_vrag[i][0]+200*(len(mas_vrag))
                    mas_vrag[i][1] = random.choice([0, 100, 200, 300])
					
		#Отображение иконки здоровья
        if i == 5:
            screen.blit(hp, (mas_vrag[i][0], mas_vrag[i][1]))
			
		#Отображение боссов
        elif i == 10:
            screen.blit(boss, (mas_vrag[i][0], mas_vrag[i][1]))
			
		#Отображение иконки лазера
        elif i == 15:
            screen.blit(laser, (mas_vrag[i][0], mas_vrag[i][1]))
			
		#Отображение врагов
        else:
            screen.blit(vrag1, (mas_vrag[i][0], mas_vrag[i][1]))
			
			
vystrel = False
coor_pul = [0, 0]

#Функция, благодаря которой производится выстрел и убийство врагов
def ubit():
    global coor_pul
    global vystrel
    global las_patron
	
	#Если выстрел произошел
    if vystrel:
        coor_pul[0] = coor_pul[0] + 25
        pygame.draw.circle(screen, (255, 255, 255), coor_pul, 2, 2)
        if coor_pul[0] > 600:
            vystrel = False
        for i in range(16):
		
			#Проверка коллизий
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

#Начальные значения здоровья, очков, выстрелов
score = 0
las_patron = 3
live = 3

#Отображение текстовой информации + счетчиков
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
clock = pygame.time.Clock()
running = True
while running:
    time_delta = clock.tick(60)/1000.0
    for event in pygame.event.get():
	
		#Условие при нажатии кнопки "Закрыть"
        if event.type == pygame.QUIT:
            running = False
			
		#Условие при нажатии любой клавиши
        elif event.type == pygame.KEYDOWN:
		
			#Условие при нажатии клавиши "Пробел"
            if event.key == pygame.K_SPACE:
                if las_patron > 0 and vystrel == False:
                    vystrel = True
                    las_patron = las_patron - 1
                    coor_pul = [x_persona+50, y_persona+32]
				
		#Условие при нажатии на кнопку "Start!"
        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == start:
                live = 10
                mas_vrag = []
				
				#Спавн координат персонажей, предметов
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
	
	#Действие при нажатии клавиши "Стрелка влево"
    keystate = pygame.key.get_pressed()
    if keystate[pygame.K_LEFT]:
                x_persona = x_persona - 5
	
	#Действие при нажатии клавиши "Стрелка вправо"
    keystate = pygame.key.get_pressed()
    if keystate[pygame.K_RIGHT]:
                x_persona = x_persona + 5
				
	#Действие при нажатии клавиши "Стрелка вниз"
    keystate = pygame.key.get_pressed()
    if keystate[pygame.K_DOWN]:
                y_persona = y_persona + 5
	
	#Действие при нажатии клавиши "Стрелка вверх"
    keystate = pygame.key.get_pressed()
    if keystate[pygame.K_UP]:
                y_persona = y_persona - 5

	#Заливает фон черным цветом
    screen.fill([0, 0, 0])
    fon()
    manager.update(time_delta)
    manager.draw_ui(screen)
	
	#При нажатии кнопки "Start!" запускается игра
    if game:
        persona()
        vrag()
        ubit()
    time_pers()

	#Отрисовка каждого кадра
    pygame.display.flip()
	
	#Ограничение FPS
    clock.tick(60)
	
#Выход из игры
pygame.quit()