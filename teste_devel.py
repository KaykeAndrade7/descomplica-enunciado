import json
from html import escape
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import parse_qs, urlparse

from analise import analisar_enunciado
from entrada import validar_enunciado

LIMITE_CORPO = 60_000  # bytes aceitos no envio do formulário


def carregar_c01() -> str:
    arquivo = Path(__file__).parent / "examples" / "casos_avaliacao.json"
    casos = json.loads(arquivo.read_text(encoding="utf-8"))["casos"]
    return next(caso["entrada"] for caso in casos if caso["id"] == "C01")


def registrar(mensagem: str) -> None:
    """Escreve no log do container. Nunca inclui o texto do enunciado."""
    print(mensagem, flush=True)


class Pagina(BaseHTTPRequestHandler):
    def do_GET(self) -> None:
        consulta = parse_qs(urlparse(self.path).query)
        enunciado = carregar_c01() if consulta.get("exemplo") == ["c01"] else ""
        self.mostrar_pagina(enunciado, "Cole um enunciado e envie para gerar o checklist.")

    def do_POST(self) -> None:
        tamanho = int(self.headers.get("Content-Length") or 0)
        if tamanho > LIMITE_CORPO:
            registrar("Envio recusado: corpo acima do limite.")
            self.mostrar_pagina("", "O envio é grande demais. Reduza o enunciado.")
            return

        campos = parse_qs(self.rfile.read(tamanho).decode("utf-8", errors="replace"))
        enunciado = campos.get("enunciado", [""])[0].replace("\r\n", "\n")

        erro = validar_enunciado(enunciado)
        if erro is not None:
            registrar("Envio recusado: enunciado vazio ou acima do limite.")
            self.mostrar_pagina(enunciado, erro)
            return

        registrar(f"Consulta recebida: {len(enunciado)} caracteres.")
        checklist, erro = analisar_enunciado(enunciado)
        if erro is not None:
            registrar("Consulta falhou.")
            self.mostrar_pagina(enunciado, erro)
            return

        registrar("Consulta concluída.")
        self.mostrar_pagina(enunciado, checklist)

    def mostrar_pagina(self, enunciado: str, resultado: str) -> None:
        pagina = f"""<!doctype html>
<html lang="pt-BR">
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Descomplica Enunciado</title>
<body style="max-width: 46rem; margin: 2rem auto; padding: 0 1rem; font-family: system-ui">
<h1>Descomplica Enunciado</h1>
<p>Cole o enunciado e receba uma lista de conferência com trechos de apoio.
Confira cada item no texto original: o modelo pode errar.</p>
<form method="post">
<textarea name="enunciado" rows="12" style="width: 100%" required>{escape(enunciado)}</textarea>
<p><button type="submit">Gerar checklist</button>
<a href="/?exemplo=c01">Usar o exemplo fictício C01</a></p>
</form>
<h2>Resultado</h2>
<pre style="white-space: pre-wrap; overflow-wrap: anywhere">{escape(resultado)}</pre>
</body>
</html>"""
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.end_headers()
        self.wfile.write(pagina.encode("utf-8"))

    def log_message(self, formato: str, *argumentos) -> None:
        registrar("Requisição HTTP atendida.")


if __name__ == "__main__":
    with ThreadingHTTPServer(("0.0.0.0", 8080), Pagina) as servidor:
        servidor.serve_forever()
