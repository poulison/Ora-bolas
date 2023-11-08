#Paulo Gabriel Gonçalves Leme R.A:24.123.075-4
#Paulo Andre de Oliveira Hirata R.A:24.123.086-1
#Marjorie Luize Martins Costa R.A:24.123.084-5


from math import *
import matplotlib.pyplot as plt

def calcular_distancia(x1, y1, x2, y2):
    return sqrt((x2 - x1)**2 + (y2 - y1)**2)

def calcular_tempo(distancia, velocidade):
    return distancia / velocidade

def encontrar_posicao_mais_perto(robo_y, lista_Y):
    posicao_y = None
    for posicao_mais_perto_y in lista_Y:
        if posicao_mais_perto_y < robo_y:
            posicao_y = posicao_mais_perto_y/2
    return posicao_y

def ler_arquivo(lista_X,lista_T,lista_Y):
    with open('trajetoria_bola.txt', 'r') as arquivo:
        linhas = arquivo.readlines()
        for linha in linhas[1:]:
            colunas = linha.strip().split()
            lista_T.append(float(colunas[0].replace(',', '.')))
            lista_X.append(float(colunas[1].replace(',', '.')))
            lista_Y.append(float(colunas[2].replace(',', '.')))
    return lista_T, lista_X, lista_Y

def calcular_forca(massa, aceleracao):
    forca = massa * aceleracao
    return round(forca, 3)

def calcular_forca_atrito_cinetico(peso):
    forca_atrito_cinetico = 0.5 * peso
    return round(forca_atrito_cinetico, 3)

def calcular_graficos(robo_x, robo_y, posicao_x, posicao_y, tempo_robo_cheguei,
                      distancia_inicial_robo, distancia_robo_e_bola,
                      distancia_bola_inicial, distancia_bola_final,
                      velocidade_inicial_bola, velocidade_final_bola,
                      aceleracao_inicial_bola, aceleracao_final_bola):
    # Cálculo da distância da origem da bola até a interceptação
    distancia_bola = calcular_distancia(posicao_x, posicao_y, 1.000, 0.500)

    # Cálculo da distância inicial da bola
    distancia_bola_inicial = calcular_distancia(1.010, 0.508, 1.000, 0.500)

    # Cálculo da distância final da bola
    distancia_bola_final = calcular_distancia(9.000, 5.300, 1.000, 0.500)

    # Cálculo da distância inicial do robô
    distancia_inicial_robo = calcular_distancia(0, 0, robo_x, robo_y)

    # Cálculo da velocidade média inicial da bola
    velocidade_inicial_bola = distancia_bola_inicial / 0.02

    # Cálculo da velocidade média final da bola
    velocidade_final_bola = (distancia_bola_final / 0.02)/2

    # Cálculo da aceleração média inicial da bola
    aceleracao_inicial_bola = velocidade_inicial_bola / 0.02

    # Cálculo da aceleração média final da bola
    aceleracao_final_bola = velocidade_final_bola / 0.02

    return (distancia_bola, distancia_bola_inicial, distancia_bola_final,
            distancia_inicial_robo, velocidade_inicial_bola, velocidade_final_bola,
            aceleracao_inicial_bola, aceleracao_final_bola)

def calcular_tudo(robo_x, robo_y):
    lista_Y = []
    lista_X = []
    lista_T = []
    ler_arquivo(lista_X,lista_T,lista_Y)

    posicao_y = encontrar_posicao_mais_perto(robo_y, lista_Y)
    print(f"Posição da bola mais perto do robô: {posicao_y:.3f} cm")

    robo_velocidade = 2.8  # m/s
    aceleracao = 2.8  # m/s²
    peso = 4.6  # N
    massa = 0.46  #

    distancia_robo_e_bola = calcular_distancia(robo_x, robo_y, 1.000, posicao_y)
    tempo_robo_cheguei = calcular_tempo(distancia_robo_e_bola, robo_velocidade)

    forca = calcular_forca(massa, aceleracao)
    forca_atrito_cinetico = calcular_forca_atrito_cinetico(peso)

    resultados = calcular_graficos(robo_x, robo_y, 1.000, posicao_y, tempo_robo_cheguei,
                                   0, distancia_robo_e_bola,
                                   0, 0,
                                   0, 0,
                                   0, 0)
    (distancia_bola, distancia_bola_inicial, distancia_bola_final,
     distancia_inicial_robo, velocidade_inicial_bola, velocidade_final_bola,
     aceleracao_inicial_bola, aceleracao_final_bola) = resultados

    print(f"Distância da origem da bola até a interceptação: {distancia_bola:.3f} cm")
    print(f"Distância inicial da bola: {distancia_bola_inicial:.3f} cm")
    print(f"Distância final da bola: {distancia_bola_final:.3f} cm")
    print(f"Distância inicial do robô: {distancia_inicial_robo:.3f} cm")
    print(f"Velocidade média inicial da bola: {velocidade_inicial_bola:.3f} m/s")
    print(f"Velocidade média final da bola: {velocidade_final_bola/10:.3f} m/s")
    print(f"Aceleração média inicial da bola: {aceleracao_inicial_bola/10:.3f} m/s²")
    print(f"Aceleração média final da bola: {aceleracao_final_bola/10000:.3f} m/s²")

    # Cálculos adicionais para os gráficos
    tempo = lista_T
    posicao_bola_x = lista_X
    posicao_bola_y = lista_Y

    # Gráfico das trajetórias da bola e do robô em um plano 𝑥𝑦, até o ponto de interceptação
    plt.figure(figsize=(8, 6))
    plt.plot(posicao_bola_x, posicao_bola_y, label="Trajetória da Bola")
    plt.plot([0, robo_x], [0, robo_y], label="Trajetória do Robô")
    plt.xlabel("Posição X (cm)")
    plt.ylabel("Posição Y (cm)")
    plt.title("Trajetórias da Bola e do Robô")
    plt.legend()
    plt.grid(True)

    # Gráfico das coordenadas 𝑥 e 𝑦 da posição da bola e do robô em função do tempo 𝑡 até o instante de interceptação
    plt.figure(figsize=(8, 6))
    plt.plot(tempo, posicao_bola_x, label="Posição X da Bola")
    plt.plot(tempo, posicao_bola_y, label="Posição Y da Bola")
    plt.plot(tempo_robo_cheguei, robo_x, 'ro', label="Posição X do Robô")
    plt.plot(tempo_robo_cheguei, robo_y, 'bo', label="Posição Y do Robô")
    plt.xlabel("Tempo (s)")
    plt.ylabel("Posição (cm)")
    plt.title("Posição da Bola e do Robô em Função do Tempo")
    plt.legend()
    plt.grid(True)

    # Gráfico dos componentes 𝑣𝑥 e 𝑣𝑦 da velocidade da bola e do robô em função do tempo 𝑡 até o instante de interceptação
    velocidade_bola_x = [((posicao_bola_x[i+1] - posicao_bola_x[i]) / (tempo[i+1] - tempo[i])) for i in range(len(tempo)-1)]
    velocidade_bola_y = [((posicao_bola_y[i+1] - posicao_bola_y[i]) / (tempo[i+1] - tempo[i])) for i in range(len(tempo)-1)]
    tempo_velocidade = [(tempo[i+1] + tempo[i]) / 2 for i in range(len(tempo)-1)]

    plt.figure(figsize=(8, 6))
    plt.plot(tempo_velocidade, velocidade_bola_x, label="Velocidade X da Bola")
    plt.plot(tempo_velocidade, velocidade_bola_y, label="Velocidade Y da Bola")
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.xlabel("Tempo (s)")
    plt.ylabel("Velocidade (m/s)")
    plt.title("Componentes da Velocidade da Bola em Função do Tempo")
    plt.legend()
    plt.grid(True)

    # Gráfico dos componentes 𝑎𝑥 e 𝑎𝑦 da aceleração da bola e do robô em função do tempo 𝑡 até o instante de interceptação
    aceleracao_bola_x = [((velocidade_bola_x[i+1] - velocidade_bola_x[i]) / (tempo[i+1] - tempo[i])) for i in range(len(tempo)-2)]
    aceleracao_bola_y = [((velocidade_bola_y[i+1] - velocidade_bola_y[i]) / (tempo[i+1] - tempo[i])) for i in range(len(tempo)-2)]
    tempo_aceleracao = [(tempo[i+1] + tempo[i]) / 2 for i in range(len(tempo)-2)]

    def calcular_posicao_x(t):
        return 0.005*t**3 + 1E-13*t**2 + 0.5*t + 1

    def calcular_posicao_y(t):
        return -0.02*t**2 + 0.9*t + 0.5

    def calcular_velocidade_x(t):
        return 0.015*t**2 - 0.0003*t + 0.5

    def calcular_velocidade_y(t):
        return -0.04*t + 0.9004

    def calcular_aceleracao_x(t):
        return 0.03*t - 0.0006

    def calcular_aceleracao_y(t):
        return -0.04

    tempo_grafico = [i/100 for i in range(0, int(tempo_robo_cheguei*100))]

    # Adicionando os gráficos solicitados
    plt.figure(figsize=(8, 6))
    plt.plot(tempo_grafico, [calcular_posicao_x(t) for t in tempo_grafico], label="Posição X da Bola (Calculada)")
    plt.plot(tempo_grafico, [calcular_posicao_y(t) for t in tempo_grafico], label="Posição Y da Bola (Calculada)")
    plt.xlabel("Tempo (s)")
    plt.ylabel("Posição (cm)")
    plt.title("Posição da Bola em Função do Tempo")
    plt.legend()
    plt.grid(True)


    plt.figure(figsize=(8, 6))
    plt.plot(tempo_aceleracao, aceleracao_bola_x, label="Aceleração X da Bola")
    plt.plot(tempo_aceleracao, aceleracao_bola_y, label="Aceleração Y da Bola")
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.xlabel("Tempo (s)")
    plt.ylabel("Aceleração (m/s²)")
    plt.title("Componentes da Aceleração da Bola em Função do Tempo")
    plt.legend()
    plt.grid(True)

    # Gráfico da distância relativa 𝑑 entre o robô e a bola como função do tempo 𝑡 até o instante de interceptação
    distancia_relativa = [calcular_distancia(robo_x, robo_y, posicao_bola_x[i], posicao_bola_y[i]) for i in range(len(tempo)-1)]

    plt.figure(figsize=(8, 6))
    plt.plot(tempo_velocidade, distancia_relativa, label="Distância Relativa")
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.xlabel("Tempo (s)")
    plt.ylabel("Distância Relativa (cm)")
    plt.title("Distância Relativa entre o Robô e a Bola em Função do Tempo")
    plt.legend()
    plt.grid(True)

    plt.show()

def obter_posicoes_do_robo():
    robo_x = float(input("Digite a posição do robô em X: "))
    robo_y = float(input("Digite a posição do robô em Y: "))
    return robo_x, robo_y

def main():
    robo_x = float(input("Posição do robô em X (cm): "))
    robo_y = float(input("Posição do robô em Y (cm): "))

    calcular_tudo(robo_x, robo_y)

if __name__ == "__main__":
    main()
