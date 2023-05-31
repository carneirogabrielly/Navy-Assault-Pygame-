import pygame
import os
from config import METEOR_WIDTH, METEOR_HEIGHT, SHIP_WIDTH, SHIP_HEIGHT, IMG_DIR, SND_DIR, FNT_DIR


BACKGROUND = 'background'
METEOR_IMG = 'meteor_img'
METEOR_IMG = 'meteor_img'
SHIP_IMG = 'ship_img'
SHIP_IMG = 'ship_img'
BULLET_IMG = 'bullet_img'
EXPLOSION_ANIM = 'explosion_anim'
SCORE_FONT = 'score_font'
BOOM_SOUND = 'boom_sound'
DESTROY_SOUND = 'destroy_sound'
PEW_SOUND = 'pew_sound'

def carrega_imagens():
#Imagens
    assets = {}
    assets['imagem_fundo'] = pygame.image.load('Imagens/Fundo.png').convert() #Inicializa a imagem no pygame 
    assets['imagem_fundo'] = pygame.transform.scale(assets['imagem_fundo'] , (650,800)) #Converte a imagem para a escala 
    
    #imagem tela inicio
    assets['imagem_inicial'] = pygame.image.load('Imagens/tela_inicio.png').convert() #Inicializa a imagem no pygame
    assets['imagem_inicial'] = pygame.transform.scale(assets['imagem_inicial'] , (650,800)) #Converte a imagem para a escala 
    
    
    #imagem tela instruções
    assets['imagem_instrucoes'] = pygame.image.load('Imagens/instruções.png').convert() #Inicializa a imagem no pygame
    assets['imagem_instrucoes'] = pygame.transform.scale(assets['imagem_instrucoes'] , (650,800)) #Converte a imagem para a escala 
    

    #imagem tela de game over
    assets['game_over'] = pygame.image.load('Imagens/tela_game_over.png').convert() #Inicializa a imagem no pygame
    assets['game_over'] = pygame.transform.scale(assets['game_over'], (650,800)) #Converte a imagem para a escala 
    

    #imagem tela de vitória
    assets['tela_vitoria'] = pygame.image.load('Imagens/tela_vitoria.png') #Inicializa a imagem no pygame
    assets['tela_vitoria'] = pygame.transform.scale(assets['tela_vitoria'], (650,800)) #Converte a imagem para a escala 
    

    #imagem da embarcação do oponente
    assets['imagem_oponente'] = pygame.image.load('Imagens/Barco_inimigo/Barco_inimigo.png').convert_alpha() #Inicializa a imagem no pygame
    assets['imagem_oponente'] = pygame.transform.scale(assets['imagem_oponente'] , (largura_oponente,comprimento_oponente)) #Converte a imagem para a escala 

    #imagem da embarcação do jogador
    assets['imagem_jogador'] = pygame.image.load('Imagens/Barco_jogador/Barco/Barco_amigo.png').convert_alpha() #Inicializa a imagem no pygame
    assets['imagem_jogador'] = pygame.transform.scale(assets['imagem_jogador'] , (largura_jogador,comprimento_jogador)) #Converte a imagem para a escala 

    #imagem do tiro do jogador
    assets['imagem_tiro'] = pygame.image.load('Imagens/Barco_jogador/Canhões/Canhões_jogador/Segundo_canhã_jogador/Tiro_canhão2.png') #Inicializa a imagem no pygame
    assets['imagem_tiro'] = pygame.transform.scale(assets['imagem_tiro'] , (largura_tiro , comrpimento_tiro) ) #Converte a imagem para a escala 

    #imagem do tiro inimigo
    assets['imagem_tiro_inimigo'] = pygame.image.load('Imagens/Barco_jogador/Canhões/Canhões_jogador/Quarto_canhão_jogador/Tiro_canhão4.png') #Inicializa a imagem no pygame
    assets['imagem_tiro_inimigo'] = pygame.transform.scale(assets['imagem_tiro_inimigo'] , (largura_tiro , comrpimento_tiro)) #Converte a imagem para a escala 


    #imagem do placar que será printado
    assets['imagem_placar'] = pygame.image.load('Imagens/Foto_placar.png') #Inicializa a imagem no pygame
    assets['imagem_placar'] = pygame.transform.scale(assets['imagem_placar'] , (100, 100)) #Converte a imagem para a escala 

    #imagem do barco que representa a imagem do jogador
    assets['Imagem_vida'] = pygame.transform.scale(assets['imagem_jogador'], (largura_vida, comprimento_vida)) #Converte a imagem para a escala 

    #imagem do boss que aparece ao final
    assets['imagem_boss']  = pygame.image.load('Imagens/Boss/Boss.png') #Inicializa a imagem no pygame
    assets['imagem_boss'] = pygame.transform.scale(assets['imagem_boss'] , (largura_boss , comprimento_boss)) #Converte a imagem para a escala 

    #imagem do tiro de canhão do boss
    assets['imagem_bala_boss'] = pygame.image.load('Imagens/Boss/Bala_de_canhão_boss.png')  #Inicializa a imagem no pygame
    assets['imagem_bala_boss']  = pygame.transform.scale(assets['imagem_bala_boss'] , (largura_bala_boss , comprimento_bala_boss)) #Converte a imagem para a escala 

    #lista vazia da animação do tiro
    anim_tiro_jogador = []

    #armazenar a imagem na lista
    for i in range(3):
        arquivo = f'Imagens/Barco_jogador/Barco/anim_barco_jogador_{i}.png '
        imagem = pygame.image.load(arquivo).convert_alpha()
        imagem = pygame.transform.scale(imagem,(largura_jogador,comprimento_jogador))
        anim_tiro_jogador.append(imagem)

    #adicionando ao dicionário
    assets['anim_tiro_jogador'] = anim_tiro_jogador

    #fazendo animações da explosão do barco do jogador
    anim_explosion_barco_amigo = []
    for i in range(27):
        arquivo2 = f'Imagens/Barco_jogador/Barco/animação-destruição/{i}.png'

        imagem = pygame.image.load(arquivo2).convert_alpha()
        imagem = pygame.transform.scale(imagem,(110,110))
        anim_explosion_barco_amigo.append(imagem)

    #imagem sendo adicionada ao dicionário
    assets['anim_explosion_barco_amigo'] = anim_explosion_barco_amigo

    #criação da lista vazia para adicionar a animação da explosão do inimigo
    anim_explod_inimigo = []

    #adicionar as animacoes da explosão do inimigo na biblioteca assets
    for i in range(23):
        arquivo3 = f'Imagens/Barco_inimigo/explod_inimigo/{i}.png'

        imagem = pygame.image.load(arquivo3).convert_alpha()
        imagem = pygame.transform.scale(imagem, (110,110))
        anim_explod_inimigo.append(imagem)

    assets['anim_explod_inimigo'] = anim_explod_inimigo

    #criação lista vazia para animação tiro inimigo
    anim_tiro_inimigo2= []

    #adicionando na biblioteca as animações do tiro inimigo
    for i in range(3):
        arquivo4 = f'Imagens/Barco_inimigo/tiro_inimigo/{i}.png'

        imagem = pygame.image.load(arquivo4).convert_alpha()
        imagem = pygame.transform.scale(imagem, (80,100))
        anim_tiro_inimigo2.append(imagem)

    assets['anim_tiro_inimigo'] = anim_tiro_inimigo2

    assets['vida_boss'] = pygame.transform.scale(assets['imagem_boss'] , (50 , 50))

    #criação lista vazia para animação da explosão do boss
    anim_explod_boss = []

    #adicionando as animações no dicionario
    for i in range(49):
        arquivo5 = f'Imagens/Boss/explosão_boss/{i}.png'
        imagem = pygame.image.load(arquivo5).convert_alpha()
        imagem = pygame.transform.scale(imagem,(largura_boss,comprimento_boss))
        anim_explod_boss.append(imagem)

    assets['anim_explod_boss'] = anim_explod_boss

    #adicionando as fontes no dicionario
    assets['fonte_regen'] = pygame.font.SysFont('arial' , 28 , True , False)
    assets['fonte_placar'] = pygame.font.SysFont('cooper black' , 28 , True , False)


    #Sons 
    pygame.mixer.music.load('Sons/Música_fundo.mp3')
    pygame.mixer.music.set_volume(0.4)


    assets['som do tiro do jogador'] = pygame.mixer.Sound('Sons/tiro_jogador.ogg') #Carrega e armazena o som em uma variável
    assets['som do tiro do jogador'].set_volume(0.2) #altura do som

    assets['som do tiro do inimigo'] = pygame.mixer.Sound('Sons/tiro_oponente.wav') #Carrega e armazena o som em uma variável
    assets['som do tiro do inimigo'].set_volume(0.2)  #altura do som

    assets['som da explosão do jogador'] = pygame.mixer.Sound('Sons/explosão_barco.wav') #Carrega e armazena o som em uma variável
    assets['som da explosão do jogador'].set_volume(0.2)  #altura do som

    assets['som da explosão do inimigo'] = pygame.mixer.Sound('Sons/Inimigo_explodindo.ogg') #Carrega e armazena o som em uma variável
    assets['som da explosão do inimigo'].set_volume(0.2)  #altura do som

    assets['som do jogador travado'] = pygame.mixer.Sound('Sons/navio_n_atira.wav') #Carrega e armazena o som em uma variável
    assets['som do jogador travado'].set_volume(0.4)  #altura do som

    assets['jogador colidindo'] = pygame.mixer.Sound('Sons/contato_com_navio.wav') #Carrega e armazena o som em uma variável
    assets['jogador colidindo'].set_volume(0.3) #altura do som

    assets['jogador curando'] = pygame.mixer.Sound('Sons/barco_curando.wav') #Carrega e armazena o som em uma variável
    assets['jogador curando'].set_volume(0.6) #altura do som

    assets['boss_chegando'] = pygame.mixer.Sound('Sons/som_boss_chegando.flac') #Carrega e armazena o som em uma variável
    assets['boss_chegando'].set_volume(0.9) #altura do som

    assets['matou boss'] = pygame.mixer.Sound('Sons/win_sound.wav') #Carrega e armazena o som em uma variável
    assets['matou boss'].set_volume(0.9) #altura do som

    assets['boss atirando'] = pygame.mixer.Sound('Sons/son_explod_boss.wav') #Carrega e armazena o som em uma variável
    assets['boss atirando'].set_volume(0.3) #altura do som
    
    return assets
