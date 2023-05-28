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
largura_vida = 50
comprimento_vida = 50


#Imagens
assets = {}
assets['imagem_fundo'] = pygame.image.load('Imagens/Fundo.png').convert() #Inicializa a imagem no pygame 
assets['imagem_fundo'] = pygame.transform.scale(assets['imagem_fundo'] , (650,800)) #Converte a imagem para a escala 

assets['imagem_oponente'] = pygame.image.load('Imagens/Barco_inimigo/Barco_inimigo.png').convert_alpha()
assets['imagem_oponente'] = pygame.transform.scale(assets['imagem_oponente'] , (largura_oponente,comprimento_oponente))

assets['imagem_jogador'] = pygame.image.load('Imagens/Barco_jogador/Barco/Barco_amigo.png').convert_alpha()
assets['imagem_jogador'] = pygame.transform.scale(assets['imagem_jogador'] , (largura_jogador,comprimento_jogador))

assets['imagem_tiro'] = pygame.image.load('Imagens/Barco_jogador/Canhões/Canhões_jogador/Segundo_canhã_jogador/Tiro_canhão2.png')
assets['imagem_tiro'] = pygame.transform.scale(assets['imagem_tiro'] , (largura_tiro , comrpimento_tiro) )

assets['imagem_tiro_inimigo'] = pygame.image.load('Imagens/Barco_jogador/Canhões/Canhões_jogador/Quarto_canhão_jogador/Tiro_canhão4.png')
assets['imagem_tiro_inimigo'] = pygame.transform.scale(assets['imagem_tiro_inimigo'] , (largura_tiro , comrpimento_tiro))

assets['imagem_placar'] = pygame.image.load('Imagens/Foto_placar.png')
assets['imagem_placar'] = pygame.transform.scale(assets['imagem_placar'] , (100, 100))

assets['Imagem_vida'] = pygame.transform.scale(assets['imagem_jogador'], (largura_vida, comprimento_vida))

assets['fonte_placar'] = pygame.font.SysFont('cooper black' , 28 , True , False)

anim_tiro_jogador = []

for i in range(3):
    arquivo = f'Imagens/Barco_jogador/Barco/anim_barco_jogador_{i}.png '
    imagem = pygame.image.load(arquivo).convert_alpha()
    imagem = pygame.transform.scale(imagem,(largura_jogador,comprimento_jogador))
    anim_tiro_jogador.append(imagem)

assets['anim_tiro_jogador'] = anim_tiro_jogador
#Classe do navio inimigo 
class Inimigo(pygame.sprite.Sprite): #Classe dos navios inimigos 
    def __init__(self , assets , all_sprites , todos_tiros_inimigo): #Essa classe baseia-se na entrada de uma imagem 
        pygame.sprite.Sprite.__init__(self) 
        self.image = assets['imagem_oponente']
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(1 , 560)
        self.rect.y = 1
        self.vx_oponente = random.randint(-2 , 2 )
        self.vy_oponente = 3.5
        self.all_sprites = all_sprites
        self.todos_tiros_inimigo = todos_tiros_inimigo
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
        novo_tiro_inimigo = Tiro_inimigo(assets['imagem_tiro_inimigo'] , self.rect.bottom  , self.rect.centerx)
        self.all_sprites.add(novo_tiro_inimigo)
        self.todos_tiros_inimigo.add(novo_tiro_inimigo)


#criando classe pro jogador
class jogador(pygame.sprite.Sprite):
    def __init__(self, assets, all_sprites, todos_tiros, ):
        pygame.sprite.Sprite.__init__(self) 
        self.image = assets['imagem_jogador']
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.centerx = largura/2
        self.rect.bottom = comprimento - 10
        self.vx_jogador = 0
        self.all_sprites = all_sprites
        self.todos_tiros = todos_tiros
        self.imagem_tiro = assets['imagem_tiro']
    
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


class canhao_anim(pygame.sprite.Sprite):
    def __init__(self,centro,assets,velocidadex):
        pygame.sprite.Sprite.__init__(self)

        self.animacao = assets['anim_tiro_jogador']
        self.frame = 0
        self.image = self.animacao[self.frame]
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.center =  centro
        self.speedx = velocidadex
        self.ultima_vez = pygame.time.get_ticks()


        self.temporizador = 10 

    def update(self):
        agora = pygame.time.get_ticks()


        tempo_decorrido = agora - self.temporizador

        if tempo_decorrido > self.temporizador:

            self.ultima_vez = agora


            self.frame += 1

        if self.frame == len(assets['anim_tiro_jogador']):
            self.kill()

        else:
            centro = self.rect.center
            self.image = self.animacao[self.frame]
            self.rect = self.image.get_rect()
            self.rect.center =  centro
            


#----Inicializa estrutura de dados 
game = True
#quantidade de vidas do jogador
vidas = 3
vidas_ganhas = []
#placar
placar = 0 

#criando navios: 

all_sprites = pygame.sprite.Group() #É uma lista com mais funcionalidades
todos_tiros = pygame.sprite.Group()
todos_tiros_inimigo = pygame.sprite.Group()
n_inimigos = 4
todos_inimigos = pygame.sprite.Group()
for i in range(n_inimigos):
    navio = Inimigo(assets , all_sprites , todos_tiros_inimigo)
    all_sprites.add(navio)
    todos_inimigos.add(navio)

navio_amigo = jogador(assets , all_sprites, todos_tiros)
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
                tiro = canhao_anim(navio_amigo.rect.center, assets)
                all_sprites.add(tiro)

        # Verifica se soltou alguma tecla.
        if event.type == pygame.KEYUP:
            # Dependendo da tecla, altera a velocidade.
            if event.key == pygame.K_LEFT:
                navio_amigo.vx_jogador += 8
            if event.key == pygame.K_RIGHT:
                navio_amigo.vx_jogador -= 8

    all_sprites.update()

    if pygame.sprite.spritecollide(navio_amigo, todos_inimigos, True, pygame.sprite.collide_mask):
        novo_inimigo = Inimigo(assets , all_sprites , todos_tiros_inimigo)
        all_sprites.add(novo_inimigo)
        todos_inimigos.add(novo_inimigo)
        vidas -= 1
        placar -= 1000
    for tirinho in todos_tiros:
        if pygame.sprite.spritecollide(tirinho, todos_inimigos, True, pygame.sprite.collide_mask)  :
            novo_inimigo = Inimigo(assets , all_sprites , todos_tiros_inimigo)
            all_sprites.add(novo_inimigo)
            todos_inimigos.add(novo_inimigo)
            tirinho.kill() 
            placar += 100
            if placar % 500 == 0 and placar > 0:
                if placar / 500 not in vidas_ganhas:
                    vidas += 1
                    vidas_ganhas.append(placar / 500)
    if pygame.sprite.spritecollide(navio_amigo, todos_tiros_inimigo, True, pygame.sprite.collide_mask):
        vidas -= 1
        placar -= 500

    if vidas == 0:
        game = False 
    

    #Gera saídas 
    window.fill( (0 , 0 , 0)) #Colore a janela window com tudo em branco 
    window.blit(assets['imagem_fundo'] , (0,0))   #Posiciona a imagem de fundo na janela window, na posição 0,0
    window.blit(assets['imagem_placar'] , (550 , 5))
    all_sprites.draw(window)

    #Colocando placar
    superficie_placar = assets['fonte_placar'].render("{0}".format(placar) , True , (255 , 255 , 255))
    window.blit(superficie_placar , (560 , 40))

    #Colocando vidas
    x_vida = 25
    y_vida = 10
    for i in range(vidas):
        window.blit(assets['Imagem_vida'], (x_vida, y_vida))
        x_vida += 25
      
    #Autaliza estado do jogo 
    pygame.display.update() #Atualiza o estado do jogo observado a cada loop
#--- Finalização 
pygame.quit() #Finaliza o game     