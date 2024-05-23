# HistorIME - O processador de históricos e verificador de trilhas

## Descrição
Este projeto é a versão em python do [verificador de trilhas](https://github.com/Renatata-H/checagem_de_trilha_BCC_IME_USP) desenvolvido por @Renatata-H, com
a separação do processo em duas partes e a adição de algumas funções. O projeto é composto por 
dois principais componentes:
* Processador de históricos escolares;
* Verificador de trilhas do BCC completas.

## O processador de históricos escolares
O arquivo pdf do histórico, gerado pelo site jupiterweb, é usado como entrada e as principais
informações são extraídas no formato de dicionário em python, sendo possível salvar no formato
JSON de arquivo.

## O verificador de trilhas do BCC
A partir do histórico escolar processado, verifica se o aluno foi aprovado nas matérias necessárias
para completar alguma trilha do Bacharelado de Ciência da Computação do Instituto de Matemática e
Estatística da USP.

## Como executar

### Processador de históricos
A partir do diretório onde o arquivo "historico.py" se encontra, execute:
```
python historico.py documento.pdf
```
O arquivo "documento.pdf" é o nome do arquivo em pdf do histórico escolar
a ser processado. Por exemplo, se o seu arquivo se chamar "historico.pdf"
(o que provavelmente é o caso, pois por automático o jupiterweb gera um
arquivo com esse nome) então o comando a ser executado é:
```
python historico.py historico.pdf
```
Após a execução, no mesmo diretório terá um novo arquivo com o mesmo nome
do pdf, mas com a extensão .json, que contém as informações do aluno e as
matérias cursadas até o momento.

### Verificador de trilhas do BCC
*** PENDENTE ***

## Dependências
- Python, versão 3.12.3 ou superior
- PyMuPDF, versão 1.24.4 ou superior

## Informações adicionais
Segue as informações da máquina onde o projeto foi desenvolvido e testado:
- Sistema operacional: Fedora Linux 40 (KDE Plasma);
- Arquitetura: x86_64;
- Processador: 4 × Intel® Core™ i7-5500U CPU @ 2.40GHz;
- Memória RAM: 15.5 GiB.
