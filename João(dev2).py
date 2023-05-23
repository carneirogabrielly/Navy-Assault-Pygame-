import pygame 
import math 

pygame.init() #Inicializa o framework do pygame 

#---Gera tela principal 
largura = 650 # Largura da tela 
comprimento = 800 #Comprimento da tela 
window = pygame.display.set_mode((largura , comprimento)) #Inicializa o display da janela, com as suas dimensões 
pygame.display.set_caption('Navy Assault') #Coloca o título da janela 

#----Inicializa estrutura de dados 
game = True
# ---- Inicia assets (Imagem) 
largura_jogador = 50#Largura do barco do jogador
altura_jogador = 38#Altura do barco do jogador
imagem_jogador = pygame.image.load('Imagens/Barco_jogador/Barco/Barco_amigo.png').convert()#Inicializa a imagem do jogador
imagem_jogador = pygame.transform.scale(imagem_jogador, (largura_jogador,altura_jogador)) #Converte a imagem da nave para a escala desejada
imagem_fundo = pygame.image.load('Imagens/Fundo.png').convert() #Inicializa a imagem no pygame 
imagem_fundo = pygame.transform.scale(imagem_fundo , (650,800)).convert() #Converte a imagem para a escala 


#----Loop principal do jogo ---
while game: 
    
    # ----- Trata eventos
    for event in pygame.event.get(): #pygame.evente.get devolve uma lista com todos os eventos que ocorreram desde a última janela 
        # ----- Verifica consequências
        if event.type == pygame.QUIT: #Se o comando do evento for igual a pygame.quit, o loop acaba 
            game = False

    #Gera saídas 
    window.fill( (0 , 0 , 0)) #Colore a janela window com tudo em branco 
    window.blit(imagem_fundo , (0,0))   #Posiciona a imagem de fundo na janela window, na posição 0,0
    #Autaliza estado do jogo 
    pygame.display.update() #Atualiza o estado do jogo observado a cada loop
#--- Finalização 
pygame.quit() #Finaliza o game 