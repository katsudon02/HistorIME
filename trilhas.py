import sys

from historico import carrega, processa

# Algumas variáveis auxiliares para formatação das cores do texto
VERDE = "\033[32m"
VERMELHO = "\033[31m"
AMARELO = "\033[93m"
RESET = "\033[0m"


# !!!!!!!!!!!!!! FALTA VERIFICAR SE A MATÉRIA É VÁLIDA !!!!!!!!!!!!!
def matches( keys: list, hist: dict ) -> list:
    found = []
    for key in keys:
        for materia in hist['materias']:
            if key == materia['sigla']:
                found.append(materia["sigla"])

    return found


# Matérias obrigatórias são uma categoria separada dos "blocos"
# >>>>> Começando com Teoria
# !!!!!!!!!!!!!!! FALTA VERIFICAR REPETIÇÕES !!!!!!!!!!!!!!!!!
def teoria( historico: dict, caminho: str ):
    # Pelo menos 7 matérias
    # Todas as obrigatórias de pelo menos dois blocos
    MIN_DISCIPLINAS = 7
    MIN_MODULOS = 2

    # 2 de Algoritmos, 3 de Matemática Discreta e 2 de Otimização
    QUANT_OBRIGATORIAS = ( 2, 3, 2 )

    # O JSON das disciplinas da trilha de Teoria da Computação
    disciplinas = carrega(caminho)

    # Obrigatórias
    completas = [ 0, 0, 0, 0 ]
    obrigatorias = matches( disciplinas["obrigatorias"].keys(), historico )
    for materia in obrigatorias:
        completas[ disciplinas["obrigatorias"][materia] ] += 1

    eq = 0
    for i in range( len(QUANT_OBRIGATORIAS) ):
        if QUANT_OBRIGATORIAS[i] == completas[i]:
            eq += 1

    if eq < MIN_MODULOS:
        print(f"{VERMELHO}Não cumpriu{RESET} os requisitos para completar a trilha de Teoria da Computação.")
        print("Causa: Não completou a quantidade mínima de obrigatórias da trilha")
        return
    
    # Optativas
    optativas = matches( disciplinas["optativas"].keys(), historico )
    for materia in optativas:
        completas[ disciplinas["optativas"][materia] ] += 1

    total = 0
    for i in range( len(QUANT_OBRIGATORIAS) ):
        total += completas[i]

    if total < MIN_DISCIPLINAS:
        print(f"{VERMELHO}Não cumpriu{RESET} os requisitos para completar a trilha de Teoria da Computação.")
        print("Causa: Não completou a quantidade mínima de disciplinas da trilha")
        return

    # O aluno completou a trilha!
    print(f"{VERDE}Cumpriu{RESET} os requisitos para completar a trilha de Teoria da Computação.")


# Inteligência Artificial
def ia( historico: dict, caminho: str ):
    # 3 de Introdução, 3 de Sistemas e 2 de Teoria
    QUANT = ( 3, 2, 1 )

    # O JSON das disciplinas da trilha de Inteligência Artificial
    disciplinas = carrega(caminho)

    completas = [ 0, 0, 0 ]
    # Obrigatória de IA
    obrigatoria = matches( disciplinas["obrigatorias"].keys(), historico )
    if len(obrigatoria) != 1:
        print(f"{VERMELHO}Não cumpriu{RESET} os requisitos para completar a trilha de Inteligência Artificial.")
        print("Causa: Não completou a disciplina obrigatória da trilha")
        return
    # Adiciona a obrigatória na contagem de disciplinas completas
    completas[ disciplinas["obrigatorias"][obrigatoria[0]] ] += 1

    # Optativas
    optativas = matches( disciplinas["optativas"].keys(), historico )
    for materia in optativas:
        completas[ disciplinas["optativas"][materia] ] += 1

    for i in range( len(QUANT) ):
        if completas[i] < QUANT[i]:
            print(f"{VERMELHO}Não cumpriu{RESET} os requisitos para completar a trilha de Inteligência Artificial.")
            print("Causa: Não completou a quantidade mínima de disciplinas dos blocos da trilha")
            return

    # O aluno completou a trilha!
    print(f"{VERDE}Cumpriu{RESET} os requisitos para completar a trilha de Inteligência Artificial.")


# Sistemas de Software
def sistemas( historico: dict, caminho: str ):
    # 2 de Desenvolvimento, 1 de Banco de Dados e 2 de Sistemas Paralelos e Distribuídos
    QUANT = ( 2, 1, 2 )

    # Quantidade mínima de disciplinas para completar a trilha
    MIN_DISCIPLINAS = 7

    # O JSON das disciplinas da trilha de Inteligência Artificial
    disciplinas = carrega(caminho)

    completas = [ 0, 0, 0 ]
    # Não há disciplinas obrigatórias
    # Optativas
    optativas = matches( disciplinas["optativas"].keys(), historico )
    for materia in optativas:
        completas[ disciplinas["optativas"][materia] ] += 1

    for i in range( len(QUANT) ):
        if completas[i] < QUANT[i]:
            print(f"{VERMELHO}Não cumpriu{RESET} os requisitos para completar a trilha de Sistemas de Software.")
            print("Causa: Não completou a quantidade mínima de disciplinas dos blocos da trilha")
            return
        
    total = 0
    for i in range( len(QUANT) ):
        total += completas[i]

    if total < MIN_DISCIPLINAS:
        print(f"{VERMELHO}Não cumpriu{RESET} os requisitos para completar a trilha de Sistemas de Software.")
        print("Causa: Não completou a quantidade total mínima de disciplinas da trilha")
        return


# Ciência de Dados
def ciencia( historico: dict, caminho: str ):
    # Pelo menos 7 matérias
    MIN_DISCIPLINAS = 7

    # 1 do Núcleo, Processamento de Sinais, Sistemas, Banco de Dados, Otimização, Probabilidade
    QUANT_OBRIGATORIAS = ( 1, 1, 1, 1, 1, 1 )

    # O JSON das disciplinas da trilha de Teoria da Computação
    disciplinas = carrega(caminho)

    # Obrigatórias
    completas = [ 0, 0, 0, 0, 0, 0, 0 ]
    obrigatorias = matches( disciplinas["obrigatorias"].keys(), historico )
    for materia in obrigatorias:
        completas[ disciplinas["obrigatorias"][materia] ] += 1

    total = 0
    for i in range( len(QUANT_OBRIGATORIAS) ):
        total += completas[i]
        if completas[i] < QUANT_OBRIGATORIAS[i]:
            print(f"{VERMELHO}Não cumpriu{RESET} os requisitos para completar a trilha de Ciência de Dados.")
            print("Causa: Não completou a quantidade mínima de obrigatórias da trilha")
            return
        
    # Optativas
    optativas = matches( disciplinas["optativas"].keys(), historico )
    for materia in optativas:
        completas[ disciplinas["optativas"][materia] ] += 1

    if total + completas[-1] < MIN_DISCIPLINAS:
        print(f"{VERMELHO}Não cumpriu{RESET} os requisitos para completar a trilha de Ciência de Dados.")
        print("Causa: Não completou a quantidade mínima de disciplinas da trilha")
        return
    
    # O aluno completou a trilha!
    print(f"{VERDE}Cumpriu{RESET} os requisitos para completar a trilha de Ciência de Dados.")


def __aprovado( materia ):
    return materia["status"] == "A" or materia["status"] == "AE"


def main():
    # info = carrega("trilhas.json")
    # total = dict()
    # for key in info["trilhas"].keys():
    #     total[key] = [ 0 ] * len( info["trilhas"][key]["minimo"] )

    historico = processa( sys.argv[1] )
    print(f"{AMARELO}NUSP - Aluno{RESET}: {historico["aluno"]}")
    print("------ Teoria da Computação ------")
    teoria( historico, "trilhas/teoria.json" )
    print("----- Inteligência Artificial ----")
    ia( historico, "trilhas/ia.json" )
    print("------ Sistemas de Software ------")
    sistemas( historico, "trilhas/sistemas.json" )
    print("------ Ciência de Dados ------")
    ciencia( historico, "trilhas/ciencia.json" )
    print()

    # found = matches(['MAC0121', 'MAE0119', 'MAC0323', 'MAC0459'], historico)
    # print(found)

    # for materia in historico["materias"]:
    #     if __aprovado(materia):
    #         disciplina = materia["sigla"][:3]
    #         if disciplina in info["materias"]:
    #             codigo = materia["sigla"][3:]
    #             if codigo in info["materias"][disciplina]:
    #                 for key in info["materias"][disciplina][codigo].keys():
    #                     total[key][info["materias"][disciplina][codigo][key]] += 1

    # print(total)


if __name__ == "__main__":
    main()