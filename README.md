# Navy Assault pygame-

# Descrição do projeto
    1. O que é o projeto? 
        Navy assault é um game programado na linguagem de programação Python. A ideia do jogo é trazer um cenário baseado em uma batalha na água, no qual, o cenário simulará um espaço de deslocamento em um local com àgua.Assim, o jogador é um navio simples, que atira e movimenta-se horizontalmente, e os obstáculos são navios inimigos, que movimentam-se horizontalmente e verticalmente, e também atiram. 
    2. Como funciona o loop do jogo? 
        - Mecânicas do jogador:
        Como já citado, o jogador joga a partir de um navio, que  possui mecânicas de mover-se no eixo x , por meio das setas no teclado, em que, na seta esquerda, o jogador move-se para a esquerda, e, na seta direita, o jogador move-se para a direita, também possui a mecânica de atirar, que é acionada quando a tecla espaço do teclado é pressionada. Além disso,  o navio do jogador inicia o jogo com 3 vidas, ao perder todas, o jogo encerra-se. Ademais, o jogador  apresenta formas de ganhar vidas ao atingir placares, quando os placares atingidos são múltiplos de 500, para cada navio inimigo que o jogador destrói ele ganha 100 pontos. Porém, existem ressalvas importantes nessa questão : as vidas só serão adicionadas caso o múltiplo de 500 obtido no placar já não tenham siddo obtidos, e, se o placar no qual o jogador estiver seja maior do que 0. 

        -Mecânicas do Inimigo: 
        Os inimigos são navios que movem-se horizontalmente e verticalmente, e, após cada segundo, cada um dos inimigos atiram, e, quabdo eles batem no eixo x, o vetor velocidade do navio assume o seu sentido oposto. Além disso, quando os navios ultrapassam o comprimento da tela, eles voltam ao topo da tela. Cada inimigo apresenta apenas 1 vida.  

        -Chefão: 
        Após dado intervalo de tempo, aparece um boss na tela, o boss aparece na tela, ele atira 3 canhões de uma vez, e movimenta-se, assim como os navios inimigos aanteriores, em ambos os eixos, porém, com velocidades diferentes. As mecânicas de ultrapassagem de tela são similires às mecânicas citadas no oponente. Além disso, o diferencial é que o boss apresenta 75 vidas, o que torna mais difícil de matá-lo.

        -Mecânica de colisões: 
        Navios Inimigos iniciais com tiro do jogador: Como já dito, o jogador atirará ao ser apertada a tecla espaço. Quando o tiro do jogador colidir com o corpo do navio do inimigo, quando isso ocorre, o navio inimigo morrerá, por apresentar só uma vida, e, além disso, o jogador ganhará 100 pontos a mais no placar. 

        Navios Inimigos iniciais com navio do jogador: Quando o navio inimigo colidir com o jogador, o jogador perderá uma vida, e, entrará em uma estado de 'regeneração, no qual não poderá sofrer colisões, e não poderá atirar, e o navio inimigo morrerá. Além disso, o jogador perderá 1000 pontos no placar.
        
        Navio do Jogador com tiros do inimigo: Quando o jogador colidir com o tiro que o inimigo lançará, o jogador perderá uma vida, e, novamente, é implementada a questão da regeneração. Nessa situação, o jogador perderá 500 pontos no placar. 
    
    3. Objetivos do projeto  
        A proposta do jogo é entregar ao usuário uma experiência de jogatina simples e rápida, de modo a garantir o entretenimento ao mesmo. Além disso, o projeto busca explorar maiores conhecimentos acerca de utilização da linguagem de programação Python.

    
    4. O que foi aprendido?
        O projeto foi muito importante para estimular nos desenvolvedores uma capacidade de pensamento crítico dos desenvolvedores, no qual foi estimulado a capacidade de identificar e resolver problemas na elaboração desse jogo. 
    
# Como instalar e executar o projeto? 
    1.Inicialmente, é necessário, para baixar-lô, ter-se acesso ao github, pois, como trata-se de um projeto com diversos desenvolvedores, foi-se utilizado dessa platafora para haver uma contribuição conjunta dos desenvolvedores, e decumentar o código;

    2.Além disso, é necessário ter uma plataforma com terminais para rodar a linguagem de programação Python. Dessa forma, recomenda-se a instalção da plataforma ''Visual Studio Code" em conjunto com a instalação do terminal Anaconda.
# Como jogar?
    1. O usuário, ao inicializar o código, será exibida a tela inícial do jogo da tela dele. Então, para avançar no mesmo, será necessário apertar a tecla 'espaço' do teclado;
    
    2.Passando-se da tela inicial, o usuário será dicrecionado para a tela de instruções, a qual irá mostrá-lo como mover-se horizontalmente, e como atirar, que são, por meio das setas do teclado, e da tecla 'espaço', respectivamente. Para sair dessa tela, o jogador deverá apertar a tecla espaço, também ;

    3. Assim, o usuário será direcionado ao jogo, no qual ele deverá executar os comandos apresentados na tela de instruções para jogar.

    4. Por fim, independente do estado em que ele queira encerrar o jogo, ele precisará apertar o 'x' , no topo da janela, para encerrá-lo. 

    5. Vídeo do jogo:
# Créditos 

    #Colaboradores: 
     1.Venâncio Freitas de Araújo Filho : 
     - Perfil no git hub:https://github.com/Venanciofaf
     - Perfil no Instagram : @venanciofreitass
    2. Wellington Rodrigues da Silva: 
    - Perfil no github: https://github.com/wellingtonrs07
    - Perfil no Instagram : @wellington07_
    3. João Victor de Almeida Braga: 
    - Perfil no github: @jvalmeidabraga
    - Perfil no Instagram : https://github.com/Joaovabbr
    
    #Referência que auxiliaram a criação do jogo: 
    [1] - https://dessoft.insper-comp.com.br/conteudo/projeto
    [2] - https://www.pixilart.com/draw
    [3] - https://freesound.org/




        





