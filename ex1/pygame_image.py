import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg")
    kk_image = pg.image.load("fig/3.png")
    kk_image = pg.transform.flip(kk_image,True,False)
    tmr = 0
    bg_x = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        screen.blit(bg_img, [bg_x, 0])
        screen.blit(kk_image,[300,200])
        pg.display.update()
        tmr += 1     
        bg_x -= 1   
        clock.tick(200)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()