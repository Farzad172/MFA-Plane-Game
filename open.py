import sys
import time
import pygame as pg
import pygame_widgets
from pygame_widgets.button import Button
import tkinter as tk
import random as r


# screen size
root = tk.Tk()
w = root.winfo_screenwidth()
h = root.winfo_screenheight()
root.destroy()

# primary
pg.init()

infinite = True
infinite2 = True
transparent = (0, 0, 0, 0)  # invisible
clock = pg.time.Clock()
screen = pg.display.set_mode((0, 0), pg.FULLSCREEN)

# title
pg.display.set_caption('MFA Plane Game')


#leaderboard

def saving(highest_s):
    with open('leaderboard.txt', 'a') as file:
        file.write("{0}\n".format(highest_s))


def leaderboard():
    x = 0
    output = []
    lboard = pg.font.SysFont("lboard.TTF", h//10)
    df = pg.font.SysFont("lboard.TTF", h // 10)
    lboard = lboard.render('Leaderboard', True, (102,100,100))
    def loading():
        with open('leaderboard.txt', 'r') as file:
            h = file.readlines()
            try:
                for i in h:
                    int(i.strip())
                    output.append(int(i))
            except ValueError:
                    i = 0
    loading()
    infinite3 = True
    gamebg = pg.image.load("space2.png")
    output = sorted(output, reverse= False)
    gamebg = pg.transform.scale(gamebg, (w, h))
    for hi_score in output:
       i = (w//2.5, h//2)
       l_value = df.render("Working on It!!!", True, (100, 1, 2))
       if x < 3:
           break
       else:
           x+= 1
    while infinite3:
       screen.blit(gamebg, (0,0))
       screen.blit(l_value, i)
       screen.blit(lboard, (w // 2.5, h // 75))
       x+=h//19
       pg.display.flip()
       events = pg.event.get()
       for event in events:
           if event.type == pg.KEYDOWN:
               if event.key == pg.K_q:
                   pg.quit()
                   sys.exit()
               elif event.key == pg.K_b:
                   button()
                   sel_screen()


def opening():
    gamebg = pg.image.load("space2.png")
    gamebg = pg.transform.scale(gamebg, (w, h))
    lf = pg.font.SysFont("font1.TTF", h // 10)
    f = pg.image.load("welcome.png")
    f = pg.transform.scale(f, (w//2, h//2))
    l_font1 = lf.render('Loading.', True, (102, 100, 102))
    l_font2 = lf.render('Loading..', True, (102, 100, 102))
    l_font3 = lf.render('Loading...', True, (102, 100, 102))
    l_font4 = lf.render('Loading....', True, (102, 100, 102))
    screen.blit(gamebg, (0, 0))
    screen.blit(f, (w//4, h//4))
    pg.display.flip()
    time.sleep(3)
    l_list = [l_font1, l_font2, l_font3, l_font4]
    for i in l_list:
        screen.blit(gamebg, (0, 0))
        screen.blit(i, (w//2.5-h//20, h//2-h//20))
        pg.display.flip()
        time.sleep(1)

#Calling function
opening()

def start():
    SCORE = 0
    LIFE = 3
    bulletnum = 6
    pg.font.init()
    sc_li = pg.font.SysFont("btnfont.ttf", h//30)
    Life = sc_li.render('LIFE:', True, (202, 23, 192))
    Score = sc_li.render('SCORE:', True, (202, 23, 192))
    gamebg = pg.image.load("space2.png")
    gamebg = pg.transform.scale(gamebg, (w, h))
    plane = pg.image.load("plane2.png")
    plane = pg.transform.scale(plane, (w//5, h//3))
    enemy1 = pg.image.load("asteroid.png")
    enemycol = pg.image.load("ast_col.png")
    enemycol = pg.transform.scale(enemycol, (w // 10, h // 7))
    bullet = pg.image.load("bullet.png")
    bullet = pg.transform.scale(bullet,(w//102.4, h//25.6))
    bulleta = pg.image.load("bullet.png")
    bulleta = pg.transform.scale(bulleta, (w // 102.4, h // 25.6))
    enemy1 = pg.transform.scale(enemy1, (w//10, h//7))
    firebox = pg.image.load("firebox.png")
    firebox = pg.transform.scale(firebox, (w//5, h//3))
    gameover = pg.image.load("gameover.png")
    gameover = pg.transform.scale(gameover, (w//1.8, h//1.9))
    life = pg.image.load("heart.png")
    life = pg.transform.scale(life, (w//51.1, h//38.4))
    x = 0
    y = 0
    x1 = 0
    y1 = -h
    px = w//2.4
    py = h//1.6
    planerect = plane.get_rect()
    bx = planerect.centerx+px
    by = planerect.centery+py
    mx = r.randint(w//10, w//1)
    my = -h//7.6
    fy = h//1.5
    fired = False
    fired2 = True

    # life animation
    def l(LIFE):
        if LIFE == 3:
            screen.blit(life, (w//1.1, h//51.2))
            screen.blit(life, (w//1.07, h//51.2))
            screen.blit(life, (w//1.04, h//51.2))
            pg.display.flip()
        elif LIFE == 2:
            screen.blit(life, (w//1.1, h//51.2))
            screen.blit(life, (w//1.07, h//51.2))
            pg.display.flip()
        elif LIFE == 1:
            screen.blit(life, (w//1.1, h//51.2))
            pg.display.flip()
        else:
            screen.blit(life, (w+1000, y+1000))
    # score
    def sc(SCORE):
        s = sc_li.render("SCORE: %d" % SCORE, True, (202, 23, 192))
        screen.blit(s, (w//11.3, h//78))
        pg.display.flip()

    def sc2(SCORE):
        sc_li2 = pg.font.SysFont("lboard.TTF", h // 25)
        s = sc_li2.render("Score: %d" % SCORE, True, (202, 23, 192))
        sc_rect = s.get_rect()
        sc_rect.center = w//2, h//2
        screen.blit(s, sc_rect)
        pg.display.flip()

    while infinite2:
        pg.display.set_caption("MFA Plane Game")
        planerect = plane.get_rect()
        if my != h//1.5:
            my += h//153.6
            if my>=h//1.5:
               my = -h//7.6
               mx = r.randint(w//10, w//1)
        for event in pg.event.get():
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_q:
                    pg.quit()
                    sys.exit()
                elif event.key == pg.K_RIGHT:
                    px += w//14.62
                    bx = planerect.centerx-px
                    by = planerect.centery+py
                    if px >= w:
                        px = w//2
                        bx = planerect.centerx - px
                        by = planerect.centery + py
                        event.key == False
                elif event.key == pg.K_LEFT:
                    px -= w//14.62
                    bx = planerect.centerx+px
                    by = planerect.centery+py
                    if px <= 0:
                        px = w//2
                        bx = planerect.centerx - px
                        by = planerect.centery + py
                        event.key == False
                elif event.key == pg.K_b:
                    button()
                    sel_screen()
                elif event.key == pg.K_r:
                    bulletnum = 6
                elif event.key == pg.K_SPACE:
                    if fired2 == True:
                      bulletnum-=1
                      fired = True
        if fired == True:
            by -= w//102.4
            if by >= my and bx >= mx and (mx + w//10) >= bx:
                SCORE += 10
                screen.blit(enemycol, (mx, my))
                pg.display.flip()
                pg.time.delay(1000)
                fired = False
                my = -h // 7.6
                mx = r.randint(w // 10, w // 1)
                bx = planerect.centerx+px
                by = planerect.centery+py
            else:
                if my > by:
                    bx = planerect.centerx + px
                    by = planerect.centery+py
                    fired = False
        y1 += 3
        y += 3
        screen.blit(gamebg, (x, y))
        screen.blit(gamebg, (x1, y1))
        screen.blit(bulleta,(bx, by))
        screen.blit(plane, (px, py))
        screen.blit(enemy1, (mx, my))
        screen.blit(Life, (w//1.16, h//50))
        l(LIFE)
        sc(SCORE)
        if (y > h):
            y = -h
        if y1 > h:
            y1 = -h
        if py <= my and px <= mx and ((px + w // 7.5) >= mx or (mx+ w//10 == px)):
            if LIFE == 0:
                SCORE -= 20
                screen.blit(firebox, (px, fy))
                pg.display.flip()
                pg.time.delay(3000)
                screen.blit(gamebg, (0, 0))
                screen.blit(gameover, (w//4.5, h//5.9))
                pg.display.flip()
                pg.time.delay(2000)
                screen.blit(gamebg, (0, 0))
                sc2(SCORE)
                saving(SCORE)
                pg.display.flip()
                pg.time.delay(3000)
                button()
                sel_screen()
            else:
                LIFE -= 1
                SCORE -= 20
                screen.blit(firebox, (px, fy))
                pg.display.flip()
                pg.time.delay(2000)
                mx = r.randint(w // 10, w // 1)
                my = -h // 7.6
        if bulletnum == 6:
            fired2 = True
            screen.blit(bullet, (w // 1.28, h // 1.164))
            screen.blit(bullet, (w // 1.28+w//102.4, h // 1.164))
            screen.blit(bullet, (w // 1.28+w//102.4+w//102.4, h // 1.164))
            screen.blit(bullet, (w // 1.28+w//102.4+w//102.4+w//102.4, h // 1.164))
            screen.blit(bullet, (w // 1.28+w//102.4+w//102.4+w//102.4+w//102.4, h // 1.164))
            screen.blit(bullet, (w // 1.28+w//102.4+w//102.4+w//102.4+w//102.4+w//102.4, h // 1.164))
        elif bulletnum == 5:
            fired2 = True
            screen.blit(bullet, (w // 1.28, h // 1.164))
            screen.blit(bullet, (w // 1.28+w//102.4, h // 1.164))
            screen.blit(bullet, (w // 1.28+w//102.4+w//102.4, h // 1.164))
            screen.blit(bullet, (w // 1.28+w//102.4+w//102.4+w//102.4, h // 1.164))
            screen.blit(bullet, (w // 1.28+w//102.4+w//102.4+w//102.4+w//102.4, h // 1.164))
            pg.display.flip()
        elif bulletnum == 4:
            fired2 = True
            screen.blit(bullet, (w // 1.28, h // 1.164))
            screen.blit(bullet, (w // 1.28+w//102.4, h // 1.164))
            screen.blit(bullet, (w // 1.28+w//102.4+w//102.4, h // 1.164))
            screen.blit(bullet, (w // 1.28+w//102.4+w//102.4+w//102.4, h // 1.164))
        elif bulletnum == 3:
            fired2 = True
            screen.blit(bullet, (w // 1.28, h // 1.164))
            screen.blit(bullet, (w // 1.28+w//102.4, h // 1.164))
            screen.blit(bullet, (w // 1.28+w//102.4+w//102.4, h // 1.164))
        elif bulletnum == 2:
            fired2 = True
            screen.blit(bullet, (w // 1.28, h // 1.164))
            screen.blit(bullet, (w // 1.28+w//102.4, h // 1.164))
        elif bulletnum == 1:
            fired2 = True
            screen.blit(bullet, (w // 1.28, h // 1.164))
        else:
            reload = sc_li.render('Relaod: press r !', True, (202, 23, 192))
            screen.blit(reload,(w // 1.28, h // 1.164))
            fired2 = False
            pg.display.flip()
        pg.display.update()
        pg.display.flip()
        clock.tick(60)

def help():
    txt = "How to play this game\n\t Press Start button to start game.\n\t Press b to back in the selecting screen.\n\t Press q or quit or exit button to exit.\n\t Press and hold Right button for right move & Left button for left move.\n\nCredit(s)\n\t All right reserved ©\n\nSome site for make this game:\n\t Picture help: pngall, pngaaa, pngfind, nicepng, pngitem\n\t Code help: w3schools, StackOverFlow\n\nAbout\n\t This game is made by MFA Gaming Zone.\n\t It is a plane game with thrill!\n\t Hope you will enjoy the game.\n\t Thanks or downloading & playing the game.\n\t Give your opinion in - araf0759@gmail.com"
    infinite3 = True
    def render_multiple_line(text, x, y, fsize):
        sys_font = pg.font.SysFont("font1.TTF", h // 25)
        lines = text.splitlines()
        for i, l in enumerate(lines):
            screen.blit(sys_font.render(l, 0, "white"), (x, y+fsize*i))
    while infinite3:
        screen.blit(sback1, (0, 0))
        render_multiple_line(txt, w//4, h//4, h//30)
        pg.display.flip()
        events = pg.event.get()
        for event in events:
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_q:
                    pg.quit()
                    sys.exit()
                elif event.key == pg.K_b:
                    button()
                    sel_screen()


def button():
    global st_btn, help_btn, lb_btn, quit_btn
    st_btn = Button(screen, w//10,h//2,w//9,h//15, text='Start', fontSize=h//30, margin=h//76, inactiveColour=(255,0,0), pressedColour=(0,255,0), radius= 50, onClick= lambda : start())
    help_btn = Button(screen, w // 10, h // 2 + h//10, w // 9, h //15, text='Help', fontSize=h//30, margin=h//76, inactiveColour=(255, 0, 0), pressedColour=(0, 255, 0), radius=50, onClick= lambda : help())
    lb_btn = Button(screen, w // 10, h // 2 + h // 5, w //9, h // 15, text='Leaderboard', fontSize=h//30, margin=h//76, inactiveColour=(255, 0, 0), pressedColour=(0, 255, 0), radius=50, onClick= lambda : leaderboard())
    quit_btn = Button(screen, w // 10, h // 2 + h//3, w // 9, h // 15, text='Exit', fontSize=h // 30, margin=h // 76, inactiveColour=(255, 0, 0), pressedColour=(0, 255, 0), radius=50, onClick=lambda: exit())


def sel_screen():
    button()
    global sback
    sback = pg.image.load('space2.png')
    global sback1
    sback1 = pg.transform.scale(sback, (w, h))
    sobj = pg.image.load('welcome.png')
    sobj = pg.transform.scale(sobj, (w//2, h//2))
    sx= 0
    sy = 0
    sy1 = -h
    sx1 = 0
    while True:
        events = pg.event.get()
        for event in events:
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_q:
                    pg.quit()
                    sys.exit()
        pygame_widgets.update(events)
        sy1 += 5
        sy += 5
        screen.blit(sback1, (sx, sy))
        screen.blit(sback1, (sx1, sy1))
        screen.blit(sobj,(w//3, h//3))
        st_btn.listen(events)
        st_btn.draw()
        help_btn.listen(events)
        help_btn.draw()
        lb_btn.listen(events)
        lb_btn.draw()
        quit_btn.listen(events)
        quit_btn.draw()
        if sy > h:
            sy = -h
        if sy1 > h:
            sy1 = -h
        pg.display.flip()
        pg.display.update()
        clock.tick(10)