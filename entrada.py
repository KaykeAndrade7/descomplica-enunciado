LIMITE_ENUNCIADO = 10_000


def ler_enunciado() -> str:
    """Lê o enunciado do terminal até o marcador fim ou o fim da entrada."""
    linhas = []

    while True:
        try:
            linha = input()
        except EOFError:
            break

        if linha.strip().casefold() == "fim":
            break

        linhas.append(linha)

    return "\n".join(linhas)


def validar_enunciado(texto: str) -> str | None:
    """Devolve uma mensagem de erro ou None quando o texto é válido."""
    if not texto.strip():
        return "O enunciado está vazio."

    tamanho = len(texto)
    if tamanho > LIMITE_ENUNCIADO:
        tamanho_formatado = f"{tamanho:,}".replace(",", ".")
        limite_formatado = f"{LIMITE_ENUNCIADO:,}".replace(",", ".")
        return (
            f"O enunciado tem {tamanho_formatado} caracteres. "
            f"O limite é de {limite_formatado} caracteres."
        )

    return None
