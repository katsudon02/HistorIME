import pymupdf
import json
import sys

# Coleção de funções com o objetivo de ler, formatar e salvar históricos escolares da USP,
# gerados pelo jupiterweb no formato .pdf e salvo em .json

def processa( nome_arquivo: str ) -> dict:
    """
    Esta função recebe o nome do arquivo do histórico e retorna um dicionário com as informações relevantes extraídas do pdf
 
    Parâmetros:
    nome_arquivo (str): O nome do arquivo do histórico escolar. O nome precisa ser um caminho válido até o arquivo.
 
    Retorna:
    dict: Informações relevantes contidas no histórico escolar
    """

    # Coleção das linhas tas tabelas do histórico
    doc = pymupdf.open( nome_arquivo )
    linhas = []
    for pagina in doc[1:]:
        for tabela in pagina.find_tables():
            for linha in tabela.extract():
                linhas.append(linha)

    historico = {
        'aluno':        linhas[3][1],
        'unidade':      linhas[2][1],
        'curso':        linhas[4][0].split('\n')[1].split(": ")[1],
        'ingresso':     linhas[4][0].split(": ")[1].split('\n')[0],
        'reingressos':  int(linhas[5][0].split(": ")[1]),
        'materias':     __filtra_materias(linhas)
    }
    return historico


def salva( historico: dict, nome_arquivo: str ):
    """
    Recebe um histórico escolar processado por processa() e o nome do arquivo de destino, e salva o dicionário em formato JSON.
 
    Parâmetros:
    historico (dict): Um dicionário gerado por processa(), que contém as informações do histórico.
    nome_arquivo (str): O nome do arquivo onde os dados serão salvos. O nome precisa ser um caminho válido.
    """

    with open( nome_arquivo, 'w' ) as arquivo:
        json.dump( historico, arquivo, indent = 4, ensure_ascii = False )


def carrega( nome_arquivo: str ) -> dict:
    """
    Recebe o nome de um arquivo JSON, gerado pela função salva(), e devolve os dados convertidos em um dicionário.
 
    Parâmetros:
    nome_arquivo (str): O nome do arquivo JSON, criado pela função salva().
 
    Retorna:
    dict: Dicionário contendo as informações do histórico processado.
    """

    with open( nome_arquivo, 'r' ) as file:
        dados = json.load( file )

    return dados

# Seleciona as linhas de uma lista que satisfazem as condições para serem 
# matérias e retorna o resultado
def __filtra_materias( linhas: list ):
    materias = []
    # Começa a filtragem a partir da 11ª linha, pois as anteriores são irrelevantes
    i = 11
    while ( not __eh_o_final(linhas[i]) ):
        if __eh_materia(linhas[i]):
            materias.append( __dicionariza(linhas[i]) )
        i += 1

    return materias

# Formata as linhas contidas em uma lista na forma de dicionário
def __dicionariza( linha: list ):
    return {
        'sigla':    linha[0],
        'au':       __intfy(linha[5]),
        'tr':       __intfy(linha[6]),
        'ch':       __intfy(linha[7]),
        'ce':       __intfy(linha[8]),
        'cp':       __intfy(linha[9]),
        'ext':      __intfy(linha[10]),
        'atpa':     __intfy(linha[11]),
        'freq':     __intfy(linha[12]),
        'nota':     __floatfy(linha[13]),
        'status':   __get_status(linha[13])
    }


# Verifica se a linha contém as informações de uma matéria
# O último elemento da linha precisa ser uma nota ou o status da matéria
def __eh_materia( linha: list ):
    return (linha[-1] != None) and ( ('A' <= linha[-1][-1] <= 'Z') or  ('0' <= linha[-1][-1] <= '9') )


# Verifica se a linha é o final das tabelas de matéria, tem uma frase que
# contém a palavra 'pretendidos' e é a última linha da tabela
def __eh_o_final( linha: list ):
    return ( "pretendidos" in linha[0] )

# Converte uma string para um número, se possível
# Exemplo:
# "5.7 A" -> 5.7 (float)
# ""      -> None
# "MA"    -> None
def __intfy( x: str ):
    x = x.split()
    try:
        return int( x[0] )
    except:
        return None
    
# Converte uma string para um número, se possível
# Exemplo:
# "5.7 A" -> 5.7 (float)
# ""      -> None
# "MA"    -> None
def __floatfy( x: str ):
    x = x.split()
    try:
        return float( x[0] )
    except:
        return None
    
# Retorna o status da matéria
# Exemplo:
# "5.2 A" -> "A"
# "MA"    -> "MA"
def __get_status( x: str ):
    x = x.split()
    return x[-1]


def main():
    if ( len(sys.argv) < 2 ):
        print("O nome do arquivo do histórico escolar é necessário")
        sys.exit()

    historico = processa(sys.argv[1])
    salva( historico, sys.argv[1].split('.')[0] + ".json" )
    print(type(carrega(sys.argv[1][:-3] + "json")))


if __name__ == "__main__":
    main()