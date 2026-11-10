# Uso de IA

## Revisão da instrução do C01

- **Ferramenta e modelo** — Codex (GPT-6.1).
- **Tarefa e resultado aproveitado** — Revisar a instrução após respostas genéricas e uma tentativa sem texto. A revisão delimitou o enunciado e detalhou o formato e os critérios do checklist.
- **Verificação** — A chamada foi conferida com cliente simulado e a imagem foi exportada. A causa da resposta vazia e a qualidade da nova saída ainda precisam ser verificadas na Devel.

## 09/11/2026 — Diagnóstico da integração com a Devel

- **Ferramenta e modelo** — Codex (GPT-6.1).
- **Tarefa** — Diagnosticar a falha de certificado e preparar uma imagem para testar a comunicação com o Ollama usando o C01 fictício.
- **Resultado aproveitado** — Opção temporária no cliente Python, ativada por variável de ambiente, e reconstrução da imagem Docker. A sugestão de usar `PYTHONHTTPSVERIFY=0` foi descartada por se aplicar ao CPython 2.7 e a imagem usar Python 3.12.
- **Verificação** — A imagem foi construída e exportada. O teste na Devel retornou HTTP 502 inicialmente e, em tentativa posterior, exibiu uma resposta do modelo. A validação com o certificado oficial e a avaliação completa da saída ficaram pendentes. Veja o [registro de evolução](EVOLUCAO.md).

