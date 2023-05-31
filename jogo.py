#---- Iniciando o jogo ---- #
# ---- realizando imports necessários
import pygame
import random
from tela_jogo import tela_jogo
from config import largura , comprimento 

pygame.init()
pygame.mixer.init()

#Gera tela principal

window = pygame.display.set_mode((largura, comprimento))
pygame.display.set_caption('Navy Assault')


tela_jogo(window)


#finaliza

pygame.quit()