
import pygame
import random
from pygame import mixer


pygame.init()
x= 1280
y= 720
#window game

screen= pygame.display.set_mode((x,y))
pygame.display.set_caption('deep space')
#background sound

mixer.music.load('music/backgroundMusic.mp3')
mixer.music.play(-1)

#colocando as imagens dentro do codigo

bg = pygame.image.load('img/galaxia.jpg').convert_alpha()
bg = pygame.transform.scale(bg,(x,y))

alien=pygame.image.load('img/alien.png').convert_alpha()
alien = pygame.transform.scale(alien,(50,50))
alien = pygame.transform.rotate(alien,-90)

fimkkj=pygame.image.load('img/fim.png').convert_alpha()
fimkkj=pygame.transform.scale(fimkkj,(x,y))

pausadokkj=pygame.image.load('img/pausado.png').convert_alpha()
pausadokkj=pygame.transform.scale(pausadokkj,(x,y))

alien2=pygame.image.load('img/alien2.png').convert_alpha()
alien2=pygame.transform.scale(alien2,(50,50))
alien2=pygame.transform.rotate(alien2,-90)

playerImg= pygame.image.load('img/nave.png').convert_alpha()
playerImg= pygame.transform.scale(playerImg,(50,50))#conversao do tamanho da nave
playerImg= pygame.transform.rotate(playerImg,-90)


missil= pygame.image.load('img/laser2.png').convert_alpha()
missil= pygame.transform.scale(missil,(25,25))#conversao do tamanho da nave
#missil= pygame.transform.rotate(missil,-45)



missil2=pygame.image.load('img/laser.png').convert_alpha()
missil2=pygame.transform.scale(missil2,(25,25))
#missil2=pygame.transform.rotate(missil2,-50)

pos_alien_x = 500
pos_alien_y= 360

pos_alien2_x= 600
pos_alien2_y=350

pos_player_x= 200
pos_player_y= 300


vel_x_missil = 0
pos_missil_x=200
pos_missil_y=300

vel_x_missil2=0
pos_missil2_x=200
pos_missil2_y=300


#FAVOR NAO MEXER NESSE PONTO, JÁ TA BUGADO E NÃO SABEMOS O MOTIVO, NÃO MEXER
pontos=2 
vidas=5

triggered= False
triggered2=False



rodando = True #variavel rodando o jogo
pausado=False #variavel de pausamento do jogo
fim=False #variavel do fim do jogo


font = pygame.font.SysFont('fonts/PixelGameFonte.ttf',50)
pause = pygame.font.SysFont('fonts/PixelGameFonte.ttf',70)
lifes=pygame.font.SysFont('fonts/PixelGameFonte.ttf',50)
fimm=pygame.font.SysFont('fonts/PixelGameFonte.ttf',50)



player_rect= playerImg.get_rect()
alien_rect= alien.get_rect()
alien2_rect=alien2.get_rect()
missil_rect=missil.get_rect()
missil2_rect=missil2.get_rect()




#funções
def respawn(): #funcao de respawn da primeira nave
    x= 1350
    y = random.randint(1,640)#a nave vai nascer pra dentro da tela ja em uma distancia de 1 X e  640 Y 
    return[x,y]

#dois respawns feitos em angulacoes de Y diferentes para nenhuma nave inimiga nascer junto ou dar B.O e nascer colado amem

def respawn2():#funcao de respawn da segunda nave
    x2= 1300
    y2 = random.randint(1,510)#a nave vai nascer pra "dentro" da tela, porem em algum lugar aleatorio da tela
    return[x2,y2]


def respawn_missil():#respawn do laser
    triggered=False
    respawn_missil_x = pos_player_x
    respawn_missil_y = pos_player_y

    vel_x_missil = 0
    return[respawn_missil_x, respawn_missil_y,triggered,vel_x_missil]

def respawn_missil2():#respawn do laser// basicamente serve pra respawnar o laser no proprio foguete ou nave
    triggered2=False
    respawn_missil2_x = pos_player_x
    respawn_missil2_y = pos_player_y

    vel_x_missil2 = 0
    return[respawn_missil2_x, respawn_missil2_y,triggered2,vel_x_missil2]


def colisoes():#colisoes 1 e pontos e vida
    global pontos #variavel global: pode ser lida e atualizada dentro e fora da funcao
    global vidas
    if player_rect.colliderect(alien_rect) or alien_rect.x==60:
        pontos -=1
        vidas-=1
        return True
    elif missil_rect.colliderect(alien_rect):

        kabum=mixer.Sound('music/kabum2.mp3')#sound effects, caso haja colisão vai rolar um efeito de explosao(em teoria)e o player ganha 1 ponto
        kabum.play()
        pontos+=1
        return True
    elif missil2_rect.colliderect(alien_rect):
        kabum=mixer.Sound('music/kabum2.mp3')
        kabum.play()
        pontos+=1
        return True
    else:
        return False

def colisoes2():#colisoes 2 e pontos e vida
    global pontos
    global vidas
    if player_rect.colliderect(alien2_rect) or alien2_rect.x == 60: #caso o player passe da nave inimiga ou bata
        pontos-=1
        vidas-=1
        return True
    elif missil_rect.colliderect(alien2_rect): #caso o missil 1 acerte o inimigo
        kabum2=mixer.Sound('music/kabum2.mp3')
        kabum2.play()
        pontos+=1
        return True
    elif missil2_rect.colliderect(alien2_rect):#caso o missil 2 acerte o inimigo

        kabum2=mixer.Sound('music/kabum2.mp3')
        kabum2.play()
        pontos+=1
        return True
    else:
        return False



while rodando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                rodando = False

    screen.blit(bg,(0,0))

    rel_x = x % bg.get_rect().width #resumidamente ele pega o
    screen.blit(bg,(rel_x - bg.get_rect().width,0))#cria background
    if rel_x <1280:
        screen.blit(bg,(rel_x,0))


    #teclas

    tecla= pygame.key.get_pressed()
    if tecla[pygame.K_UP]and pos_player_y >1:
        pos_player_y -=1
        if not triggered:
            pos_missil_y-=1
        if not triggered2:
            pos_missil2_y-=1

    if tecla[pygame.K_DOWN] and pos_player_y <665:
        pos_player_y +=1

        if not triggered:
            pos_missil_y+=1
        if not triggered2:
            pos_missil2_y+=1

    if tecla[pygame.K_SPACE]: #missil 1
        triggered = True
        vel_x_missil= 2
        tiro=mixer.Sound('music/tiro2.mp3')
        tiro.play()

    if tecla[pygame.K_a]: #missil 2
        triggered2=True
        vel_x_missil2= 2
        tiro = mixer.Sound('music/tiro2.mp3')
        tiro.play()


#tecla pra pausar
    if tecla[pygame.K_p]: #pause
        pausado=True

    if tecla[pygame.K_q]: #continua
        pausado=False

    if tecla[pygame.K_w]: #sair
        rodando=False

#quando as vidas chegam em 0 o jogo automaticamente se encerra
    if vidas== 0:
          fim==True
          screen.blit(fimkkj,(0,0))
          pygame.display.flip()
          continue
       

 #respawn

    if pos_alien_x ==50:
      pos_alien_x=respawn()[0]
      pos_alien_y= respawn()[1]

    if pos_alien2_x==50:
        pos_alien2_x=respawn2()[0]
        pos_alien2_y=respawn2()[1]

    if pos_missil_x==650:
        pos_missil_x,pos_missil_y,triggered,vel_x_missil = respawn_missil()

    if pos_missil2_x==650:
        pos_missil2_x,pos_missil2_y,triggered2,vel_x_missil2=respawn_missil2()

    if pos_alien_x== 50 or colisoes():
        pos_alien_x =respawn()[0]
        pos_alien_y= respawn()[1]

    if pos_alien2_x == 50 or colisoes2():
        pos_alien2_x = respawn2()[0]
        pos_alien2_y = respawn2()[1]

#sistema de pausamento do jogo
    if pausado == True:
        screen.blit(pausadokkj,(0,0))
        pygame.display.flip()
        continue


    #posicao rect ou posicao da hitbox
    player_rect.y= pos_player_y
    player_rect.x= pos_player_x

    missil_rect.x=pos_missil_x
    missil_rect.y=pos_missil_y

    missil2_rect.x=pos_missil2_x
    missil2_rect.y=pos_missil2_y

    alien_rect.x=pos_alien_x
    alien_rect.y=pos_alien_y

    alien2_rect.x = pos_alien2_x
    alien2_rect.y = pos_alien2_y



    #movimento
    x-=3
    pos_alien_x -=1
    pos_alien2_x -=1


    pos_missil_x +=vel_x_missil
    pos_missil2_x+=vel_x_missil2

    #pygame.draw.rect(screen,(255,0,0),player_rect,4)
    #pygame.draw.rect(screen,(255,0,0),missil_rect,4)
    #pygame.draw.rect(screen,(255,0,0),alien_rect,4)
    #pygame.draw.rect(screen,(255,0,0),alien2_rect,4)
    #pygame.draw.rect(screen,(255,0,0),missil2_rect,4)

    score=font.render(f'Pontos: {int(pontos)}',True,(255,255,255))
    screen.blit(score,(50,100))

    lifess=lifes.render(f'Vidas: {int(vidas)}',True,(255,255,255))
    screen.blit(lifess,(50,50))


    #criar imagens
    screen.blit(alien,(pos_alien_x,pos_alien_y))
    screen.blit(missil,(pos_missil_x,pos_missil_y))
    screen.blit(missil2,(pos_missil2_x,pos_missil2_y))
    screen.blit(playerImg,(pos_player_x,pos_player_y ))
    screen.blit(alien2,(pos_alien2_x,pos_alien2_y))


    print(pontos)
    print(vidas)


    pygame.display.update()
