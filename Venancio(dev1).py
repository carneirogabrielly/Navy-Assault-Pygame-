from typing import Any
import pygame 
import math 
import random


pygame.init() #Inicializa o framework do pygame 

#---Gera tela principal 
largura = 650 # Largura da tela 
comprimento = 800 #Comprimento da tela 

window = pygame.display.set_mode((largura , comprimento)) #Inicializa o display da janela, com as suas dimensões 
pygame.display.set_caption('Navy Assault') #Coloca o título da janela 


# ---- Inicia assets (Imagem) 
#Dimensões das imagens 
largura_oponente = 130  
comprimento_oponente = 160
largura_jogador = 180
comprimento_jogador = 210
#Imagens
imagem_fundo = pygame.image.load('Imagens/Fundo.png').convert() #Inicializa a imagem no pygame 
imagem_fundo = pygame.transform.scale(imagem_fundo , (650,800)) #Converte a imagem para a escala 

imagem_oponente = pygame.image.load('Imagens/Barco_inimigo/Barco_inimigo.png').convert_alpha()
imagem_oponente = pygame.transform.scale(imagem_oponente , (largura_oponente,comprimento_oponente))

imagem_jogador =  pygame.image.load('Imagens/Barco_jogador/Barco/Barco_amigo.png').convert_alpha()
imagem_jogador = pygame.transform.scale(imagem_jogador , (largura_jogador,comprimento_jogador))

#----Inicializa estrutura de dados 
game = True

#Classe do jogador 
class Player(pygame.sprite.Sprite):
    def __init__(self , imagem_jogador):
        pygame.sprite.Sprite.__init__(self)
        
        self.image = imagem_jogador
        self.rect = self.image.get_rect()
        self.rect.centerx = largura/2
        self.rect.bottom = comprimento - 20
        self.vxj = 0
        self.vyj = 0
    def update(self):
        self.rect.x += self.vxj
        self.rect.y += self.vyj
        if self.rect.left < 0: 
            self.rect.left = 1 
        if self.rect.right > largura:
            self.rect.right = largura - 10
        if self.rect.top > comprimento:
            self.rect.y = comprimento
        if self.rect.y > comprimento - 150:
            self.rect.y = comprimento - 150

#Classe do navio inimigo 
class Inimigo(pygame.sprite.Sprite): #Classe dos navios inimigos 
    def __init__(self , imagem_oponente): #Essa classe baseia-se na entrada de uma imagem 
        pygame.sprite.Sprite.__init__(self) #Classe base simples para objetos de jogos visíveis
        self.image = imagem_oponente #definindo a imagem como a imagem dada na função
        self.rect = self.image.get_rect() #convertendo a imagem em um retangulo para conseguir utilizar os comandos rect
        self.rect.x = random.randint(1 , 650) #posição no eixo x do retângulo
        self.rect.y = random.randint(-1,1) #posição no eixo y do retângulo
        self.vx_oponente = 1.5 #velocidade do navio em x 
        self.vy_oponente = 6 #velocidade do navio em y 
    
    def update(self): #Função para, quando for acionada dentro da classe, atualizar a posição do jogador
        #Atualizando a posição do navio 
        self.rect.x += self.vx_oponente 
        self.rect.y += self.vy_oponente
        #Condições para reposcionar o inimigo: 
        if self.rect.left > largura:
            self.rect.x = largura - 10 
            self.vx_oponente = self.vx_oponente * -1
        if self.rect.right <  0:
            self.rect.x = 0
            self.vx_oponente = self.vx_oponente * -1 
        if self.rect.top > comprimento:
            self.rect.y = 1
            self.rect.x = random.randint(0 , 650)


#criando navios: 
todos_elementos  = pygame.sprite.Group() #É uma lista com mais funcionalidades
n_inimigos = 4
for i in range(n_inimigos):
    navio = Inimigo(imagem_oponente)
    todos_elementos.add(navio)
#player 
player = Player(imagem_jogador)
todos_elementos.add(player)


#Relógio que controla o loop
clock = pygame.time.Clock()
FPS = 50

#----Loop principal do jogo ---
while game: 
    clock.tick(FPS)
    # ----- Trata eventos
    for event in pygame.event.get(): #pygame.evente.get devolve uma lista com todos os eventos que ocorreram desde a última janela 
        # ----- Verifica consequências
        if event.type == pygame.QUIT: #Se o comando do evento for igual a pygame.quit, o loop acaba 
            game = False
        if event.type == pygame.KEYDOWN:
            if event.type == pygame.K_LEFT:
                player.vxj -= 8
            if event.type == pygame.K_RIGHT:
                player.vxj += 8
            if event.type == pygame.K_UP:
                player.vyj -= 4
            if event.type == pygame.K_DOWN:
                player.vyj += 4
        
        if event.type == pygame.KEYUP:
            # Dependendo da tecla, altera a velocidade.
            if event.key == pygame.K_LEFT:
                player.vxj += 8/2
            if event.key == pygame.K_RIGHT:
                player.vxj -= 8/2
            if event.key == pygame.K_UP:
                player.vyj += 4/2
            if event.key == pygame.K_DOWN:
                player.vyj -= 4/2
        
    todos_elementos.update() #Atualizando a posição do inimigo 
    #Gera saídas 
    window.fill( (0 , 0 , 0)) #Colore a janela window com tudo em branco 
    window.blit(imagem_fundo , (0,0))   #Posiciona a imagem de fundo na janela window, na posição 0,0
    todos_elementos.draw(window)
    #Autaliza estado do jogo 
    pygame.display.update() #Atualiza o estado do jogo observado a cada loop
#--- Finalização 
pygame.quit() #Finaliza o game 