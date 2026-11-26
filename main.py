import json
import sys
from pathlib import Path

from analise import MENSAGEM_SEM_CONFIGURACAO, analisar_enunciado, verificar_trechos_de_apoio
from entrada import ler_enunciado, validar_enunciado


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


def consultar_modelo(texto: str) -> str | None:
    """Envia o enunciado ao modelo. Devolve o checklist ou None se algo falhar."""
    print("Consultando o modelo; isso pode levar alguns segundos...")
    checklist, erro = analisar_enunciado(texto)
    if erro is not None:
        print(erro)
        if erro == MENSAGEM_SEM_CONFIGURACAO:
            print("Para ver a demonstração sem o modelo, use: python main.py --simulado")
        return None
    return checklist


def mostrar_resposta_do_modelo(checklist: str) -> None:
    print("\nChecklist gerado pelo modelo. Confira cada item no enunciado original.\n")
    print(checklist)


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
    simulado = "--simulado" in sys.argv[1:]
    try:
        while True:
            print("Cole o enunciado e digite fim em uma linha separada.")
            texto = ler_enunciado()
            erro = validar_enunciado(texto)

            if erro is None:
                if simulado:
                    mostrar_resposta_simulada(texto)
                    return
                checklist = consultar_modelo(texto)
                if checklist is None:
                    sys.exit(1)
                mostrar_resposta_do_modelo(checklist)
                return

            print(erro)
            if not tentar_novamente():
                return
    except (EOFError, KeyboardInterrupt):
        print("\nEntrada cancelada.")


if __name__ == "__main__":
    main()
