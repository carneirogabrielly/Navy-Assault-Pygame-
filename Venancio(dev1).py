import pygame 
import random 

pygame.init() #Inicializa o framework do pygame 

#---Gera tela principal 
largura = 650 # Largura da tela 
comprimento = 800 #Comprimento da tela 

window = pygame.display.set_mode((largura , comprimento)) #Inicializa o display da janela, com as suas dimensões 
pygame.display.set_caption('Navy Assault') #Coloca o título da janela 


# ---- Inicia assets (Imagem) 
#tamanho imagem oponente
largura_oponente = 80
comprimento_oponente = 100

#Tamanho imagem jogador
largura_jogador = 80
comprimento_jogador = 100

#Tamanho tiros 
largura_tiro = 35
comrpimento_tiro = 35 

#Tamanho vidas
largura_vida = 10
comprimento_vida = 10


#Imagens
imagem_fundo = pygame.image.load('Imagens/Fundo.png').convert() #Inicializa a imagem no pygame 
imagem_fundo = pygame.transform.scale(imagem_fundo , (650,800)) #Converte a imagem para a escala 

imagem_oponente = pygame.image.load('Imagens/Barco_inimigo/Barco_inimigo.png').convert_alpha()
imagem_oponente = pygame.transform.scale(imagem_oponente , (largura_oponente,comprimento_oponente))

imagem_jogador = pygame.image.load('Imagens/Barco_jogador/Barco/Barco_amigo.png').convert_alpha()
imagem_jogador = pygame.transform.scale(imagem_jogador , (largura_jogador,comprimento_jogador))

imagem_tiro = pygame.image.load('Imagens/Barco_jogador/Canhões/Canhões_jogador/Segundo_canhã_jogador/Tiro_canhão2.png')
imagem_tiro = pygame.transform.scale(imagem_tiro , (largura_tiro , comrpimento_tiro) )

imagem_tiro_inimigo = pygame.image.load('Imagens/Barco_jogador/Canhões/Canhões_jogador/Quarto_canhão_jogador/Tiro_canhão4.png')
imagem_tiro_inimigo = pygame.transform.scale(imagem_tiro_inimigo , (largura_tiro , comrpimento_tiro))

imagem_placar = pygame.image.load('Imagens/Foto_placar.png')
imagem_placar = pygame.transform.scale(imagem_placar , (100, 100))

fonte_placar = pygame.font.SysFont('cooper black' , 28 , True , False)
#Classe do navio inimigo 
class Inimigo(pygame.sprite.Sprite): #Classe dos navios inimigos 
    def __init__(self , imagem_oponente , all_sprites , todos_tiros_inimigo , imagem_tiro_oponente): #Essa classe baseia-se na entrada de uma imagem 
        pygame.sprite.Sprite.__init__(self) 
        self.image = imagem_oponente
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(1 , 560)
        self.rect.y = 1
        self.vx_oponente = random.randint(-2 , 2 )
        self.vy_oponente = 3.5
        self.all_sprites = all_sprites
        self.todos_tiros_inimigo = todos_tiros_inimigo
        self.imagem_tiro_inimigo = imagem_tiro_oponente
    def update(self):
        #Atualizando a posição do navio 
        self.rect.x += self.vx_oponente 
        self.rect.y += self.vy_oponente

        #Condições para reposcionar o inimigo: 
        if self.rect.x > 560:
            self.rect.x = 560
            self.vx_oponente = self.vx_oponente * -1
        if self.rect.x <  -30:
            self.rect.x = -30 
            self.vx_oponente = self.vx_oponente * -1 
        if self.rect.y > comprimento:
            self.rect.y = 1
            self.rect.x = random.randint(0 , 560)
    def tiro_inimigo(self):
        novo_tiro_inimigo = Tiro_inimigo(imagem_tiro_inimigo , self.rect.bottom  , self.rect.centerx)
        self.all_sprites.add(novo_tiro_inimigo)
        self.todos_tiros_inimigo.add(novo_tiro_inimigo)


#criando classe pro jogador
class jogador(pygame.sprite.Sprite):
    def __init__(self, imagem_jogador, all_sprites, todos_tiros, imagem_tiro):
        pygame.sprite.Sprite.__init__(self) 
        self.image = imagem_jogador
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.centerx = largura/2
        self.rect.bottom = comprimento - 10
        self.vx_jogador = 0
        self.all_sprites = all_sprites
        self.todos_tiros = todos_tiros
        self.imagem_tiro = imagem_tiro
    
    def update(self):
        # Atualização da posição da nave
        self.rect.x += self.vx_jogador

        # Mantem dentro da tela
        if self.rect.x > 595:
            self.rect.x = 595
        if self.rect.x < -60:
            self.rect.x = -59
            
    def tiro(self):
    # A nova bala vai ser criada logo acima e no centro horizontal da nave
        novo_tiro = Tiro(self.imagem_tiro, self.rect.top, self.rect.centerx)
        self.all_sprites.add(novo_tiro)
        self.todos_tiros.add(novo_tiro)
    
class Tiro(pygame.sprite.Sprite):
    # Construtor da classe.

    def __init__(self, img, bottom, centerx):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)

        self.image = img
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)

        # Coloca no lugar inicial definido em x, y do constutor
        self.rect.centerx = centerx
        self.rect.bottom = bottom +20
        self.speedy = -10  # Velocidade fixa para cima

    def update(self):
        # A bala só se move no eixo y
        self.rect.y += self.speedy

        # Se o tiro passar do inicio da tela, morre.
        if self.rect.bottom < 0:
            self.kill()

class Tiro_inimigo(pygame.sprite.Sprite):
    # Construtor da classe.

    def __init__(self, img, bottom, centerx):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)

        self.image = img
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)

        # Coloca no lugar inicial definido em x, y do constutor
        self.rect.centerx = centerx
        self.rect.bottom = bottom +20
        self.speedy = 5  # Velocidade fixa para cima

    def update(self):
        # A bala só se move no eixo y
        self.rect.y += self.speedy

        # Se o tiro passar do inicio da tela, morre.
        if self.rect.bottom < 0:
            self.kill()


#----Inicializa estrutura de dados 
game = True
#quantidade de vidas do jogador
vidas = 3
#placar
placar = 0 

#criando navios: 

all_sprites = pygame.sprite.Group() #É uma lista com mais funcionalidades
todos_tiros = pygame.sprite.Group()
todos_tiros_inimigo = pygame.sprite.Group()
n_inimigos = 4
todos_inimigos = pygame.sprite.Group()
for i in range(n_inimigos):
    navio = Inimigo(imagem_oponente , all_sprites , todos_tiros_inimigo , imagem_tiro_inimigo)
    all_sprites.add(navio)
    todos_inimigos.add(navio)

navio_amigo = jogador(imagem_jogador, all_sprites, todos_tiros, imagem_tiro)
all_sprites.add(navio_amigo)


#Relógio que controla o loop
clock = pygame.time.Clock()
FPS = 50
tempo_inimigo = 0 
#----Loop principal do jogo ---
while game: 
    clock.tick(FPS) 
    tempo_inimigo += 1 
    if tempo_inimigo == 50: 
        for i in todos_inimigos: 
            i.tiro_inimigo()
        tempo_inimigo = 0 
    # ----- Trata eventos
    for event in pygame.event.get(): #pygame.evente.get devolve uma lista com todos os eventos que ocorreram desde a última janela 
        # ----- Verifica consequências
        if event.type == pygame.QUIT: #Se o comando do evento for igual a pygame.quit, o loop acaba 
            game = False
        # Verifica se apertou alguma tecla.
        if event.type == pygame.KEYDOWN:
            # Dependendo da tecla, altera a velocidade.
            if event.key == pygame.K_LEFT:
                navio_amigo.vx_jogador -= 8
            if event.key == pygame.K_RIGHT:
                navio_amigo.vx_jogador += 8
            if event.key == pygame.K_SPACE:
                navio_amigo.tiro()
        # Verifica se soltou alguma tecla.
        if event.type == pygame.KEYUP:
            # Dependendo da tecla, altera a velocidade.
            if event.key == pygame.K_LEFT:
                navio_amigo.vx_jogador += 8
            if event.key == pygame.K_RIGHT:
                navio_amigo.vx_jogador -= 8

    all_sprites.update()

    if pygame.sprite.spritecollide(navio_amigo, todos_inimigos, True, pygame.sprite.collide_mask):
        vidas -= 1
        placar -= 1000
    for tirinho in todos_tiros:
        if pygame.sprite.spritecollide(tirinho, todos_inimigos, True, pygame.sprite.collide_mask)  :
            novo_inimigo = Inimigo(imagem_oponente , all_sprites , todos_tiros_inimigo , imagem_tiro_inimigo)
            all_sprites.add(novo_inimigo)
            todos_inimigos.add(novo_inimigo)
            tirinho.kill() 
            placar += 100
    if pygame.sprite.spritecollide(navio_amigo, todos_tiros_inimigo, True, pygame.sprite.collide_mask):
        vidas -= 1
        placar -= 500

    if vidas == 0:
        game = False 


    #Gera saídas 
    window.fill( (0 , 0 , 0)) #Colore a janela window com tudo em branco 
    window.blit(imagem_fundo , (0,0))   #Posiciona a imagem de fundo na janela window, na posição 0,0
    window.blit(imagem_placar , (550 , 5))
    all_sprites.draw(window)

    #Colocando placar
    superficie_placar = fonte_placar.render("{0}".format(placar) , True , (255 , 255 , 255))
    window.blit(superficie_placar , (560 , 40))

    #Autaliza estado do jogo 
    pygame.display.update() #Atualiza o estado do jogo observado a cada loop
#--- Finalização 
pygame.quit() #Finaliza o game     