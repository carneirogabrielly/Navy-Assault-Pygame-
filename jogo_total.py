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
    def tiro_inimigo(self): #Inicializando o método tiro do inimigo dentro da classe
        novo_tiro_inimigo = Tiro_inimigo(assets['imagem_tiro_inimigo'] , self.rect.bottom  , self.rect.centerx) #Chamando a classe tiro inimigo(que será mencioada a baixo) para inicializar o tiro dentro do navio do inimigo
        self.all_sprites.add(novo_tiro_inimigo) #Adicionando o tiro do inimigo em all sprites 
        self.todos_tiros_inimigo.add(novo_tiro_inimigo) #Adicionando o tiro do inimigo 


#criando classe pro jogador
class jogador(pygame.sprite.Sprite): #Iniciliazando a classe do jogador 
    def __init__(self, assets, all_sprites, todos_tiros, ): #A classe recebe assets, all sprites, todos os tiros do jogador
        pygame.sprite.Sprite.__init__(self) #Construtor da classe 
        self.image = assets['imagem_jogador'] #Tornando self.image  a imagem do jogador dentro de assets 
        self.mask = pygame.mask.from_surface(self.image) #Fazendo mascaras para melhorar a animação das colisões 
        self.rect = self.image.get_rect() #Transformando a imagem e m um retângulo
        self.rect.centerx = largura/2 #Posicionando o centro do navio no eixo x na metade da largura tela 
        self.rect.bottom = comprimento - 10 #Posicionando o menor ponto do eixo y do jogador nas cordenadas comprimento - 10
        self.vx_jogador = 0 #Inicializando a velocidade do jogador em x como 0 
        self.all_sprites = all_sprites #Definindo esse self como all s´rites
        self.todos_tiros = todos_tiros #Inicializando esse self como todos os tiros
        self.imagem_tiro = assets['imagem_tiro'] #Inicilizando o self de imagem tiro como assets imagem tiro 
    
    def update(self): #Inicializando o método updato 
        # Atualização da posição da nave
        self.rect.x += self.vx_jogador #Atualizando a velocidade do jogador baseado em x 

        # Mantem dentro da tela
        if self.rect.x > 595:
            self.rect.x = 595
        if self.rect.x < -30:
            self.rect.x = -29
            
    def tiro(self): #Inicializando o método Tiro
    # A nova bala vai ser criada logo acima e no centro horizontal da nave
        novo_tiro = Tiro(self.imagem_tiro, self.rect.top, self.rect.centerx) #Fazendo com o tiro do jogador o mesmo que foi feito com o inimigo
        self.all_sprites.add(novo_tiro) #Adicionando em all sprites 
        self.todos_tiros.add(novo_tiro) #Adicionando em todos os tiros 

     

    
class Tiro(pygame.sprite.Sprite): #Inicializando a classe tiro 
    # Construtor da classe.

    def __init__(self, img, bottom, centerx): #A classe recebe imagem, bottom e o centro de x dos navios 
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)

        self.image = img #Iniicializando o método self.image como a imagem que entra 
        self.rect = self.image.get_rect() #Transformando a imagem em um retângulo
        self.mask = pygame.mask.from_surface(self.image) #Transformando a imagem em uma máscara 

        # Coloca no lugar inicial definido em x, y do constutor
        self.rect.centerx = centerx #Posicionando o tiro no centro de x 
        self.rect.bottom = bottom +20 #Inicializando o seu bottom
        self.speedy = -10  # Velocidade fixa para cima

    def update(self): #Inicializando o método atualizando a posição
        # A bala só se move no eixo y
        self.rect.y += self.speedy #Atualizando a posição em y 

        # Se o tiro passar do inicio da tela, morre.
        if self.rect.bottom < 0:
            self.kill()

class Tiro_inimigo(pygame.sprite.Sprite): #Inicializando a classe tiro
    # Construtor da classe.

    def __init__(self, img, bottom, centerx): #Todos os processos do tiro inimigo serão iguais ao do tiro do navio do jogador
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


class canhao_anim(pygame.sprite.Sprite): #Classe da animação do canhão 
    def __init__(self, centrox, velocidadex, assets): #Recebe o centro de x do navio, a velocidade em x e os assets 
        pygame.sprite.Sprite.__init__(self)

        self.animacao = assets['anim_tiro_jogador'] #inicializa o self.animação a lista dos elementos da animação
        self.frame = 0 #O que define qual imagem irá ser passada na animação 
        self.image = self.animacao[self.frame] #Inicializa o self da imagem como o self.frame
        self.mask = pygame.mask.from_surface(self.image) #Transformando a imagem em máscara 
        self.rect = self.image.get_rect() #Transformando a imagem em rect 
        self.rect.centerx =  centrox 
        self.rect.centery = comprimento - 10  #Captura a posição do cnetro do retangulo da imagem no eixo 'y'
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

        self.explosao = assets['anim_explosion_barco_amigo']#atributo que armazena as imagens da animação
        self.frame = 0#numeração da imagem da animação
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

            


#----Inicializa estrutura de dados 
game = True
#quantidade de vidas do jogador
vidas = 3
vidas_ganhas = []#Armazena quais pontuações já cederam vida ao jogador 
#placar
placar = 0 

#criando navios: 

all_sprites = pygame.sprite.Group() #Uma lista que armazena todos os sprites do jogo 
todos_tiros = pygame.sprite.Group() #Lista que armazena somente os tiros do jogador 
todos_tiros_inimigo = pygame.sprite.Group()#lista que armazena todos os tiros dos inimigos 
n_inimigos = 4 #variável que armazena a quantidade de inimigos 
todos_inimigos = pygame.sprite.Group()#lista que armazena todos os inimigos
for i in range(n_inimigos):#loop para armazenar todos os inimigos dentro do grupo
    navio = Inimigo(assets , all_sprites , todos_tiros_inimigo)#Gerador do barco inimigo 
    all_sprites.add(navio)#adiciona o navio à lista de sprites 
    todos_inimigos.add(navio)#adiciona o navio a lista de inimigos 

navio_amigo = jogador(assets , all_sprites, todos_tiros)#gerador do navio do jogador 
all_sprites.add(navio_amigo)#adiciona o navio à lista de sprites 


#Relógio que controla o loop
clock = pygame.time.Clock()
FPS = 50#quantidade de imagens que são mostradas na tela por segundo 
tempo_inimigo = 0 #tempo em que o inimigo ira atirar 
#----Loop principal do jogo ---
while game: 
    clock.tick(FPS) 
    tempo_inimigo += 1 #adiciona tempo ao ocntador 
    if tempo_inimigo == 50:#verifica se já passou  o tempo necessário para o inimigo atirar 
        for i in todos_inimigos: #loop para acessar todos os inimigos dentro da lista
            i.tiro_inimigo()#faz o inimigo atirar 
            assets['som do tiro do inimigo'].play()#roda o som do tiro 
        tempo_inimigo = 0 #reinicia o contador de tempo após atirar 
    # ----- Trata eventos
    for event in pygame.event.get(): #pygame.evente.get devolve uma lista com todos os eventos que ocorreram desde a última janela 
        # ----- Verifica consequências
        if event.type == pygame.QUIT: #Se o comando do evento for igual a pygame.quit, o loop acaba 
            game = False#finaliza o jogo 
        # Verifica se apertou alguma tecla.
        if event.type == pygame.KEYDOWN:
            # Dependendo da tecla, altera a velocidade.
            if event.key == pygame.K_LEFT:#verifica a telca apertada 
                navio_amigo.vx_jogador -= 8#Faz o jogador se movimenta para a esquerda 
            if event.key == pygame.K_RIGHT:#verifica a tecla apertada 
                navio_amigo.vx_jogador += 8#faz o jogador se movimentar para a direita 
            if event.key == pygame.K_SPACE:#verifica a tecla apertada 
                navio_amigo.tiro()#Faz o navio do jogador atirar 
                assets['som do tiro do jogador'].play()#roda o som do tiro do jogador 
                tiro = canhao_anim(navio_amigo.rect.centerx,navio_amigo.vx_jogador, assets)#realiza a animação de tiro do jogador 
                all_sprites.add(tiro)#Adiciona a animação no grupo de sprites 

        # Verifica se soltou alguma tecla.
        if event.type == pygame.KEYUP:
            # Dependendo da tecla, altera a velocidade.
            if event.key == pygame.K_LEFT:#verifica tecla apertada 
                navio_amigo.vx_jogador += 8#Faz o jogador parar após soltar a tecla 
            if event.key == pygame.K_RIGHT:#verifica tecla apertada 
                navio_amigo.vx_jogador -= 8#faz o jogador parar após soltar a telca 

    all_sprites.update()#atualiza todos os eventos dos sprites dentro dos grupos 

    if pygame.sprite.spritecollide(navio_amigo, todos_inimigos, True, pygame.sprite.collide_mask):#verifica se houve colizão entre o jogador e algum inimigo
        novo_inimigo = Inimigo(assets , all_sprites , todos_tiros_inimigo)#cria inimigo novamente 
        all_sprites.add(novo_inimigo)#Adiciona sprite do inimigo no grupo de todos os sprites 
        todos_inimigos.add(novo_inimigo)#Adiciona sprite do inimigo no grupo de sprites dos inimigos 
        vidas -= 1#Diminui a quantidade de vida do jogador 
        placar -= 1000#Reduz a pontuação do jogador 
        assets['som da explosão do inimigo'].play()#Roda o som da explosão do inimigo
    hit_navio = pygame.sprite.groupcollide(todos_inimigos, todos_tiros, True, True, pygame.sprite.collide_mask)#Armazena todos os inimigos que foram acertados por tiros 
    for navio in hit_navio:#Acessa os inimigos 1 por 1 
        assets['som da explosão do inimigo'].play()#roda o som de explosão do inimigo 
        novo_inimigo = Inimigo(assets , all_sprites , todos_tiros_inimigo)#cria inimigo novamente 
        all_sprites.add(novo_inimigo)#Adiciona sprite do inimigo no grupo de todos os sprites 
        todos_inimigos.add(novo_inimigo)#Adiciona sprite do inimigo no grupo de sprites dos inimigos 
        morte_inimigo = explod_inimigo(navio.rect.center, assets)#roda animação de explosão do inimigo
        all_sprites.add(morte_inimigo)#Adiciona animação de explosão do inimigo no grupo de todos os sprites 
        placar += 100#adiciona os pontos do jogador 
        if placar % 500 == 0 and placar > 0:#verifica se o jogador ganhou 500 pontos
            if placar / 500 not in vidas_ganhas:#verifica se é a primeira vez que o jogador chegou nessa quantidade de pontos 
                vidas += 1#adiciona vidas ao jogador 
                vidas_ganhas.append(placar / 500)#acrescenta à lista de vidas ganhas essa quantidade de pontos 
    if pygame.sprite.spritecollide(navio_amigo, todos_tiros_inimigo, True, pygame.sprite.collide_mask):#Verifica colisão do jogdor com os tiros inimigos
        vidas -= 1#Reduz a quantidade de vidas 
        placar -= 500#Reduz a quantidade de pontos 

    if vidas == 0:#verifica se ainda tem vidas 
        morte_jogador = explo_jogador(navio_amigo.rect.center, assets)#roda animação de explosão do navio do jogador 
        all_sprites.add(morte_jogador)#adiciona a animação no grupo de todas as sprites 
        navio_amigo.kill()#Remove o navio do grupo de sprites 
        assets['som da explosão do jogador'].play()#Roda o som de explosão do navio do jogador 
    

    #Gera saídas 
    window.fill( (0 , 0 , 0)) #Colore a janela window com tudo em branco 
    window.blit(assets['imagem_fundo'] , (0,0))   #Posiciona a imagem de fundo na janela window, na posição 0,0
    window.blit(assets['imagem_placar'] , (550 , 5))#desenha a imagem do placar na janela do jogo 
    all_sprites.draw(window)#Desenha as imagens de todos os sprites na janela do jogo 

    #Colocando placar
    superficie_placar = assets['fonte_placar'].render("{0}".format(placar) , True , (255 , 255 , 255))#guarda a imagem da quantidade de pontos que será mostrada 
    window.blit(superficie_placar , (560 , 40))#desenha a quantidade de pontos na janela 

    #Colocando vidas
    x_vida = 25#posição inicial da imagem de vidas no eixo 'x' 
    y_vida = 10#posição inicial da imagem de vidas no eixo 'y'
    for i in range(vidas):#loop para gerar imagens das vidas 
        window.blit(assets['Imagem_vida'], (x_vida, y_vida))#desenha a imagem da vida na tela 
        x_vida += 25#move a posição da imagem no eixo 'x'
      
    #Autaliza estado do jogo 
    pygame.display.update() #Atualiza o estado do jogo observado a cada loop
#--- Finalização 
pygame.quit() #Finaliza o game     