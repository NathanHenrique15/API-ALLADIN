from fastapi import FastAPI, HTTPException
import httpx
from datetime import datetime

app = FastAPI()

URL_PRECOS = "https://testedefensoriapr.pythonanywhere.com/precos"


@app.get("/consultar")
async def buscar_precos():

    data_atual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    try:
        async with httpx.AsyncClient(timeout=10) as client:
            resposta = await client.get(URL_PRECOS)
            resposta.raise_for_status()
            dados_da_loja = resposta.json()

        return {
            "data_da_consulta": data_atual,
            "precos_recebidos": dados_da_loja
        }

    except httpx.RequestError:
        raise HTTPException(
            status_code=503,
            detail="Serviço de preços indisponível."
        )

    except httpx.HTTPStatusError:
        raise HTTPException(
            status_code=502,
            detail="Erro ao acessar o serviço externo."
        )