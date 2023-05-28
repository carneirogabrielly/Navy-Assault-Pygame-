import pygame 
import random 
import time

pygame.init() #Inicializa o framework do pygame 
pygame.mixer.init()
#---Gera tela principal 
largura = 650 # Largura da tela 
comprimento = 800 #Comprimento da tela 

window = pygame.display.set_mode((largura , comprimento)) #Inicializa o display da janela, com as suas dimensões 
pygame.display.set_caption('Navy Assault') #Coloca o título da janela 


# ---- Inicia assets (Imagem) 
#tamanho imagem oponente
largura_oponente = 80 #Largura do navio do oponente
comprimento_oponente = 100 #Comprimento do navio do aponente 

#Tamanho imagem jogador
largura_jogador = 80 #Largura do navio do jogador 
comprimento_jogador = 100 #Comprimento do navio do jogador 

#Tamanho tiros 
largura_tiro = 35 #Largura da imagem do tiro 
comrpimento_tiro = 35 #Comprimento da imagem do Tiro 

#Tamanho vidas
largura_vida = 50 #Largura da imagem das vidas 
comprimento_vida = 50 #Comprimento da imagem das vidas 


#Imagens
assets = {} #Dicionário para guardar todos os assets do pygame 
assets['imagem_fundo'] = pygame.image.load('Imagens/Fundo.png').convert() #Inicializa a imagem no pygame guardando-a nos assets
assets['imagem_fundo'] = pygame.transform.scale(assets['imagem_fundo'] , (650,800)) #Converte a imagem para a escala 

assets['imagem_oponente'] = pygame.image.load('Imagens/Barco_inimigo/Barco_inimigo.png').convert_alpha() #Inicializando a imagem dos  navios oponentes e guardando-a em assets
assets['imagem_oponente'] = pygame.transform.scale(assets['imagem_oponente'] , (largura_oponente,comprimento_oponente)) #Convertendo a imagem do oponente para escala 

assets['imagem_jogador'] = pygame.image.load('Imagens/Barco_jogador/Barco/Barco_amigo.png').convert_alpha() #Inicializando a imagem do jogador 
assets['imagem_jogador'] = pygame.transform.scale(assets['imagem_jogador'] , (largura_jogador,comprimento_jogador)) #Convertendo-a em escala 

assets['imagem_tiro'] = pygame.image.load('Imagens/Barco_jogador/Canhões/Canhões_jogador/Segundo_canhã_jogador/Tiro_canhão2.png') #Inicializando a imagem do tiro
assets['imagem_tiro'] = pygame.transform.scale(assets['imagem_tiro'] , (largura_tiro , comrpimento_tiro) ) #Convertendo-a em escala 

assets['imagem_tiro_inimigo'] = pygame.image.load('Imagens/Barco_jogador/Canhões/Canhões_jogador/Quarto_canhão_jogador/Tiro_canhão4.png') #Inicializando a imagem do tiro do inimigo
assets['imagem_tiro_inimigo'] = pygame.transform.scale(assets['imagem_tiro_inimigo'] , (largura_tiro , comrpimento_tiro)) #Convertendo-a em escala

assets['imagem_placar'] = pygame.image.load('Imagens/Foto_placar.png') #Inicializandoa imagem do placar 
assets['imagem_placar'] = pygame.transform.scale(assets['imagem_placar'] , (100, 100)) #Transformando a imagem do placar em escala

assets['Imagem_vida'] = pygame.transform.scale(assets['imagem_jogador'], (largura_vida, comprimento_vida)) #Inicializando a imagem das vidas 

assets['fonte_placar'] = pygame.font.SysFont('cooper black' , 28 , True , False) #Definindo a fonte do número representado no placar 

anim_tiro_jogador = [] #Inicializando a lista que guardará as imagens das animações do tiro do jogador

for i in range(3): #Utilizando o for para, inicialmente, gerar a sequência de imagens da animação do tiro do jogador, tornando-a mais rápida
    arquivo = f'Imagens/Barco_jogador/Barco/anim_barco_jogador_{i}.png ' #Inicializando uma variável para armazenar o dado pra dar load na imagem
    imagem = pygame.image.load(arquivo).convert_alpha() #Inicializando a imagem do Arquivo no Pygame
    imagem = pygame.transform.scale(imagem,(largura_jogador,comprimento_jogador)) #Convertendo essas imagens na escala da imagem do jogador, para sobrepô-la
    anim_tiro_jogador.append(imagem) #Adicionando a imagem da lista da animação do tiro do jogador

assets['anim_tiro_jogador'] = anim_tiro_jogador #Adicionando a animação do tiro do jogador em assets

anim_explosion_barco_amigo = [] #Inicializando a lista de explosão do Barco 
for i in range(27): #Utilizando o for para otimizar o processo de converter todas as imagens da animação na animação da explosão 
    arquivo2 = f'Imagens/Barco_jogador/Barco/animação-destruição/{i}.png' #Inicializando uma variável para armazenar o dado pra dar load na imagem

    imagem = pygame.image.load(arquivo2).convert_alpha() #Inicializando a imagem do Arquivo no Pygame
    imagem = pygame.transform.scale(imagem,(110,110)) #Convertendo a imagem em escala
    anim_explosion_barco_amigo.append(imagem) #Repassando a imagem para a lista de animação da explosão 

assets['anim_explosion_barco_amigo'] = anim_explosion_barco_amigo #depositando a lista de sequência da animação da explosão do barco 

anim_explod_inimigo = [] #Inicializando a lista referente à animação da explosão do navio inimigo

for i in range(23): #Utilizando  o for para otimizar o processo 
    arquivo3 = f'Imagens/Barco_inimigo/explod_inimigo/{i}.png' #Inicializando uma variável para armazenar o dado pra dar load na imagem

    imagem = pygame.image.load(arquivo3).convert_alpha() #Inicializando a imagem do Arquivo no Pygame
    imagem = pygame.transform.scale(imagem, (110,110)) #Convertendo a imagem em escala
    anim_explod_inimigo.append(imagem) #Repassando a imagem para a lista de animação da explosão do inimigo

assets['anim_explod_inimigo'] = anim_explod_inimigo #Salvando a animação no dicionário assets 


#Sons 


pygame.mixer.music.load('Sons/Música_fundo.mp3') #Inicializando o som que tocará no fundo durante o game
pygame.mixer.music.set_volume(0.05) #Ajustando o seu volume
assets['som do tiro do jogador'] = pygame.mixer.Sound('Sons/tiro_jogador.ogg') #Inicializado o som do tiro do jogador
assets['som do tiro do jogador'].set_volume(0.01) #Ajustando o seu volume
assets['som do tiro do inimigo'] = pygame.mixer.Sound('Sons/tiro_oponente.wav') #Inicializando o som do tiro do oponente
assets['som do tiro do inimigo'].set_volume(0.01) #Ajustando o seu volume 
assets['som da explosão do jogador'] = pygame.mixer.Sound('Sons/explosão_barco.wav') #Inicializando o som da explosão do jogador
assets['som da explosão do jogador'].set_volume(0.05) #Ajustando o seu volume
assets['som da explosão do inimigo'] = pygame.mixer.Sound('Sons/Inimigo_explodindo.ogg') #Inicializando o som da explosão do inimigo
assets['som da explosão do inimigo'].set_volume(0.05) #Ajustando o seu volume


#Classe do navio inimigo 
class Inimigo(pygame.sprite.Sprite): #Classe dos navios inimigos 
    def __init__(self , assets , all_sprites , todos_tiros_inimigo): #Essa classe baseia-se na entrada dos assets, de todos os sprites e dos tiroes do inimigo
        pygame.sprite.Sprite.__init__(self) #Construtor da classe mãe 
        self.image = assets['imagem_oponente'] #Declarando que a imagem do oponente será o valor referente a essa chave do dicionário assets
        self.rect = self.image.get_rect() #Transformando a imagem em um retângulo com diversas propriedades
        self.rect.x = random.randint(1 , 560) #Sorteando a imagem do retângulo no eixo x 
        self.rect.y = 1 #Posicionando o navio inimigo no eixo y 
        self.vx_oponente = random.randint(-2 , 2 ) #Sorteando a velocidade do navio inimigo no eixo x 
        self.vy_oponente = 3.5 #Colocando a velocidade no eixo y 
        self.all_sprites = all_sprites #Declarando que o self.allsprites se equivalerá ao argumento all_sprites que será dado
        self.todos_tiros_inimigo = todos_tiros_inimigo #Declarando que o self.tiros do inimigo se equivalerá ao argumento todos_tiros_inimigo que será dado
        self.imagem_tiro_inimigo = assets['imagem_tiro_inimigo'] #Declarando que o self.tiros do inimigo se equivalerá ao argumento da imagem dos tiros que será dado dentro dos assets 
    def update(self): #Inicializando o método update dentro da classe 
        #Atualizando a posição do navio 
        self.rect.x += self.vx_oponente #Utilizando a posição do navio em x  baseado na velocidade em vx
        self.rect.y += self.vy_oponente #Utilizando a posição do navio em y  baseado na velocidade em vy

        #Condições para reposcionar o inimigo: 
        if self.rect.x > 595: #Se o navio inimigo passar da coordenada 595 da tela
            self.rect.x = 595 #Ele será reposcionado nela 
            self.vx_oponente = self.vx_oponente * -1 #E a velocidade do barco inimigo no eixo x se inverterá, para não ocorrerem bugs de movimento infinito
        if self.rect.x <  -30: #Limitando a posição do inimigo na questão negativa do eixo x 
            self.rect.x = -30 
            self.vx_oponente = self.vx_oponente * -1 
        if self.rect.y > comprimento: #Limitando a posição do navio caso passe do eixo y, se isso acontecer, ele voltará para a posção inicial no eixo y e terá uma posição sorteada novamente no eixo x 
            self.rect.y = 1
            self.rect.x = random.randint(0 , 560)
    def tiro_inimigo(self): #Inicializando
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
        if self.rect.x < -30:
            self.rect.x = -29
            
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
    def __init__(self, centrox, velocidadex, assets):
        pygame.sprite.Sprite.__init__(self)

        self.animacao = assets['anim_tiro_jogador']
        self.frame = 0
        self.image = self.animacao[self.frame]
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.centerx =  centrox 
        self.rect.centery = comprimento - 10  
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

            centrox = self.rect.centerx + self.speedx
            self.image = self.animacao[self.frame]
            self.rect = self.image.get_rect()
            self.rect.centerx =  centrox
            self.rect.centery = comprimento - 60

            if self.rect.x > 595:
                self.rect.x = 595
            if self.rect.x < -30:
                self.rect.x = -29
                

class explo_jogador(pygame.sprite.Sprite):
   def __init__(self, centro, assets):
        pygame.sprite.Sprite.__init__(self)

        self.explosao = assets['anim_explosion_barco_amigo']
        self.frame = 0
        self.image = self.explosao[self.frame]
        self.rect = self.image.get_rect()
        self.rect.center = centro
        self.ultima_vez = pygame.time.get_ticks()


        self.temporizador = 2

   def update(self):
        agora = pygame.time.get_ticks()


        tempo_decorrido = agora - self.temporizador

        if tempo_decorrido > self.temporizador:

            self.ultima_vez = agora


            self.frame += 1

        if self.frame == len(self.explosao):
            self.kill()

        else:

            centro = self.rect.center
            self.image = self.explosao[self.frame]
            self.rect = self.image.get_rect()
            self.rect.center =  centro

class explod_inimigo(pygame.sprite.Sprite):
   def __init__(self, centro, assets):
        pygame.sprite.Sprite.__init__(self)

        self.explosao = assets['anim_explod_inimigo']
        self.frame = 0
        self.image = self.explosao[self.frame]
        self.rect = self.image.get_rect()
        self.rect.center = centro
        self.ultima_vez = pygame.time.get_ticks()


        self.temporizador = 2

   def update(self):
        agora = pygame.time.get_ticks()


        tempo_decorrido = agora - self.temporizador

        if tempo_decorrido > self.temporizador:

            self.ultima_vez = agora


            self.frame += 1

        if self.frame == len(self.explosao):
            self.kill()

        else:

            centro = self.rect.center
            self.image = self.explosao[self.frame]
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
            assets['som do tiro do inimigo'].play()
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
                assets['som do tiro do jogador'].play()
                tiro = canhao_anim(navio_amigo.rect.centerx,navio_amigo.vx_jogador, assets)
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
        assets['som da explosão do inimigo'].play()
    hit_navio = pygame.sprite.groupcollide(todos_inimigos, todos_tiros, True, True, pygame.sprite.collide_mask)
    for navio in hit_navio:
        assets['som da explosão do inimigo'].play()
        novo_inimigo = Inimigo(assets , all_sprites , todos_tiros_inimigo)
        all_sprites.add(novo_inimigo)
        todos_inimigos.add(novo_inimigo)
        morte_inimigo = explod_inimigo(navio.rect.center, assets)
        all_sprites.add(morte_inimigo)
        placar += 100
        if placar % 500 == 0 and placar > 0:
            if placar / 500 not in vidas_ganhas:
                vidas += 1
                vidas_ganhas.append(placar / 500)
    if pygame.sprite.spritecollide(navio_amigo, todos_tiros_inimigo, True, pygame.sprite.collide_mask):
        vidas -= 1
        placar -= 500

    if vidas == 0:
        morte_jogador = explo_jogador(navio_amigo.rect.center, assets)
        all_sprites.add(morte_jogador)
        navio_amigo.kill()
        assets['som da explosão do jogador'].play()
    

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