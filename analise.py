import os
import re
from urllib.error import HTTPError, URLError

from ollama_cliente import consultar_ollama
from prompt import montar_mensagem

MENSAGEM_SEM_CONFIGURACAO = "Defina as variáveis OLLAMA_URL e OLLAMA_MODELO (veja o .env.example)."
AVISO_TRECHO = "[Não foi possível verificar no enunciado]"
AVISO_SEM_TRECHOS = (
    "Aviso: o modelo não trouxe trechos de apoio. Nada abaixo foi verificado "
    "no enunciado; confira cada item no texto original.\n\n"
)

# O rótulo "Trecho de apoio:" em qualquer posição da linha, com o texto que o
# segue até o próximo rótulo ou o fim da linha.
APOIO = re.compile(
    r"(trechos?\s+de\s+apoio\s*:)(.*?)(?=trechos?\s+de\s+apoio\s*:|$)",
    re.IGNORECASE | re.MULTILINE,
)
CITACAO_RETA = re.compile(r'"([^"]+)"')
CITACAO_CURVA = re.compile(r"“([^”]+)”")


def normalizar(texto: str) -> str:
    """Troca qualquer sequência de espaços ou quebras de linha por um espaço."""
    return " ".join(texto.split())


def verificar_trechos_de_apoio(enunciado: str, resposta: str) -> str:
    """Troca por um aviso cada citação que não aparece literalmente no enunciado.

    Conferem-se as citações em aspas curvas em qualquer parte da resposta e,
    depois do rótulo "Trecho de apoio:", também as aspas retas e o texto sem aspas.
    """
    base = normalizar(enunciado)

    def presente(trecho: str) -> bool:
        return normalizar(trecho) in base

    def conferir_apoio(apoio: re.Match[str]) -> str:
        rotulo, resto = apoio.groups()
        if "“" in resto or not resto.strip():
            return apoio.group(0)  # aspas curvas: conferidas na etapa seguinte
        if '"' in resto:
            resto = CITACAO_RETA.sub(
                lambda c: c.group(0) if presente(c.group(1)) else AVISO_TRECHO, resto
            )
        elif not presente(resto):
            final = resto[len(resto.rstrip()):]  # separa do próximo rótulo
            resto = " " + AVISO_TRECHO + final
        return rotulo + resto

    def conferir_curva(citacao: re.Match[str]) -> str:
        return citacao.group(0) if presente(citacao.group(1)) else AVISO_TRECHO

    resposta = APOIO.sub(conferir_apoio, resposta)
    return CITACAO_CURVA.sub(conferir_curva, resposta)


def contar_trechos_de_apoio(resposta: str) -> int:
    """Quantas vezes a resposta usa o rótulo "Trecho de apoio:"."""
    return len(APOIO.findall(resposta))


def analisar_enunciado(texto: str) -> tuple[str | None, str | None]:
    """Consulta o modelo e devolve (checklist verificado, None) ou (None, mensagem de erro)."""
    endereco = os.getenv("OLLAMA_URL")
    modelo = os.getenv("OLLAMA_MODELO")
    if not endereco or not modelo:
        return None, MENSAGEM_SEM_CONFIGURACAO

    try:
        resposta = consultar_ollama(endereco, modelo, montar_mensagem(texto))
    except HTTPError as erro:
        return None, f"O Ollama devolveu o erro HTTP {erro.code}."
    except URLError as erro:
        return None, f"Falha na conexão com o Ollama: {erro.reason}"
    except TimeoutError:
        return None, "O Ollama não respondeu dentro do tempo de espera."
    except ValueError as erro:
        return None, f"Falha ao ler a resposta do Ollama: {erro}"

    checklist = verificar_trechos_de_apoio(texto, resposta)
    if contar_trechos_de_apoio(resposta) == 0:
        checklist = AVISO_SEM_TRECHOS + checklist
    return checklist, None
