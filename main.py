import time
from colorama import init # type: ignore
from core.rpg import intro_message, robo_intro, robos, status_jogador
from core.jogador import perguntar_nome
import json
 

with open('data/jogador.json', 'r') as file:
    dados = json.load(file)

if dados["nome"] == "":
    perguntar_nome()


init(autoreset=True)

intro_message()
robo_intro(robos[0])

status_jogador()






