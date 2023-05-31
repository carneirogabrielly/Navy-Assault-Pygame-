import pygame
from config import FPS, largura, comprimento, BLACK, YELLOW, RED
from assets import load_assets, DESTROY_SOUND, BOOM_SOUND, BACKGROUND, SCORE_FONT
from sprites import Ship, Meteor, Bullet, Explosion

def tela_jogo(window):

    assets = carrega_imagens()
    imagem_fundo_rect = assets['imagem_fundo'].get_rect()
    #Definindo variaveis do scroll
    imagem_fundo_bg = assets['imagem_fundo'].get_width()
    scroll = 0
    tiles = math.ceil(comprimento / imagem_fundo_bg) + 1
    #quantidade de vidas do jogador
    vidas = 3
    vidas_boss = 75
    vidas_ganhas = []#Armazena quais pontuações já cederam vida ao jogador 
    #placar
    placar = 0 
    #criando navios: 

    all_sprites = pygame.sprite.Group() #Uma lista que armazena todos os sprites do jogo 

    todos_tiros = pygame.sprite.Group() #Lista que armazena somente os tiros do jogador 
    todos_amigo = pygame.sprite.Group()
    todos_tiros_inimigo = pygame.sprite.Group()#lista que armazena todos os tiros dos inimigos 
    todos_tiros_boss = pygame.sprite.Group()
    n_inimigos = 4 #variável que armazena a quantidade de inimigos 
    todos_boss = pygame.sprite.Group()
    todos_inimigos = pygame.sprite.Group()#lista que armazena todos os inimigos

    groups = {}
    groups['all_sprites'] = all_sprites
    groups['todos_tiros'] = todos_tiros
    groups['todos_tiros_inimigo'] = todos_tiros_inimigo
    groups['todos_inimigos'] = todos_inimigos
    groups['todos_tiros_boss'] = todos_tiros_boss
    for i in range(n_inimigos):#loop para armazenar todos os inimigos dentro do grupo

        navio = Inimigo(assets , groups)#Gerador do barco inimigo 
        all_sprites.add(navio)#adiciona o navio à lista de sprites 
        todos_inimigos.add(navio)#adiciona o navio a lista de inimigos 

    navio_amigo = jogador(assets, groups)#gerador do navio do jogador 
    all_sprites.add(navio_amigo)#adiciona o navio à lista de sprites 
    navio_boss = Boss( assets , groups )
    todos_boss.add(navio_boss)
    todos_amigo.add(navio_amigo)
    #Relógio que controla o loop
    clock = pygame.time.Clock()

    FPS = 50  #quantidade de imagens que são mostradas na tela por segundo 
    tempo_inimigo = 0 #tempo em que o inimigo ira atirar 

    #Estados do próprio jogador  
    acabou = 5
    perdeu_vidas = 3
    regenerando = 4
    playing = 2
    tela_inicial = 0
    tela_instrucoes = 1
    game_over = 6
    matou_boss = 7
    venceu = 8
    state = tela_inicial

    #Estados do estágio do jogo 
    fase_1 = 10
    fase_final = 20 
    status_fase = fase_1
    #----Loop principal do jogo ---
    pygame.mixer.music.play(loops=-1)
    while state != game_over and state != venceu and state != acabou: 
        clock.tick(FPS) 
        while state == tela_inicial:
            window.fill( (0 , 0 , 0)) #Colore a janela window com tudo em branco 
            window.fill( (0 , 0 , 0))
            window.blit(assets['imagem_inicial'], imagem_fundo_rect)
            
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        state = tela_instrucoes


                if event.type == pygame.QUIT:
                    state = acabou

        while state == tela_instrucoes:
            window.fill( (0 , 0 , 0)) #Colore a janela window com tudo em branco 
            window.fill( (0 , 0 , 0))
            window.blit(assets['imagem_instrucoes'], imagem_fundo_rect)
            
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        state = playing

                if event.type == pygame.QUIT:
                    state = acabou
        tempo_fase1 = pygame.time.get_ticks()
        tempo_inimigo += 1 #adiciona tempo ao ocntador 
        if tempo_inimigo == 50:#verifica se já passou  o tempo necessário para o inimigo atirar 
            for i in todos_inimigos: #loop para acessar todos os inimigos dentro da lista
                i.tiro_inimigo()#faz o inimigo atirar 
                assets['som do tiro do inimigo'].play()#roda o som do tiro 
                anim_tiro2 = canhao_inimigo_anim(i.rect.centerx, i.rect.centery, i.vx_oponente,i.vy_oponente,  assets)
                all_sprites.add(anim_tiro2)
            tempo_inimigo = 0 #reinicia o contador de tempo após atirar 
        
        # ----- Trata eventos
        for event in pygame.event.get(): #pygame.evente.get devolve uma lista com todos os eventos que ocorreram desde a última janela 
            # ----- Verifica consequências
            if event.type == pygame.QUIT: #Se o comando do evento for igual a pygame.quit, o loop acaba 
                state = acabou #finaliza o jogo 
            # Verifica se apertou alguma tecla.
            if event.type == pygame.KEYDOWN:
                # Dependendo da tecla, altera a velocidade.
                if event.key == pygame.K_LEFT:#verifica a telca apertada 
                    navio_amigo.vx_jogador -= 8#Faz o jogador se movimenta para a esquerda 
                if event.key == pygame.K_RIGHT:#verifica a tecla apertada 
                    navio_amigo.vx_jogador += 8#faz o jogador se movimentar para a direita 
                if event.key == pygame.K_SPACE:#verifica a tecla apertada 
                    if state == playing:
                        navio_amigo.tiro()#Faz o navio do jogador atirar 
                        assets['som do tiro do jogador'].play()#roda o som do tiro do jogador 
                        tiro = canhao_anim(navio_amigo.rect.centerx,navio_amigo.vx_jogador, assets)#realiza a animação de tiro do jogador 
                        all_sprites.add(tiro)#Adiciona a animação no grupo de sprites 
                    if state == regenerando:
                        assets['som do jogador travado'].play()   
            # Verifica se soltou alguma tecla.
            if event.type == pygame.KEYUP:
                # Dependendo da tecla, altera a velocidade.
                if event.key == pygame.K_LEFT:#verifica tecla apertada 
                    navio_amigo.vx_jogador += 8#Faz o jogador parar após soltar a tecla 
                if event.key == pygame.K_RIGHT:#verifica tecla apertada 
                    navio_amigo.vx_jogador -= 8#faz o jogador parar após soltar a telca 

        all_sprites.update()#atualiza todos os eventos dos sprites dentro dos grupos 
        
        if state == playing and status_fase == fase_1: 
            if pygame.sprite.spritecollide(navio_amigo, todos_inimigos, True, pygame.sprite.collide_mask):#verifica se houve colizão entre o jogador e algum inimigo
                novo_inimigo = Inimigo(assets , groups)  #cria inimigo novamente 
                all_sprites.add(novo_inimigo)  #Adiciona sprite do inimigo no grupo de todos os sprites 
                todos_inimigos.add(novo_inimigo)  #Adiciona sprite do inimigo no grupo de sprites dos inimigos 
                vidas -= 1   #Diminui a quantidade de vida do jogador 
                assets['jogador colidindo'].play()
                placar -= 1000   #Reduz a pontuação do jogador 
                assets['som da explosão do inimigo'].play() #Roda o som da explosão do inimigo
                if vidas > 0: 
                    state = regenerando
                    tomou_tiro = pygame.time.get_ticks()
                else:
                    state = perdeu_vidas
                    morreu = pygame.time.get_ticks()
            hit_navio = pygame.sprite.groupcollide(groups['todos_inimigos'], groups['todos_tiros'], True, True, pygame.sprite.collide_mask)#Armazena todos os inimigos que foram acertados por tiros 
            for navio in hit_navio:   #Acessa os inimigos 1 por 1 
                assets['som da explosão do inimigo'].play()   #roda o som de explosão do inimigo 
                novo_inimigo = Inimigo(assets , groups)   #cria inimigo novamente 
                all_sprites.add(novo_inimigo)   #Adiciona sprite do inimigo no grupo de todos os sprites 
                todos_inimigos.add(novo_inimigo)  #Adiciona sprite do inimigo no grupo de sprites dos inimigos 
                morte_inimigo = explod_inimigo(navio.rect.center, assets)   #roda animação de explosão do inimigo
                all_sprites.add(morte_inimigo)  #Adiciona animação de explosão do inimigo no grupo de todos os sprites 
                placar += 100   #adiciona os pontos do jogador 
                if placar % 500 == 0 and placar > 0:  #verifica se o jogador ganhou 500 pontos
                    if placar / 500 not in vidas_ganhas:  #verifica se é a primeira vez que o jogador chegou nessa quantidade de pontos 
                        vidas += 1   #adiciona vidas ao jogador 
                        vidas_ganhas.append(placar / 500)  #acrescenta à lista de vidas ganhas essa quantidade de pontos 
            
            if pygame.sprite.spritecollide(navio_amigo, groups['todos_tiros_inimigo'], True, pygame.sprite.collide_mask):#Verifica colisão do jogdor com os tiros inimigos
                vidas -= 1     #Reduz a quantidade de vidas 
                placar -= 500 #Reduz a quantidade de pontos
                assets['jogador colidindo'].play()  
                if vidas > 0: 
                    state = regenerando
                    tomou_tiro = pygame.time.get_ticks()
                else:
                    state = perdeu_vidas
                    morreu = pygame.time.get_ticks()
        elif state == regenerando:
                now = pygame.time.get_ticks()
                assets['jogador curando'].play()
                if now - tomou_tiro > 3000:
                    state = playing
                    now = 0 
        #Verifica se o perdeu todas vidas 
        elif state == perdeu_vidas:
            morte_jogador = explo_jogador(navio_amigo.rect.center, assets)#roda animação de explosão do navio do jogador 
            all_sprites.add(morte_jogador)#adiciona a animação no grupo de todas as sprites 
            navio_amigo.kill()#Remove o navio do grupo de sprites 
            assets['som da explosão do jogador'].play()#Roda o som de explosão do navio do jogador
            tempo_morte =  pygame.time.get_ticks()
            if tempo_morte - morreu > 1500:
                state = game_over

        #Verifcia se o boss foi  morto 
        elif state == matou_boss:
            assets['matou boss'].play()
            explosao_boss = explod_boss(navio_boss.rect.center, assets)
            all_sprites.add(explosao_boss)
            navio_boss.kill()
            agora2 = pygame.time.get_ticks()
            if agora2 - boss_atingido > 1500:
                state = venceu
        
        #inicia  a segunda fase(boss)
        if tempo_fase1 - (1000 * 60) > 0 and status_fase == fase_1:
            status_fase = fase_final
            assets['boss_chegando'].play() #toca o som do boss chegando 
            for tiro_inimigo2 in todos_tiros_inimigo: #Acaba com todos os disparos dos anivos inimigos 
                tiro_inimigo2.kill()
            for navio_inimigo_morrer in todos_inimigos:#Acaba com todos os navios inimigos 
                    navio_inimigo_morrer.kill() 
            all_sprites.add(navio_boss)   # adiciona o boss no grupo de sprites 
            if vidas_boss > 0:
                navio_boss.tiro_boss()
                contagem_tiro_boss = 0
        #Verifica se está jogando contra o boss 
        if status_fase == fase_final:
            contagem_tiro_boss += 1
            if contagem_tiro_boss % 75 == 0 and vidas_boss > 0: #Verifica o tempo passado desde o ultimo disparo do boss
                navio_boss.tiro_boss() #Faz o boss atirar 
                assets['boss atirando'].play() #Toca o som de tiro do boss
            if state == playing: #Verifica se o jogador ainda está vivo 
                hits3 =  pygame.sprite.spritecollide(navio_amigo , todos_boss , False , pygame.sprite.collide_mask) # verifica se houve colisão entre o jogador e o boss
                if len(hits3) > 0:
                    vidas -= 1 
                    if vidas > 0:
                        state = regenerando
                        tomou_tiro = pygame.time.get_ticks()
                    if vidas == 0:
                        state = perdeu_vidas
                        morreu = pygame.time.get_ticks()
                
                hits4 = pygame.sprite.groupcollide(todos_boss , groups['todos_tiros'] , False, True, pygame.sprite.collide_mask) #aramazena a lsita de colisões entre o boss e o os tiros do jogador 
                if len(hits4) > 0:
                    for chave, valor in hits4.items():
                        vidas_boss -= 1
                        boss_atingido = pygame.time.get_ticks()
                        if vidas_boss == 0:
                            chave.kill()
                            state = matou_boss
                        for termo in valor: 
                            termo.kill() 
                hits5 = pygame.sprite.groupcollide(todos_amigo , groups['todos_tiros_boss'] , False , True , pygame.sprite.collide_mask) #armazena a lista de colisões entre o navio do jogador e os tiros do inimigo 
                if len(hits5) > 0: #verifica se houveram colisões 
                    for i in hits5: # percorre a lista com as máscaras dos sprites que colidiram 
                        vidas -= 1 # reduz a quantidade de vidas 
                        if vidas > 0: # verifica se ainda restam vidas para o jogador 
                            state = regenerando #troca o estado do jogador 
                            tomou_tiro = pygame.time.get_ticks() #armazena o momento em que o jogador é atingido
                        else:
                            state = perdeu_vidas # troca o estado do jogador 
                            morreu = pygame.time.get_ticks() #Armazena o momento em que o  jogador perde todas suas vidas 
        
        #Gera saídas 
        window.fill( (0 , 0 , 0)) #preenche a tela de preto
        window.blit(assets['imagem_fundo'] , (0,0))   #Posiciona a imagem de fundo na janela window, na posição 0,0
        for i in range(0, tiles):
            window.blit(assets['imagem_fundo'], (0, i * imagem_fundo_bg + scroll))
        
        #Colocando o scrool no fundo
        scroll -= 5
        
        #Resetando o scroll
        if abs(scroll) > imagem_fundo_bg:
            scroll = 0

        if status_fase == fase_1:
            window.blit(assets['imagem_placar'] , (550 , 5))  #desenha a imagem do placar na janela do jogo 
        all_sprites.draw(window)#Desenha as imagens de todos os sprites na janela do jogo 

        #Colocando placar
        if status_fase == fase_1: #verifica o status atual da fase do jogador 
            superficie_placar = assets['fonte_placar'].render("{0}".format(placar) , True , (255 , 255 , 255))#guarda a imagem da quantidade de pontos que será mostrada 
            window.blit(superficie_placar , (560 , 40))#desenha a quantidade de pontos na janela 
        #Colocando vidas
        x_vida = 25  #posição inicial da imagem de vidas no eixo 'x' 
        y_vida = 10  #posição inicial da imagem de vidas no eixo 'y'
        for i in range(vidas):#loop para gerar imagens das vidas 
            window.blit(assets['Imagem_vida'], (x_vida, y_vida))#desenha a imagem da vida na tela 
            x_vida += 25#move a posição da imagem no eixo 'x'

        if state == regenerando: #Condicional para mostrar o alerta de regeneração
            regen = assets['fonte_regen'].render('Regenerando...', True, (255,255,255)) #renderiza o texto na variável regen
            window.blit(regen , (largura/2 - 100 , 30)) #desenha o texto de alerta de regeneração na tela 
        

            #Autaliza estado do jogo 
        pygame.display.update() #Atualiza o estado do jogo observado a cada loop
    #--- Finalização 
    while state == game_over: #condicional para trocar para tela de derrota
        clock.tick(FPS)# roda os frames conforme a quantidade passada anterior mente
        window.fill( (0 , 0 , 0)) #Colore a janela window com tudo em branco 
        window.blit(assets['game_over'], imagem_fundo_rect) # preenche a tela com a imagem de fim de jogo 

        pygame.display.update() # atualiza a tela 
        for event in pygame.event.get(): # verifica todos as ações tomadas pelo jogador 
            if event.type == pygame.QUIT: # verifica se o jogador aperto o botão de fechar a janela 
                state = acabou # finaliza o jogo 

    while state == venceu: #condicional para trocar para tela de vitória 
        clock.tick(FPS) # roda os frames conforme a quantidade passada anterior mente 
        if agora2 - boss_atingido > 15: # verifica o tempo passado após a morte do boss
            window.fill( (0 , 0 , 0)) #Colore a janela window com tudo em branco 
            window.blit(assets['tela_vitoria'], imagem_fundo_rect) #desenha a imagem de vitória 

            pygame.display.update() #atualiza o display
            for event in pygame.event.get(): # verifica toda as ações tomadas pelo jogar 
                if event.type == pygame.QUIT: #verifica o tipo do evento
                    state = acabou # finaliza o jogo 
        
    if state == regenerando: # condicional para mostrar o alerta de regem 
            regen = assets['fonte_regen'].render('Regenerando...', True, (255,255,255)) # carrega o texto de regeneração 
            window.blit(regen , (largura/2 - 100 , 30)) #desenha o aviso de regeneração do barco 
