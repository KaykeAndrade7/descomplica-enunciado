import json
import os
import ssl
from urllib.request import Request, urlopen


def consultar_ollama(endereco: str, modelo: str, texto: str) -> str:
    """Envia uma mensagem ao Ollama e devolve o texto da resposta."""
    pedido = {
        "model": modelo,
        "messages": [{"role": "user", "content": texto}],
        "think": False,
        "stream": False,
    }
    requisicao = Request(
        f"{endereco.rstrip('/')}/api/chat",
        data=json.dumps(pedido).encode("utf-8"),
        headers={"Content-Type": "application/json"},
        method="POST",
    )

    contexto = ssl.create_default_context()
    if os.getenv("OLLAMA_TESTE_SEM_VERIFICACAO_TLS") == "1":
        contexto.check_hostname = False
        contexto.verify_mode = ssl.CERT_NONE

    with urlopen(requisicao, timeout=120, context=contexto) as resposta:
        dados = json.load(resposta)

    try:
        mensagem = dados["message"]
        conteudo = mensagem["content"]
    except (KeyError, TypeError) as erro:
        raise ValueError("O Ollama devolveu uma resposta em formato inesperado.") from erro

    if not isinstance(conteudo, str) or not conteudo.strip():
        motivo = dados.get("done_reason")
        if motivo not in ("stop", "length", "load"):
            motivo = "ausente ou não reconhecido"
        tokens = dados.get("eval_count")
        if type(tokens) is not int or tokens < 0:
            tokens = "não informado"
        outros_campos = sum(
            isinstance(valor, str) and bool(valor.strip())
            for chave, valor in mensagem.items()
            if chave not in ("role", "content")
        )
        raise ValueError(
            "O Ollama devolveu uma resposta sem texto.\n"
            f"Motivo de término (done_reason): {motivo}\n"
            f"Tokens gerados (eval_count): {tokens}\n"
            f"Outros campos de mensagem com texto: {outros_campos}"
        )

    return conteudo
