import pygame
from pygame.locals import *
from sys import exit
from random import randint

pygame.init()

skiar = pygame.image.load('ski_normal.png')
arvore = pygame.image.load('arvore.png')
arvore1 = pygame.image.load('arvore1.png')
arvore2 = pygame.image.load('arvore2.png')
arvore3 = pygame.image.load('arvore3.png')
bandeira = pygame.image.load('ski_bandeira.png')

pygame.mixer.music.set_volume(0.4)
musica_de_fundo = pygame.mixer.music.load('BoxCat_Games_-_Battle__Normal_.wav')
pygame.mixer.music.play(-1)
    
som_bandeira = pygame.mixer.Sound('smw_kick.wav')

largura = 640
altura = 480
x = 300
y = 40
morreu = False
    
fonte = pygame.font.SysFont('arial', 30, True, True)
pontos = 0

pos_x = 300
pos_y = 800
posi_x_1 = 160
posi_y_1 = 800
posi_x_2 = 400
posi_y_2 = 800
posi_x_3 = 210
posi_y_3 = 800
banx = 300
bany = 400

def reiniciar_jogo():
    global pontos, x, y, pos_x, pos_y, posi_x_1, posi_y_1, posi_x_2, posi_y_2, posi_x_3, posi_y_3, banx, bany, morreu
    pontos = 0
    x = 300
    y = 40
    pos_x = 300
    pos_y = 800
    posi_x_1 = 160
    posi_y_1 = 800
    posi_x_2 = 400
    posi_y_2 = 800
    posi_x_3 = 210
    posi_y_3 = 800
    banx = 300
    bany = 400
    morreu = False

relogio = pygame.time.Clock()
velocidade = 23

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Ski')

while True:
    relogio.tick(20)
    tela.fill((255,255,255))
    mensagem = f'Pontos: {pontos}'
    texto_formatado = fonte.render(mensagem, True, (0,0,0))
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    pygame.draw.line(tela, (0,0,255),(106,0),(106,600), 20)
    pygame.draw.line(tela, (0,0,255),(520,0),(520,600),20)
    pygame.draw.line(tela, (100,100,100),(0,0),(0,600),193)
    pygame.draw.line(tela, (100,100,100),(630,0),(630,600),200)
    
    tela.blit(skiar,(x,y))
    tela.blit(arvore,(pos_x,pos_y))
    tela.blit(arvore1,(posi_x_1, posi_y_1))
    tela.blit(arvore2, (posi_x_2, posi_y_2))
    tela.blit(arvore3, (posi_x_3, posi_y_3))
    tela.blit(bandeira, (banx, bany))
    tela.blit(texto_formatado, (120, 10))

    if pygame.key.get_pressed()[K_a] and x >= 140:
        x = x -20
    if pygame.key.get_pressed()[K_d] and x <= 460:
        x = x +20

    if ((x + 10 > banx - 10 and y + 10 > bany + 10)) and ((x - 10 < banx + 1 and y - 10 < bany + 10)):
        pontos = pontos + 1
        som_bandeira.play()

    if ((x + 10 > pos_x - 10 and y + 15 > pos_y + 15)) and ((x - 10 < pos_x + 15 and y - 15 < pos_y + 15)):

        fonte2 = pygame.font.SysFont('arial', 20, True, True)
        mensagem = 'Game Over! Pressione a tecla W para jogar novamente'
        texto_form = fonte2.render(mensagem, True, (0,0,0))
        rect_texto = texto_form.get_rect()

        morreu = True
        while morreu:
            tela.fill((255,255,255))
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                if event.type == KEYDOWN:
                    if event.key == K_w:
                        reiniciar_jogo()

            rect_texto.center = (largura//2, altura//2)
            tela.blit(texto_form, rect_texto)
            pygame.display.update()

    if ((x + 10 > posi_x_1 - 10 and y + 15 > posi_y_1 + 15)) and ((x - 10 < posi_x_1 + 15 and y - 15 < posi_y_1 + 15)):

        fonte2 = pygame.font.SysFont('arial', 20, True, True)
        mensagem = 'Game Over! Pressione a tecla W para jogar novamente'
        texto_form = fonte2.render(mensagem, True, (0,0,0))
        rect_texto = texto_form.get_rect()

        morreu = True
        while morreu:
            tela.fill((255,255,255))
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                if event.type == KEYDOWN:
                    if event.key == K_w:
                        reiniciar_jogo()

            rect_texto.center = (largura//2, altura//2)
            tela.blit(texto_form, rect_texto)
            pygame.display.update()
     

    if ((x + 10 > posi_x_2 - 10 and y + 15 > posi_y_2 + 15)) and ((x - 10 < posi_x_2 + 15 and y - 15 < posi_y_2 + 15)):

        fonte2 = pygame.font.SysFont('arial', 20, True, True)
        mensagem = 'Game Over! Pressione a tecla W para jogar novamente'
        texto_form = fonte2.render(mensagem, True, (0,0,0))
        rect_texto = texto_form.get_rect()

        morreu = True
        while morreu:
            tela.fill((255,255,255))
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                if event.type == KEYDOWN:
                    if event.key == K_w:
                        reiniciar_jogo()

            rect_texto.center = (largura//2, altura//2)
            tela.blit(texto_form, rect_texto)
            pygame.display.update()
     

    if ((x + 10 > posi_x_3 - 10 and y + 15 > posi_y_3 + 15)) and ((x - 10 < posi_x_3 + 15 and y - 15 < posi_y_3 + 15)):

        fonte2 = pygame.font.SysFont('arial', 20, True, True)
        mensagem = 'Game Over! Pressione a tecla W para jogar novamente'
        texto_form = fonte2.render(mensagem, True, (0,0,0))
        rect_texto = texto_form.get_rect()

        morreu = True
        while morreu:
            tela.fill((255,255,255))
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                if event.type == KEYDOWN:
                    if event.key == K_w:
                        reiniciar_jogo()

            rect_texto.center = (largura//2, altura//2)
            tela.blit(texto_form, rect_texto)
            pygame.display.update()
     

    if pos_y <= -40:
        pos_y = randint(800,2000)
        pos_x = randint(140,460)
        
    if posi_y_1 <= -40:
        posi_y_1 = randint(800,2000)
        posi_x_1 = randint(140,460)
        
    if posi_y_2 <= -40:
        posi_y_2 = randint(800,2000)
        posi_x_2 = randint(140,460)
        
    if posi_y_3 <= -40:
        posi_y_3 = randint(800,2000)
        posi_x_3 = randint(140,460)
        
    if bany <= -60:
        bany = randint(800, 1000)
        banx = randint(140, 460)
       
    pos_y -= velocidade
    posi_y_1 -= velocidade 
    posi_y_2 -= velocidade 
    posi_y_3 -= velocidade
    bany -= velocidade
     
    pygame.display.update()
