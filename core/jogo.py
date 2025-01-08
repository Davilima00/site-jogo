from time import sleep
from random import randint
import json


def BlocoCheio():
    return '<div class="BlocoCheio"></div>'

def BlocoVazio():
    return '<div class="BlocoVazio"></div>'


ConteudoInicial = [
    {
        "caminho": [
            {"proxicao": 1, "bloco": BlocoCheio()},
            {"proxicao": 2, "bloco": BlocoCheio()}
        ]
    }
]

# caminho base/inicial
with open('data/jogo.json', 'w') as file:
    json.dump(ConteudoInicial, file, indent=4)  
    print("Conteúdo inicial gravado no arquivo.")


def GerarCaminho():
    BlocoAnterior = BlocoCheio() 
    Caminho = []
    
    while True:
        sleep(0.5)

        # Gera um novo bloco, evitando dois blocos vazios consecutivos
        if BlocoAnterior == BlocoVazio():
            NovoBloco = BlocoCheio()  
        else:
            NovoBloco = BlocoCheio() if randint(0, 1) == 0 else BlocoVazio()  

        Caminho.append(NovoBloco) 
        BlocoAnterior = NovoBloco  

        # Atualiza o arquivo JSON
        with open('data/jogo.json', 'r+') as file:
            dados = json.load(file)
            dados[0]["caminho"].append({"proxicao": len(dados[0]["caminho"]) + 1, "bloco": NovoBloco})

            # Move o ponteiro do arquivo para o início antes de escrever novamente
            file.seek(0)
            json.dump(dados, file, indent=4)
        
        print("Bloco adicionado.")

        if len(Caminho) >= 10:  
            break

    return Caminho




