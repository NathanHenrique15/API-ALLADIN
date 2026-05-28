from fastapi import FastAPI # API
import requests # buscas

app = FastAPI()

@app.get("/consultar")
def buscar_precos(data_atual: str):

    url = "https://testedefensoriapr.pythonanywhere.com/precos"
    
    try:
        # A lógica de buscar os dados (Passo 5) entra aqui
        resposta = requests.get(url, timeout=10)
        resposta.raise_for_status() 
        dados_da_loja = resposta.json()
        
        # O retorno dos dados com a data (Requisito do desafio) [1]
        return {
            "data_da_consulta": data_atual,
            "precos_recebidos": dados_da_loja
        }
        
    except Exception:
        # O tratamento de erro obrigatório (Requisito do desafio) [2]
        return {"erro": "Desculpe, o serviço de preços está indisponível."}