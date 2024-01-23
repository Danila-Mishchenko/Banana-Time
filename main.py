import random
import sqlite3
import pygame
import sys

FPS = 1000


def terminate():  # функция закрытия
    pygame.quit()
    sys.exit()


def vvod():  # ввод ника
    global symarno_banan
    global kup
    global imya
    global skin
    activ = False
    screen = pygame.display.set_mode((400, 100))
    text = 'Введите ник'
    q = pygame.font.Font(None, 50)
    nik = q.render(text, True, (0, 0, 0))
    screen.blit(nik, (0, 0))
    fon = pygame.transform.scale(load_image('data/gifon.gif'), (800, 600))
    screen.blit(fon, (0, 0))
    input_box = pygame.Rect(50, 25, 300, 50)
    pygame.draw.rect(screen, (200, 255, 200), (50, 25, 300, 50))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if input_box.collidepoint(event.pos):  # если нажать мышкой на прямоугольник, то можно ввести ник
                    activ = True
                    if text == 'Введите ник':
                        text = ''
                else:
                    activ = False

            elif event.type == pygame.KEYDOWN:
                if activ:
                    if event.key == pygame.K_BACKSPACE:  # удаления последнего символа
                        text = text[:-1]
                    elif event.key == pygame.K_RETURN:
                        plist = []
                        con = sqlite3.connect('data/baza.db')
                        cur = con.cursor()
                        imena = cur.execute("""SELECT nik FROM skins""")
                        for i in imena:
                            plist.append(i[0])
                        if text not in plist:  # если нет в базе данных, то добавляем новый профиль
                            cur.execute(
                                """INSERT INTO skins(kol, skin0, skin1, skin2, skin3, nik) VALUES (?, ?, ?, ?, ?, ?)""",
                                (0, 1, 0, 0, 0, text))
                            symarno_banan = 0
                            kup = [1, 0, 0, 0]
                            imya = text
                        else:  # берем значения из базы данных данного профиля
                            result1 = cur.execute("""SELECT * FROM skins WHERE nik = ?""", (text,))
                            result2 = []
                            for i in result1:
                                result2.append(i)
                            result = result2[0]
                            symarno_banan = result[0]
                            kup = [result[1], result[2], result[3], result[4]]
                            imya = text
                        con.commit()
                        con.close()
                        skin = 0
                        start_screen()  # включение лобби
                    else:
                        if len(text) < 11:  # ограничение по количеству символов
                            text += event.unicode  # добавления символа
        screen.blit(fon, (0, 0))
        if activ:
            pygame.draw.rect(screen, (200, 255, 200), (50, 25, 300, 50))
        else:
            pygame.draw.rect(screen, (0, 255, 0), (50, 25, 300, 50))
        nik = q.render(text, True, (0, 0, 0))
        screen.blit(nik, (input_box.x + 5, input_box.y + 5))
        pygame.display.update()


def start_screen():
    global skin
    global symarno_banan
    screen = pygame.display.set_mode((800, 600))
    if zvyk1:
        pygame.mixer.music.load('data/music.mp3')
        pygame.mixer.music.play(-1)
    fon = pygame.transform.scale(load_image('data/gifon.gif'), (800, 600))
    screen.blit(fon, (0, 0))
    fon1 = pygame.transform.scale(load_image('data/test.png'), (400, 50))
    screen.blit(fon1, (200, 400))
    fon2 = pygame.transform.scale(load_image('data/shop.png'), (300, 50))
    screen.blit(fon2, (250, 451))
    fon3 = pygame.transform.scale(load_image('data/settings.png'), (300, 50))
    screen.blit(fon3, (250, 502))
    text_coord = 50
    ava_banana = pygame.transform.scale(load_image('data/banan.png'), (100, 70))
    screen.blit(ava_banana, (700, -10))
    r = pygame.font.Font(None, 50)
    text = r.render(str(symarno_banan), True, (255, 255, 0))
    screen.blit(text, (630, 0))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if 600 >= event.pos[0] >= 200 and 450 >= event.pos[1] >= 400:
                    if zvyk1:
                        pygame.mixer.music.pause()  # включение музыки если True
                    game()  # включение игры
                elif 500 >= event.pos[0] >= 300 and 501 >= event.pos[1] >= 451:
                    shop()  # включение магазина
                elif 500 >= event.pos[0] >= 300 and 552 >= event.pos[1] >= 502:
                    seetings()  # включение настроек
        screen.blit(fon, (0, 0))
        screen.blit(fon1, (200, 400))
        screen.blit(fon2, (250, 451))
        screen.blit(fon3, (250, 502))
        screen.blit(ava_banana, (700, -10))
        r = pygame.font.Font(None, 50)
        text = r.render(str(symarno_banan), True, (255, 255, 0))
        screen.blit(text, (630, 0))
        pygame.display.update()


def load_image(name, colorkey=True):  # обработка изображений
    image = pygame.image.load(name)
    image = image.convert_alpha()
    return image


def seetings():
    global zvyk1
    global zvyk2
    global zvyk3
    fon = pygame.transform.scale(load_image('data/fon.webp'), (800, 600))
    screen.blit(fon, (0, 0))
    fon1 = pygame.transform.scale(load_image('data/strelka.png'), (100, 50))
    screen.blit(fon1, (0, 0))
    ok = pygame.transform.scale(load_image('data/off.png'), (400, 80))
    screen.blit(ok, (425, 55))
    k = pygame.font.Font(None, 70)
    text3 = k.render('МУЗЫКА В ИГРЕ', True, (0, 0, 0))
    screen.blit(text3, (75, 75))
    ok1 = pygame.transform.scale(load_image('data/off.png'), (400, 80))
    screen.blit(ok1, (425, 155))
    p = pygame.font.Font(None, 60)
    text4 = p.render('МУЗЫКА В ЛОББИ', True, (0, 0, 0))
    screen.blit(text4, (75, 175))
    yu = pygame.font.Font(None, 60)
    text8 = yu.render('ПРОФИЛЬ - ' + imya, True, (0, 0, 0))
    screen.blit(text8, (75, 375))
    ef = pygame.font.Font(None, 60)
    textef = ef.render('ЗВУКИ ЭФФЕКТОВ', True, (0, 0, 0))
    screen.blit(textef, (75, 275))
    sm = pygame.transform.scale(load_image('data/smena.png'), (750, 80))
    screen.blit(sm, (25, 425))
    sv = pygame.transform.scale(load_image('data/off.png'), (400, 80))
    screen.blit(sv, (425, 255))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if 100 >= event.pos[0] >= 0 and 50 >= event.pos[1] >= 0:
                    return  # возвращение в лобби чтобы музыка не начиналась заново
                elif 800 >= event.pos[0] >= 450 and 225 >= event.pos[1] >= 160:
                    if zvyk1:  # выключение или включение музыки в игре
                        zvyk1 = False
                        pygame.mixer.music.pause()
                    else:
                        zvyk1 = True
                        pygame.mixer.music.play()
                elif 800 >= event.pos[0] >= 450 and 125 >= event.pos[1] >= 60:
                    if zvyk2:  # выключение или включение музыки в лобби
                        zvyk2 = False
                    else:
                        zvyk2 = True
                elif 500 >= event.pos[0] >= 225 and 500 >= event.pos[1] >= 425:
                    pygame.mixer.music.pause()
                    vvod()
                elif 800 >= event.pos[0] >= 425 and 335 >= event.pos[1] >= 255:
                    if zvyk3:  # выключение или включение звуков эффектов
                        zvyk3 = False
                    else:
                        zvyk3 = True

        screen.blit(fon, (0, 0))
        screen.blit(fon1, (0, 0))
        if zvyk2:
            ok = pygame.transform.scale(load_image('data/off.png'), (400, 80))
            screen.blit(ok, (425, 55))
        else:
            ok = pygame.transform.scale(load_image('data/on.png'), (400, 80))
            screen.blit(ok, (425, 55))
        screen.blit(text3, (75, 75))
        if zvyk1:
            ok1 = pygame.transform.scale(load_image('data/off.png'), (400, 80))
        else:
            ok1 = pygame.transform.scale(load_image('data/on.png'), (400, 80))
        if zvyk3:
            sv = pygame.transform.scale(load_image('data/off.png'), (400, 80))
        else:
            sv = pygame.transform.scale(load_image('data/on.png'), (400, 80))
            screen.blit(ok1, (425, 155))
        screen.blit(ok1, (425, 155))
        screen.blit(text4, (75, 175))
        screen.blit(text8, (75, 375))
        screen.blit(sm, (25, 425))
        screen.blit(textef, (75, 275))
        screen.blit(sv, (425, 255))

        pygame.display.update()


def game():
    global symarno_banan
    global life
    global ochki
    global FPS
    ochki = 0
    if zvyk2:  # проверка не отключали ли звук в игре
        pygame.mixer.music.load('data/music2.mp3')
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(2)
    mus = pygame.mixer.Sound('data/poed.wav')
    yd = pygame.mixer.Sound('data/ydar.wav')
    hp = pygame.mixer.Sound('data/dlya hp.wav')
    for i in sprite_banana:  # удаление прошлых спрайтов
        i.kill()
    for i in all_sprites:
        i.kill()
    for i in zizn_sprite:
        i.kill()
    for i in dinam_sprite:
        i.kill()
    lis = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 3, 2,
           2]  # список рандомного падения предмета у некоторых больше шансов
    fon = pygame.transform.scale(load_image('data/fongreen.jpg'), (800, 600))
    screen.blit(fon, (0, 0))
    payz = pygame.transform.scale(load_image('data/payza.png'), (100, 50))
    screen.blit(payz, (0, 0))
    ava_banana = pygame.transform.scale(load_image('data/banan.png'), (50, 50))
    screen.blit(ava_banana, (560, 0))
    heart1 = pygame.transform.scale(load_image('data/heart.png'), (50, 50))
    screen.blit(heart1, (620, 0))
    heart2 = pygame.transform.scale(load_image('data/heart.png'), (50, 50))
    screen.blit(heart2, (680, 0))
    heart3 = pygame.transform.scale(load_image('data/heart.png'), (50, 50))
    screen.blit(heart3, (740, 0))
    r = pygame.font.Font(None, 50)
    text = r.render(str(ochki), True, (41, 255, 0))
    screen.blit(text, (520, 0))
    pygame.display.flip()
    pos = 320  # начальная позиция обезьяны
    m = pos  # слежка чтобы персонаж не выходил за границы
    pos2 = 480  # начальная позиция обезьяны
    Monkey(all_sprites)
    all_sprites.update(pos, pos2)
    all_sprites.draw(screen)
    pygame.display.update()
    sprite_banana.update()
    sprite_banana.draw(screen)
    ckor = True
    chet_banana = 10
    mesta = [0, 160, 320, 480, 640]  # места спавна объектов рандомно
    payza = False
    life = 3
    prom = 120  # для того что бы бананы падали через промежуток времени
    zad = 5  # задержка для замедления падания объектов
    while True:
        levo = False
        pravo = False
        prod = False
        me = False
        pygame.time.delay(zad)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()  # выключение
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT and m < 640:
                pravo = True  # передвижение на право
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT and m > 0:
                levo = True  # передвижение на лево
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                if payza:  # пауза на enter
                    payza = False
                else:
                    payza = True
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if 100 >= event.pos[0] >= 0 and 50 >= event.pos[1] >= 0:
                    payza = True  # пауза на мышку
                elif 600 >= event.pos[0] >= 200 and 400 >= event.pos[1] >= 250:
                    prod = True  # продолжить во время пауза
                elif 600 >= event.pos[0] >= 200 and 550 >= event.pos[1] >= 400:
                    me = True  # уйти в меню
        if ochki == 50:  # уровни скорости
            zad = 2
        elif ochki == 30:
            zad = 3
        elif ochki == 10:
            zad = 4
        if life == 0:  # проигрыш и сохранение результатов
            symarno_banan += ochki
            pygame.mixer.music.pause()
            sorted(kup)
            data = (symarno_banan, imya)
            pygame.mixer.music.load('data/music.mp3')
            con = sqlite3.connect('data/baza.db')
            cur = con.cursor()
            cur.execute("""UPDATE skins
                        SET kol = ?
                        WHERE nik = ?""", data)
            con.commit()
            con.close()
            start_screen()
        if not payza:  # нет паузы все нормально идет
            if pravo:
                pos = 160
                m += 160
                pos2 = 0
                all_sprites.update(pos, pos2)
            if levo:
                pos = -160
                m -= 160
                pos2 = 0
                all_sprites.update(pos, pos2)
            if chet_banana % prom == 0:  # добавление нового рандомного обекта
                x = random.choice(mesta)
                y = -120
                z = random.choice(lis)
                if z == 1:
                    BANANCHIKI(x, y, sprite_banana)
                elif z == 2:
                    SERDECHKI(x, y, zizn_sprite)
                elif z == 3:
                    HAE(x, y, dinam_sprite)
            screen.blit(fon, (0, 0))
            all_sprites.draw(screen)
            if ckor:  # мини замедление
                ckor = False
                sprite_banana.update()
                zizn_sprite.update()
                dinam_sprite.update()
            else:
                ckor = True
            dinam_sprite.draw(screen)
            sprite_banana.draw(screen)
            zizn_sprite.draw(screen)
            chet_banana += 1  # прибавления для счетчика чтобы вовремя появился новый обьект
            colisions = pygame.sprite.groupcollide(all_sprites, sprite_banana, False, True)
            if colisions:  # колизия с бананом и удаление, если касается, а также проигрывание эффекта если не отключили
                ochki += 1
                if zvyk3:
                    mus.play()
            colisions1 = pygame.sprite.groupcollide(all_sprites, zizn_sprite, False, True)
            if colisions1:  # колизия с сердцем и удаление, если касается, а также проигрывание эффекта если не отключили
                if zvyk3:
                    hp.play()
                if life < 3:
                    life += 1
            colisions2 = pygame.sprite.groupcollide(all_sprites, dinam_sprite, False, True)
            if colisions2:  # колизия с динамитом и удаление, если касается, а также проигрывание эффекта если не отключили
                life -= 1
                if zvyk3:
                    yd.play()
            screen.blit(payz, (0, 0))
            screen.blit(ava_banana, (560, 0))
            r = pygame.font.Font(None, 50)
            text = r.render(str(ochki), True, (255, 255, 0))
            screen.blit(text, (520, 0))
            if life == 1:  # количество жизни для отображения
                screen.blit(heart1, (620, 0))
                pygame.display.flip()
            elif life == 2:
                screen.blit(heart1, (620, 0))
                screen.blit(heart2, (680, 0))
                pygame.display.flip()
            elif life == 3:
                screen.blit(heart1, (620, 0))
                screen.blit(heart2, (680, 0))
                screen.blit(heart3, (740, 0))
                pygame.display.flip()
        else:  # остановка из-за паузы
            fon = pygame.transform.scale(load_image('data/fongreen.jpg'), (800, 600))
            screen.blit(fon, (0, 0))
            payz = pygame.transform.scale(load_image('data/payza.png'), (100, 50))
            screen.blit(payz, (0, 0))
            ava_banana = pygame.transform.scale(load_image('data/banan.png'), (50, 50))
            screen.blit(ava_banana, (560, 0))
            r = pygame.font.Font(None, 50)
            text = r.render(str(ochki), True, (255, 255, 0))
            screen.blit(text, (520, 0))
            pro = pygame.transform.scale(load_image('data/prodolzhit.png'), (400, 150))
            screen.blit(pro, (200, 250))
            menu = pygame.transform.scale(load_image('data/menu.png'), (400, 150))
            screen.blit(menu, (200, 400))
            pygame.display.flip()
            if prod:  # продолжение игры
                payza = False
            if me:  # уход в меню и включение другой музыкой
                if zvyk2:
                    pygame.mixer.music.pause()
                pygame.mixer.music.load('data/music.mp3')
                start_screen()
        clock.tick(FPS)


class Monkey(pygame.sprite.Sprite):  # класс для персонажа
    image = [pygame.image.load('data/osnova.png'), pygame.image.load('data/pix.png'),
             pygame.image.load('data/nepix.png'), pygame.image.load('data/nepix2.png')]

    def __init__(self, *group):
        super().__init__(*group)
        global skin
        self.image = Monkey.image[skin]  # спрайт - тот скин который выбран или по умолчанию
        self.rect = self.image.get_rect()

    def update(self, pos, pos2):
        self.rect = self.rect.move(pos, pos2)  # перемещение


class BANANCHIKI(pygame.sprite.Sprite):  # класс для бананов
    image = pygame.image.load('data/banan.png')

    def __init__(self, x, y, *group):
        super().__init__(*group)
        self.image = BANANCHIKI.image
        self.rect = self.image.get_rect()
        self.rect[0] = x
        self.rect[1] = y

    def update(self):
        global life
        global ochki
        self.rect = self.rect.move(0, 2)  # перемещение
        if self.rect[1] == 600:
            life -= 1  # если игрок не поймал, то отнимается одна жизнь


class SERDECHKI(pygame.sprite.Sprite):  # класс для сердечек
    image = pygame.image.load('data/life.png')

    def __init__(self, x, y, *group):
        super().__init__(*group)
        self.image = SERDECHKI.image
        self.rect = self.image.get_rect()
        self.rect[0] = x
        self.rect[1] = y

    def update(self):
        self.rect = self.rect.move(0, 2)  # перемещение


class HAE(pygame.sprite.Sprite):  # класс для динамита
    image = pygame.image.load('data/din.png')

    def __init__(self, x, y, *group):
        super().__init__(*group)
        self.image = HAE.image
        self.rect = self.image.get_rect()
        self.rect[0] = x
        self.rect[1] = y

    def update(self):
        self.rect = self.rect.move(0, 2)  # перемещение


def shop():
    global symarno_banan
    global skin
    global kup
    fon = pygame.transform.scale(load_image('data/fonlobi.jpg'), (800, 600))
    screen.blit(fon, (0, 0))
    fon1 = pygame.transform.scale(load_image('data/strelka.png'), (100, 50))
    screen.blit(fon1, (0, 0))
    on = pygame.transform.scale(load_image('data/on.png'), (200, 50))
    screen.blit(on, (40, 250))
    on2 = pygame.transform.scale(load_image('data/on.png'), (200, 50))
    screen.blit(on2, (300, 250))
    on3 = pygame.transform.scale(load_image('data/on.png'), (200, 50))
    screen.blit(on3, (560, 250))
    on4 = pygame.transform.scale(load_image('data/on.png'), (200, 50))
    screen.blit(on4, (40, 470))
    photo = pygame.transform.scale(load_image('data/osnova.png'), (160, 120))
    screen.blit(photo, (50, 90))
    photo1 = pygame.transform.scale(load_image('data/pix.png'), (160, 120))
    screen.blit(photo1, (310, 90))
    photo2 = pygame.transform.scale(load_image('data/nepix.png'), (160, 120))
    screen.blit(photo2, (570, 90))
    photo3 = pygame.transform.scale(load_image('data/nepix2.png'), (160, 120))
    screen.blit(photo3, (50, 350))
    d = pygame.font.Font(None, 75)
    text = d.render('ВСЁ ПО 100 БАНАНОВ', True, (0, 255, 0))
    screen.blit(text, (220, 350))
    ava_banana = pygame.transform.scale(load_image('data/banan.png'), (100, 70))
    screen.blit(ava_banana, (700, -10))
    r = pygame.font.Font(None, 50)
    text1 = r.render(str(symarno_banan), True, (255, 255, 0))
    screen.blit(text1, (630, 0))
    n = [0, 0, 0, 0]  # список - какой скин выбран
    n[skin] = 1  # нынешний скин
    if kup != [1, 0, 0, 0]:  # изменение кнопки выбранного скина
        if skin == 1:
            on2 = pygame.transform.scale(load_image('data/banan.png'), (200, 50))
            screen.blit(on2, (300, 250))
        elif skin == 2:
            on3 = pygame.transform.scale(load_image('data/banan.png'), (200, 50))
            screen.blit(on3, (560, 250))
        elif skin == 3:
            on4 = pygame.transform.scale(load_image('data/banan.png'), (200, 50))
            screen.blit(on4, (40, 470))
    else:
        on = pygame.transform.scale(load_image('data/banan.png'), (200, 50))
        screen.blit(on, (40, 250))
    pygame.display.flip()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if 0 <= event.pos[0] <= 100 and 0 <= event.pos[1] <= 50:
                    return  # возвращение в лобби
                elif 240 >= event.pos[0] >= 40 and 300 >= event.pos[1] >= 250:  # выбор скина
                    if kup[0] != 0:
                        if skin != 0:
                            skin = 0
                            n = [0, 0, 0, 0]
                            n[skin] = 1
                elif (500 >= event.pos[0] >= 300) and (
                        300 >= event.pos[1] >= 250):  # выбор скина и проверка куплен ли он
                    if kup[1] != 0:
                        if skin != 1:
                            skin = 1
                            n = [0, 0, 0, 0]
                            n[skin] = 1
                    elif symarno_banan >= 100:  # проверка хватает ли бананов на него, покупка и добавление в бд
                        kup[1] = 1
                        symarno_banan -= 100
                        con = sqlite3.connect('data/baza.db')
                        cur = con.cursor()
                        cur.execute("""UPDATE skins
                                    SET kol = ?
                                    WHERE nik = ?""", (symarno_banan, imya))
                        cur.execute("""UPDATE skins
                                    SET skin1 = 1
                                    WHERE nik = ?""", (imya,))
                        con.commit()
                        con.close()
                        skin = 1
                        n = [0, 0, 0, 0]
                        n[skin] = 1
                elif 760 >= event.pos[0] >= 560 and 300 >= event.pos[1] >= 250:  # выбор скина и проверка куплен ли он
                    if kup[2] != 0:
                        if skin != 2:
                            skin = 2
                            n = [0, 0, 0, 0]
                            n[skin] = 1
                    elif symarno_banan >= 100:  # проверка хватает ли бананов на него, покупка и добавление в бд
                        kup[2] = 1
                        symarno_banan -= 100
                        con = sqlite3.connect('data/baza.db')
                        cur = con.cursor()
                        cur.execute("""UPDATE skins
                                    SET kol = ?
                                    WHERE nik = ?""", (symarno_banan, imya))
                        cur.execute("""UPDATE skins
                                    SET skin2 = 2
                                    WHERE nik = ?""", (imya,))
                        con.commit()
                        con.close()
                        skin = 2
                        n = [0, 0, 0, 0]
                        n[skin] = 1
                elif 240 >= event.pos[0] >= 40 and 520 >= event.pos[1] >= 470:  # выбор скина и проверка куплен ли он
                    if kup[3] != 0:
                        if skin != 3:
                            skin = 3
                            n = [0, 0, 0, 0]
                            n[skin] = 1
                    elif symarno_banan >= 100:  # проверка хватает ли бананов на него, покупка и добавление в бд
                        kup[3] = 1
                        symarno_banan -= 100
                        con = sqlite3.connect('data/baza.db')
                        cur = con.cursor()
                        cur.execute("""UPDATE skins
                                    SET kol = ?
                                    WHERE nik = ?""", (symarno_banan, imya))
                        cur.execute("""UPDATE skins
                                    SET skin3 = 3
                                    WHERE nik = ?""", (imya,))
                        con.commit()
                        con.close()
                        skin = 3
                        n = [0, 0, 0, 0]
                        n[skin] = 1
        screen.blit(fon, (0, 0))
        screen.blit(fon1, (0, 0))
        for i in range(len(n)):  # изменение кнопок если скин менялся
            if n[i] == 1 and i == 0:
                on = pygame.transform.scale(load_image('data/banan.png'), (200, 50))
                screen.blit(on, (40, 250))
            elif n[i] == 0 and i == 0:
                on = pygame.transform.scale(load_image('data/on.png'), (200, 50))
                screen.blit(on, (40, 250))
            elif n[i] == 1 and i == 1:
                on2 = pygame.transform.scale(load_image('data/banan.png'), (200, 50))
                screen.blit(on2, (300, 250))
            elif n[i] == 0 and i == 1:
                on2 = pygame.transform.scale(load_image('data/on.png'), (200, 50))
                screen.blit(on2, (300, 250))
            elif n[i] == 1 and i == 2:
                on3 = pygame.transform.scale(load_image('data/banan.png'), (200, 50))
                screen.blit(on3, (560, 250))
            elif n[i] == 0 and i == 2:
                on3 = pygame.transform.scale(load_image('data/on.png'), (200, 50))
                screen.blit(on3, (560, 250))
            elif n[i] == 1 and i == 3:
                on4 = pygame.transform.scale(load_image('data/banan.png'), (200, 50))
                screen.blit(on4, (40, 470))
            elif n[i] == 0 and i == 3:
                on4 = pygame.transform.scale(load_image('data/on.png'), (200, 50))
                screen.blit(on4, (40, 470))
        screen.blit(photo, (50, 90))
        screen.blit(photo1, (310, 90))
        screen.blit(photo2, (570, 90))
        screen.blit(photo3, (50, 350))
        screen.blit(text, (220, 350))
        screen.blit(ava_banana, (700, -10))
        r = pygame.font.Font(None, 50)
        text1 = r.render(str(symarno_banan), True, (255, 255, 0))
        screen.blit(text1, (630, 0))
        pygame.display.update()


pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_icon(pygame.image.load('data/avatarka.jpg'))
screen.fill((255, 255, 255))
pygame.display.flip()
clock = pygame.time.Clock()
ochki = 0
life = 3
zvyk1 = True  # звук лобби
zvyk2 = True  # звук игры
zvyk3 = True  # звук эффектов
symarno_banan = 0  # всего бананов
kup = []  # список скинов
imya = ''  # нынешний ник
all_sprites = pygame.sprite.Group()
sprite_banana = pygame.sprite.Group()
zizn_sprite = pygame.sprite.Group()
dinam_sprite = pygame.sprite.Group()
skin = 0  # номер скина
vvod()
pygame.init()
size = 800, 600
screen = pygame.display.set_mode(size)
screen.fill((0, 0, 0))
running = True
while running:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit()

