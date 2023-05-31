import random
import pygame
from config import largura, comprimento 
from assets import 


class Inimigo(pygame.sprite.Sprite): #Classe dos navios inimigos 
    def __init__(self , assets , groups): #Essa classe baseia-se na entrada de uma imagem 
        pygame.sprite.Sprite.__init__(self) 
        self.image = assets['imagem_oponente']
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(1 , 560)
        self.rect.y = 1
        self.vx_oponente = random.randint(-2 , 2 )
        self.vy_oponente = 3.5
        self.all_sprites = groups['all_sprites']
        self.todos_tiros_inimigo = groups['todos_tiros_inimigo']
        self.imagem_tiro_inimigo = assets['imagem_tiro_inimigo']

    def update(self):
        #Atualizando a posição do navio 
        self.rect.x += self.vx_oponente 
        self.rect.y += self.vy_oponente

        #Condições para reposcionar o inimigo: 
        if self.rect.x > 595:
            self.rect.x = 595
            self.vx_oponente = self.vx_oponente * -1
        if self.rect.x <  -30:
            self.rect.x = -30 
            self.vx_oponente = self.vx_oponente * -1 
        if self.rect.y > comprimento:
            self.rect.y = 1
            self.rect.x = random.randint(0 , 560)

    def tiro_inimigo(self):
        #posicionando o tiro
        novo_tiro_inimigo = Tiro_inimigo(assets['imagem_tiro_inimigo'] , self.rect.bottom  , self.rect.centerx)
        self.all_sprites.add(novo_tiro_inimigo)
        self.todos_tiros_inimigo.add(novo_tiro_inimigo)


#criando classe pro jogador
class jogador(pygame.sprite.Sprite):
    def __init__(self, assets, groups):
        pygame.sprite.Sprite.__init__(self) 
        self.image = assets['imagem_jogador']
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.centerx = largura/2
        self.rect.bottom = comprimento - 10
        self.vx_jogador = 0
        self.all_sprites = groups['all_sprites']
        self.todos_tiros = groups['todos_tiros']
        self.imagem_tiro = assets['imagem_tiro']
    
    def update(self):
        # Atualização da posição do barco
        self.rect.x += self.vx_jogador

        # Mantem dentro da tela
        if self.rect.x > 595:
            self.rect.x = 595
        if self.rect.x < -30:
            self.rect.x = -29
            
    def tiro(self):
    # criação da nova bala
        novo_tiro = Tiro(self.imagem_tiro, self.rect.top, self.rect.centerx)
        self.all_sprites.add(novo_tiro)
        self.todos_tiros.add(novo_tiro)

     

    
class Tiro(pygame.sprite.Sprite):
    # Construtor da classe do tiro do barco do jogador

    def __init__(self, img, bottom, centerx):
        pygame.sprite.Sprite.__init__(self)

        self.image = img
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)

        self.rect.centerx = centerx
        self.rect.bottom = bottom +20
        self.speedy = -10  # Velocidade fixa para cima

    def update(self):
        # A bala só se move no eixo y
        self.rect.y += self.speedy

        # Se o tiro passar do inicio da tela, morre.
        if self.rect.bottom < 0:
            self.kill()

#construindo classe do tiro inimigo
class Tiro_inimigo(pygame.sprite.Sprite):

    def __init__(self, img, bottom, centerx):
        pygame.sprite.Sprite.__init__(self)

        self.image = img
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)

        self.rect.centerx = centerx
        self.rect.bottom = bottom +20
        self.speedy = 5  # Velocidade fixa para cima

    def update(self):
        # A bala só se move no eixo y
        self.rect.y += self.speedy

        # Se o tiro passar do inicio da tela, morre.
        if self.rect.bottom < 0:
            self.kill()


#construindo a classe do boss que aparece ao final do jogo
class Boss(pygame.sprite.Sprite):
    def __init__(self , assets , groups):
        pygame.sprite.Sprite.__init__(self)
        self.image= assets['imagem_boss'] 
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.centerx = largura/2
        self.rect.bottom = 200
        self.vx_boss = 2
        self.vy_boss = 1
        self.todos_tiros_boss = groups['todos_tiros_boss']
        self.all_sprites = groups['all_sprites']
        self.imagem_tiro_boss = assets['imagem_bala_boss']

        self.tempo = pygame.time.get_ticks()
        self.subiu = False
    
    #atualizando os atributos da classe
    def update(self):
        self.rect.x += self.vx_boss
        self.rect.y += self.vy_boss
        
        #Condições para reposcionar o inimigo: 
        if self.rect.x > 450:
            self.rect.x = 449
            self.vx_boss = self.vx_boss * -1
        if self.rect.x <  -30:
            self.rect.x = -30 
            self.vx_boss = self.vx_boss * -1 
        if self.rect.top > 700:
            self.rect.y = 1
            self.rect.x = random.randint(0 , 300)
        if self.rect.bottom >= comprimento + 20:
            self.vy_boss = - 20
            self.vx_boss = 0
        if self.rect.top == -40:
            self.vx_boss = 2
            self.vy_boss = 1
            self.subiu = True
        
        if self.rect.bottom == comprimento/2 + 50 and self.subiu == True:
            self.vy_boss = 10
            self.vx_boss = 0
            self.subiu = False
    
    #atualizando os tiros do boss e carregando as imagens(canhões)
    def tiro_boss(self):
        novo_tiro_boss1 = Tiro_boss(assets['imagem_bala_boss'] , self.rect.bottom , self.rect.centerx , 0 , 10 )
        novo_tiro_boss2 = Tiro_boss(assets['imagem_bala_boss'] , self.rect.bottom , self.rect.centerx , 5, 10 )
        novo_tiro_boss3 = Tiro_boss(assets['imagem_bala_boss'] , self.rect.bottom , self.rect.centerx , -5 , 10 )
        self.todos_tiros_boss.add(novo_tiro_boss1)
        self.todos_tiros_boss.add(novo_tiro_boss2)
        self.todos_tiros_boss.add(novo_tiro_boss3)
        self.all_sprites.add(novo_tiro_boss1)
        self.all_sprites.add(novo_tiro_boss2)
        self.all_sprites.add(novo_tiro_boss3)

#criação da classe dos tiros do boss
class Tiro_boss(pygame.sprite.Sprite):
    def __init__(self, img , bottom , centerx , vx_tiro_boss , vy_tiro_boss):
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.centerx = centerx
        self.rect.bottom = bottom
        self.vy_tiro_boss = vy_tiro_boss
        self.vx_tiro_boss = vx_tiro_boss
    #atualizando as posições do tiro
    def update(self):
        self.rect.x += self.vx_tiro_boss
        self.rect.y += self.vy_tiro_boss

        if self.rect.left > largura or self.rect.right < 0:
            self.kill()
        if self.rect.bottom > comprimento:
            self.kill()

#criando classe da animação do canhao 
class canhao_anim(pygame.sprite.Sprite):

    def __init__(self, centrox, velocidadex, assets):
        pygame.sprite.Sprite.__init__(self)

        self.animacao = assets['anim_tiro_jogador']
        self.frame = 0
        self.image = self.animacao[self.frame]
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.centerx =  centrox 
        self.rect.centery = comprimento - 10  #Captura a posição do centro do retangulo da imagem no eixo 'y'
        self.speedx = velocidadex #Define a velocidade da animação(para acompanhar o barco após o tiro)
        self.ultima_vez = pygame.time.get_ticks()#Captura o tempo da animação


        self.temporizador = 10 #Tempo necessário para que rode outra animação

    def update(self):#Atualiza a classe
        agora = pygame.time.get_ticks()#Captura o tempo atual 


        tempo_decorrido = agora - self.temporizador#Verifica o tempo decorrido

        if tempo_decorrido > self.temporizador:#condição para que a animação continue a rodar 

            self.ultima_vez = agora #Captura o tempo da ultima animação


            self.frame += 1 #Atualiza a imagem que será usada

        if self.frame == len(assets['anim_tiro_jogador']): #verifica se está na ultima imagem
            self.kill()#finaliza a animação

        else:
            
            centrox = self.rect.centerx + self.speedx #Atualiza a posição da animação 
            self.image = self.animacao[self.frame]#Define nova imagem
            self.rect = self.image.get_rect()#Captura o espaço retangular da imagem
            self.rect.centerx =  centrox #Define a posição do centro da imagem no eixo 'x'
            self.rect.centery = comprimento - 60 # Define a posição do centro da imagem no eixo 'y'

            if self.rect.x > 595:#Verifica se a animação passou do limite positivo da tela
                self.rect.x = 595#Reposiciona a animação
            if self.rect.x < -30:#Verifica se a animação passou do limite negativo da tela 
                self.rect.x = -29#Reposiciona a animação
                

class explo_jogador(pygame.sprite.Sprite):#Represent a explosão do jogador
    
   def __init__(self, centro, assets): #construtor da classe 
        pygame.sprite.Sprite.__init__(self)# Construtor da classe mãe 

        self.explosao = assets['anim_explosion_barco_amigo']#Atributo que armazena as imagens da animação
        self.frame = 0#Numeração da imagem da animação
        self.image = self.explosao[self.frame]#Define a imagem atual da animação
        self.rect = self.image.get_rect()#Captura a área retangular da imagem
        self.rect.center = centro #Define a posição em 'x' e 'y' do centro da imagem
        self.ultima_vez = pygame.time.get_ticks()#Captura o tempo 


        self.temporizador = 2 #Tempo necessário para que rode outra animação

   def update(self):#atualiza a classe 
        agora = pygame.time.get_ticks()#Captura o tempo atual 


        tempo_decorrido = agora - self.temporizador#Verifica o tempo decorrido

        if tempo_decorrido > self.temporizador:#condição para que a animação continue a rodar 

            self.ultima_vez = agora#Captura o tempo da ultima animação


            self.frame += 1 #atualiza a que será usada

        if self.frame == len(self.explosao):#verifica se chegou à ultima imagem
            self.kill()#finaliza a animação

        else:

            centro = self.rect.center#Atualiza a posição da animação 
            self.image = self.explosao[self.frame]#Define nova imagem
            self.rect = self.image.get_rect()#Captura o espaço retangular da imagem
            self.rect.center =  centro#Define a posição em 'x' e 'y' do centro da imagem

class explod_inimigo(pygame.sprite.Sprite):#Representa a animação de explosão do inimigo
   
   def __init__(self, centro, assets):#Construtor da classe
        
        pygame.sprite.Sprite.__init__(self)#Construtor da classe mãe 

        self.explosao = assets['anim_explod_inimigo']#atributo que armazena as imagens da animação
        self.frame = 0#numeração da imagem da animação
        self.image = self.explosao[self.frame]#Define a imagem atual da animação
        self.rect = self.image.get_rect()#Captura a área retangular da imagem
        self.rect.center = centro#Define a posição em 'x' e 'y' do centro da imagem
        self.ultima_vez = pygame.time.get_ticks()#Captura o tempo 


        self.temporizador = 22 #Tempo necessário para que rode outra animação

   def update(self):#atualiza a classe 
        agora = pygame.time.get_ticks()#Captura o tempo atual 


        tempo_decorrido = agora - self.temporizador#Verifica o tempo decorrido

        if tempo_decorrido > self.temporizador:#condição para que a animação continue a rodar 

            self.ultima_vez = agora#Captura o tempo da ultima animação


            self.frame += 1#atualiza a que será usada

        if self.frame == len(self.explosao):#verifica se chegou à ultima imagem
            self.kill()#finaliza a animação

        else:

            centro = self.rect.center#Atualiza a posição da animação 
            self.image = self.explosao[self.frame]#Define nova imagem
            self.rect = self.image.get_rect()#Captura o espaço retangular da imagem
            self.rect.center =  centro#Define a posição em 'x' e 'y' do centro da imagem
       

#classe da animação do canhão do inimigo
class canhao_inimigo_anim(pygame.sprite.Sprite):
    
    def __init__(self, centerx, centery, velocidadex, velocidadey, assets):    
        pygame.sprite.Sprite.__init__(self)

        self.tiro = assets['anim_tiro_inimigo']
        self.frame = 0
        self.image = self.tiro[self.frame]
        self.rect = self.image.get_rect()
        self.rect.centerx = centerx
        self.rect.centery = centery
        self.ultima_vez = pygame.time.get_ticks()
        self.speedx = velocidadex
        self.speedy = velocidadey

        self.temporizador = 2

    def update(self):
        agora = pygame.time.get_ticks()#Captura o tempo atual 


        tempo_decorrido = agora - self.temporizador#Verifica o tempo decorrido

        if tempo_decorrido > self.temporizador:#condição para que a animação continue a rodar 

            self.ultima_vez = agora#Captura o tempo da ultima animação


            self.frame += 1 #atualiza a que será usada

        if self.frame == len(self.tiro):#verifica se chegou à ultima imagem
            self.kill()#finaliza a animação

        else:

            centrox = self.rect.centerx + self.speedx#Atualiza a posição da animação 
            centroy = self.rect.centery + self.speedy
            self.image = self.tiro[self.frame]#Define nova imagem
            self.rect = self.image.get_rect()#Captura o espaço retangular da imagem
            self.rect.centerx =  centrox#Define a posição em 'x' e 'y' do centro da imagem
            self.rect.centery = centroy

            if self.rect.x > 595:#Verifica se a animação passou do limite positivo da tela
                self.rect.x = 595#Reposiciona a animação
            if self.rect.x < -30:#Verifica se a animação passou do limite negativo da tela 
                self.rect.x = -29#Reposiciona a animação

class explod_boss(pygame.sprite.Sprite):#Representa a animação de explosão do inimigo
   
   def __init__(self, centro, assets):#Construtor da classe
        
        pygame.sprite.Sprite.__init__(self)#Construtor da classe mãe 

        self.explosao_boss = assets['anim_explod_boss']#atributo que armazena as imagens da animação
        self.frame = 0#numeração da imagem da animação
        self.image = self.explosao_boss[self.frame]#Define a imagem atual da animação
        self.rect = self.image.get_rect()#Captura a área retangular da imagem
        self.rect.center = centro#Define a posição em 'x' e 'y' do centro da imagem
        self.ultima_vez = pygame.time.get_ticks()#Captura o tempo 


        self.temporizador = 50 #Tempo necessário para que rode outra animação

   def update(self):#atualiza a classe 
        agora = pygame.time.get_ticks()#Captura o tempo atual 


        tempo_decorrido = agora - self.temporizador#Verifica o tempo decorrido

        if tempo_decorrido > self.temporizador:#condição para que a animação continue a rodar 

            self.ultima_vez = agora#Captura o tempo da ultima animação


            self.frame += 1#atualiza a que será usada

        if self.frame == len(self.explosao_boss):#verifica se chegou à ultima imagem
            self.kill()#finaliza a animação

        else:

            centro = self.rect.center#Atualiza a posição da animação 
            self.image = self.explosao_boss[self.frame]#Define nova imagem
            self.rect = self.image.get_rect()#Captura o espaço retangular da imagem
            self.rect.center =  centro#Define a posição em 'x' e 'y' do centro da imagem