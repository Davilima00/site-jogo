from fastapi import FastAPI, Request # type: ignore
from fastapi.responses import HTMLResponse # type: ignore
from fastapi.templating import Jinja2Templates # type: ignore
from fastapi.staticfiles import StaticFiles # type: ignore

from core.jogo import InicializarCaminho, GerarBlocos, EnviarCaminho
 

app = FastAPI()
  
app.mount("/static", StaticFiles(directory="static"), name="static")

app.mount("/static/styles/index.css", StaticFiles(directory="static"), name="static")
app.mount("/static/styles/jogo.css", StaticFiles(directory="static"), name="static")
app.mount("/static/src/entrada.js", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")


# pagina de entrada do jogo 
@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "message": "Bem-vindo ao FastAPI!"})

ProxicaoJogador = 0

# pagina do jogo
@app.get("/jogo", response_class=HTMLResponse)
async def AddBlock(request: Request):

    CaminhoHtml = InicializarCaminho()

    return templates.TemplateResponse("jogo.html", {
        "request": request, 
        "message": "Bem-vindo ao FastAPI!", 
        "Caminho": CaminhoHtml
    })

@app.post("/onclick")
async def Pulo(request: Request):
    global ProxicaoJogador
    try:
        # Incrementa a posição do jogador
        ProxicaoJogador += 1

        # Obtém os dados enviados pelo frontend
        data = await request.json()
        print("Proxição do jogador atualizada:", ProxicaoJogador)
        print("Dados recebidos:", data)

        # Gera novos blocos
        caminho_html = GerarBlocos()
        print("Caminho gerado com sucesso:", caminho_html)

        # Retorna o resultado ao frontend
        return {
            "message": "onclick clicado com sucesso!",
            "prosicao": ProxicaoJogador,
            "caminho": caminho_html
        }
    except Exception as e:
        # Captura o erro e exibe no console
        print(f"Erro no endpoint '/onclick': {e}")
        return { "error": "Erro interno no servidor" }, 500




@app.post("/doubleclick")
async def doubleclick(request: Request, data: dict):
    global ProxicaoJogador
    ProxicaoJogador += 2

    print(ProxicaoJogador)
    print("doubleclick clicado! Dados recebidos:", data)
    return {"message": "doubleclick clicado com sucesso!", "prosicao": ProxicaoJogador, "caminho": GerarBlocos()}


@app.get("/renderizar", response_class=HTMLResponse)
async def atualizar(request: Request):

    CaminhoHtml = EnviarCaminho()

    return templates.TemplateResponse("jogo.html", {
        "request": request, 
        "message": "Bem-vindo ao FastAPI!", 
        "Caminho": CaminhoHtml
    })


