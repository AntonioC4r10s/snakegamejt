import pygame
from pygame.locals import *
from sys import exit
from random import randint


# Iniciar o pygame
pygame.init()

# Definindo altura e largura da janela
LARGURA = 640
ALTURA = 480

# Criando janela e suas proriedades
janela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption('Snake JT')

# Cores
# Cor de fundo da janela
COR_DE_FUNDO = (135,206,235)
COR_SCORE = (0,0,0)

# Fontes
fonte1 = pygame.font.SysFont('gabriola', 35, True, True)

# Constantes
FPS = 10
VELOCIDADE = 10

# Variaveis
pontos = 0
x_controle = VELOCIDADE
y_controle = 0
relogio = pygame.time.Clock()
lista_cobra = []
comprimento_inicial = 5

# Propriedades da Cobra
LARGURA_COBRA = 30
ALTURA_COBRA = 30
COR__COBRA = (0,100,0)
COR__CORPO = (0, 255, 0)
x_cobra = LARGURA/2
y_cobra = ALTURA/2

# Propriedades da Maçã
LARGURA_MACA = 25
ALTURA_MACA = 25
COR__MACA = (200,0,0)
X_MACA_INICIAL = randint(LARGURA_MACA, LARGURA - LARGURA_MACA)
Y_MACA_INICIAL = randint(ALTURA_MACA, ALTURA-ALTURA_MACA)


# Funções
def aumenta_cobra(lista_cobra):
    for XeY in lista_cobra:
        # XeY = [x, y]
        # XeY[0] = x
        # XeY[1] = y

        pygame.draw.rect(janela, COR__CORPO, (XeY[0], XeY[1], LARGURA_COBRA - 5, ALTURA_COBRA - 5))

def reiniciar_jogo():
    global pontos, comprimento_inicial, x_cobra, y_cobra, lista_cobra, lista_cabeca, x_maca, y_maca, morreu
    pontos = 0
    comprimento_inicial = 5
    x_cobra = int(LARGURA/2) 
    y_cobra = int(ALTURA/2)
    lista_cobra = []
    lista_cabeca = []
    X_MACA_INICIAL = randint(LARGURA_MACA, LARGURA - LARGURA_MACA)
    Y_MACA_INICIAL = randint(ALTURA_MACA, ALTURA-ALTURA_MACA)
    morreu = False

# Loop principal
while True:
    
    # FPS
    relogio.tick(FPS)

    # Cor de fundo(BG)
    janela.fill(COR_DE_FUNDO)

    # Score
    score = f'Pontos: {pontos}'
    score_formated = fonte1.render(score, True, COR_SCORE)


    # Cobra
    cobra = pygame.draw.rect(janela, COR__COBRA, (x_cobra, y_cobra, LARGURA_COBRA, ALTURA_COBRA))

    # Maçã
    maca = pygame.draw.rect(janela, COR__MACA, (X_MACA_INICIAL, Y_MACA_INICIAL, LARGURA_MACA, ALTURA_MACA))


    # Loop de eventos dentro do loop principal
    for event in pygame.event.get():
        
        # Fechar game ao sair
        if event.type == QUIT:
            pygame.quit()
            exit()
        
        # Capturando teclas 
        if event.type == KEYDOWN:
            
            if event.key == K_a:
                if x_controle == VELOCIDADE:
                    pass
                else:
                    x_controle = -VELOCIDADE
                    y_controle = 0

            if event.key == K_w:
                if y_controle == VELOCIDADE:
                    pass
                else:
                    x_controle = 0
                    y_controle = -VELOCIDADE
            
            if event.key == K_s:
                if y_controle == -VELOCIDADE:
                    pass
                else:
                    x_controle = 0
                    y_controle = VELOCIDADE
            
            if event.key == K_d:
                if x_controle == -VELOCIDADE:
                    pass
                else:
                    x_controle = VELOCIDADE
                    y_controle = 0
            

    # Movimento da cobra
    x_cobra = x_cobra + x_controle
    y_cobra = y_cobra + y_controle

    # Fazendo a cobra estar sempre dentro da janela
    if x_cobra >= LARGURA:
        x_cobra = 0
    if x_cobra < 0:
        x_cobra = LARGURA
    if y_cobra >= ALTURA:
        y_cobra = 0
    if y_cobra < 0:
        y_cobra = ALTURA

    # Colisão com da cobra com a maçã
    if cobra.colliderect(maca):
        X_MACA_INICIAL = randint(LARGURA_MACA, LARGURA - LARGURA_MACA)
        Y_MACA_INICIAL = randint(ALTURA_MACA, ALTURA-ALTURA_MACA)
        pontos += 1
        comprimento_inicial += 1
        FPS += 2

    # Lista com o valor das coordenadas da cabeça da cobra e lista para o corpo
    lista_cabeca = []
    lista_cabeca.append(x_cobra)
    lista_cabeca.append(y_cobra)

    lista_cobra.append(lista_cabeca)

    if len(lista_cobra) > comprimento_inicial:
        del lista_cobra[0]

    aumenta_cobra(lista_cobra)

    # Ao se colidir consigo mesma
    if lista_cobra.count(lista_cabeca) > 1:
        fonte2 = pygame.font.SysFont('arial', 20, True, True)
        mensagem = 'Game over! Pressione a tecla R para jogar novamente'
        texto_formatado = fonte2.render(mensagem, True, (0,0,0))
        ret_texto = texto_formatado.get_rect()

        morreu = True
        while morreu:
            janela.fill((255,255,255))
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                if event.type == KEYDOWN:
                    if event.key == K_r:
                        reiniciar_jogo()

            ret_texto.center = (LARGURA//2, ALTURA//2) 
            janela.blit(texto_formatado, ret_texto)
            pygame.display.update()

    # Mostrar Score
    janela.blit(score_formated, (430, 35))

    # Atualizar janela
    pygame.display.update()