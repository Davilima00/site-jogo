from random import randint
import json

def BlocoCheio():
    return '<div class="BlocoCheio"></div>'

def BlocoVazio():
    return '<div class="BlocoVazio"></div>'




def EnviarCaminho():
    blocos = []

    with open('data/jogo.json', 'r', encoding='utf-8') as arquivo:
        dados = json.load(arquivo)

    for item in dados:
        caminho = item.get("caminho", [])
        
        # Itera sobre os itens dentro de 'caminho'
        for bloco in caminho:
            html = bloco.get("bloco", "")
            blocos.append(html)

    conteudo = " ".join(blocos)
    print(conteudo)
    return conteudo

def InicializarCaminho():
    ConteudoInicial = [
        {
            "caminho": [
                {"proxicao": 1, "bloco": BlocoCheio()},
                {"proxicao": 2, "bloco": BlocoCheio()}
            ]
        }
    ]

    with open('data/jogo.json', 'w') as file:
        json.dump(ConteudoInicial, file, indent=4)  

    conteudo = EnviarCaminho()
    print("Conteúdo inicial gravado no arquivo.")
    return conteudo
    
def GerarBloco():
    try:
        # Abrir o arquivo em modo leitura e escrita
        with open('data/jogo.json', 'r+') as file:
            try:
                dados = json.load(file)
            except json.JSONDecodeError:
                # Inicializa o JSON se estiver vazio ou malformado
                dados = [{"caminho": []}]

            # Verifica se existem blocos no caminho
            if dados[0]["caminho"]:
                ultimo_bloco = dados[0]["caminho"][-1]["bloco"]
            else:
                ultimo_bloco = None

            # Determina o novo bloco a ser gerado
            if ultimo_bloco == '<div class="BlocoVazio"></div>':
                NovoBloco = '<div class="BlocoCheio"></div>'  # Evita dois vazios consecutivos
            else:
                NovoBloco = '<div class="BlocoCheio"></div>' if randint(0, 1) == 0 else '<div class="BlocoVazio"></div>'

            # Adiciona o novo bloco ao caminho
            novo_bloco_dados = {
                "proxicao": len(dados[0]["caminho"]) + 1,
                "bloco": NovoBloco
            }
            dados[0]["caminho"].append(novo_bloco_dados)

            # Move o ponteiro para o início e atualiza o arquivo
            file.seek(0)
            json.dump(dados, file, indent=4)
            file.truncate()  # Remove dados antigos após a escrita
    except FileNotFoundError:
        # Cria o arquivo se ele não existir
        with open('data/jogo.json', 'w') as file:
            dados = [{"caminho": []}]
            json.dump(dados, file, indent=4)
        print("Arquivo 'jogo.json' criado.")

def GerarBlocos():
    try:
        # Gera dois blocos consecutivos
        GerarBloco()
        GerarBloco()

        # Retorna o caminho atualizado em formato HTML
        return EnviarCaminho()
    except Exception as e:
        print(f"Erro na função 'GerarBlocos': {e}")
        raise



