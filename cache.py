# Tópicos 1 e 2:

def inicializaCache(tam_cache):
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
    print("-" * 50)
    print("TAMANHO DA CACHE: ")
    for c in posicaoC:
        print(c)
    print("-" * 50)
    print("TAMANHO DA MEMÓRIA: ")
    for c in posicaoM:
        print(c)

# Tópico 4

def mapeamento_direto(pos_memoria):
    miss = 0
    hit = 0
    posicao = int(input("QUANTAS POSIÇÃO DA MEMÓRIA VOCÊ DESEJA ACESSAR: "))
    for c in range(posicao):
        valor = int(input("- QUAL VALOR NA MEMÓRIA VOCÊ DESEJA ACESSAR: "))
        pos_memoria.append(valor)
    for item in pos_memoria:
        if item in posicaoM:
            print(f"{item}: HIT")
            hit += 1
        else:
            posicao_cache = item % tam_cache
            print(f"{item}: MISS")
            miss += 1
            posicaoM[posicao_cache] = item

    taxa_acertos = (hit/posicao) * 100
    imprimirCache()
    print("-" * 50)
    print("- MEMÓRIAS ACESSADAS: ", posicao)
    print("- Número de HITS: ", hit)
    print("- Número de MISS: ", miss)
    print("- TAXA DE ACERTOS: %.2f%%" % taxa_acertos)



tam_cache = int(input("- Digite o tamanho da memória cache: "))

pos_memoria = []
posicaoM = []
posicaoC = []

inicializaCache(tam_cache)

mapeamento_direto(pos_memoria)
