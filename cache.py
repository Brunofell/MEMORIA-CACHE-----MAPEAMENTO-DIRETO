# Tópicos 1 e 2:

def inicializaCache(tam_cache):
    posicaoM = []
    posicaoC = []
    c = 0
    for cont in range(tam_cache):
        posicaoM.append(-1)
        posicaoC.append(c)
        c += 1
    for c in posicaoC:
        print(c)
    print("-" * 50)
    print("TAMANHO DA MEMÓRIA: ")
    for c in posicaoM:
        print(c)


# Tópico 3

def imprimirCache():
    print("TAMANHO DA CACHE: ", tam_cache)
    inicializaCache(tam_cache)


# Tópico 4

def mapeamento_direto(tam_cache, pos_memoria):
    posicao = int(input("QUANTAS POSIÇÃO DA MEMÓRIA VOCÊ DESEJA ACESSAR: "))
    for c in range(posicao):
        valor = int(input("- QUAL POSIÇÃO NA MEMÓRIA VOCÊ DESEJA ACESSAR: "))
        pos_memoria.append(valor)
    print(pos_memoria)
    print(tam_cache)


tam_cache = int(input("- Digite o tamanho da memória cache: "))

imprimirCache()

pos_memoria = []

mapeamento_direto(tam_cache, pos_memoria)

