import json
import re
from pathlib import Path

from entrada import ler_enunciado, validar_enunciado


def verificar_trechos_de_apoio(enunciado: str, resposta: str) -> str:
    def conferir(citacao: re.Match[str]) -> str:
        if citacao.group(1) in enunciado:
            return citacao.group(0)
        return "[Não foi possível verificar no enunciado]"

    return re.sub(r"“([^”]+)”", conferir, resposta)


def mostrar_resposta_simulada(texto: str) -> None:
    pasta = Path(__file__).resolve().parent
    exemplos = pasta / "examples" / "casos_avaliacao.json"
    casos = json.loads(exemplos.read_text(encoding="utf-8"))["casos"]
    caso = next(caso for caso in casos if caso["id"] == "C01")

    if texto.strip() != caso["entrada"]:
        print("Entrada válida. A demonstração usa o enunciado fictício C01.")
        return

    exemplo = pasta / "docs" / "EXEMPLO_RESPOSTA.md"
    resposta = exemplo.read_text(encoding="utf-8")
    inicio = resposta.index("## Objetivo")
    print("\nResposta simulada — C01\n")
    print(verificar_trechos_de_apoio(texto, resposta[inicio:].rstrip()))


def tentar_novamente() -> bool:
    while True:
        print("1 — Tentar novamente")
        print("2 — Sair")
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            return True
        if opcao == "2":
            return False

        print("Opção inválida. Digite 1 ou 2.")


def main() -> None:
    try:
        while True:
            print("Cole o enunciado e digite fim em uma linha separada.")
            texto = ler_enunciado()
            erro = validar_enunciado(texto)

            if erro is None:
                mostrar_resposta_simulada(texto)
                return

            print(erro)
            if not tentar_novamente():
                return
    except (EOFError, KeyboardInterrupt):
        print("\nEntrada cancelada.")


if __name__ == "__main__":
    main()
