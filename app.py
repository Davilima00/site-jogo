from fastapi import FastAPI, Request # type: ignore
from fastapi.responses import HTMLResponse # type: ignore
from fastapi.templating import Jinja2Templates # type: ignore
from fastapi.staticfiles import StaticFiles # type: ignore

from core.jogo import BlocoCheio, BlocoVazio, GerarCaminho



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


# pagina do jogo
@app.get("/jogo", response_class=HTMLResponse)
async def read_root(request: Request):

    CaminhoHtml = GerarCaminho()

    return templates.TemplateResponse("jogo.html", {
        "request": request, 
        "message": "Bem-vindo ao FastAPI!", 
        "Caminho": CaminhoHtml


    })


prosicao = 0

@app.post("/onclick")
async def onclick(data: dict):
    global prosicao
    prosicao += 1

    print(prosicao)
    print("onclick clicado! Dados recebidos:", data)
    return {"message": "onclick clicado com sucesso!", "prosicao": prosicao}

@app.post("/doubleclick")
async def doubleclick(data: dict):
    global prosicao
    prosicao += 2

    print(prosicao)
    print("doubleclick clicado! Dados recebidos:", data)
    return {"message": "doubleclick clicado com sucesso!", "prosicao": prosicao}

