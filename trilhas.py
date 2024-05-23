from historico import carrega


def __aprovado( materia ):
    return materia["status"] == "A" or materia["status"] == "AE"


def main():
    info = carrega("trilhas.json")
    total = dict()
    for key in info["trilhas"].keys():
        total[key] = [ 0 ] * len( info["trilhas"][key]["minimo"] )

    historico = carrega("historico.json")
    for materia in historico["materias"]:
        if __aprovado(materia):
            disciplina = materia["sigla"][:3]
            if disciplina in info["materias"]:
                codigo = materia["sigla"][3:]
                if codigo in info["materias"][disciplina]:
                    for key in info["materias"][disciplina][codigo].keys():
                        total[key][info["materias"][disciplina][codigo][key]] += 1

    print(total)


if __name__ == "__main__":
    main()