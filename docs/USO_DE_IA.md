# Uso de IA

## 26/11/2026 — Avaliação da v4 na Devel

- **Ferramenta e modelo** — Claude Code (Claude Sonnet 5.5) com Claude in Chrome.
- **Tarefa e resultado aproveitado** — Enviar à página os casos fictícios (duas repetições do C01 e C02 a C06), preservar as saídas em `SAIDAS_V4.md` e comparar com o gabarito.
- **Verificação** — Respostas reais da Devel. A comparação com o gabarito foi feita pela ferramenta e ainda precisa da revisão do aluno.

## 25/11/2026 — Revisão do prompt após o eco da instrução (v4)

- **Ferramenta e modelo** — Claude Code (Claude Sonnet 5.5).
- **Tarefa e resultado aproveitado** — Separar, no prompt, os títulos de seção das regras de preenchimento, depois que o modelo copiou a instrução no Objetivo.
- **Verificação** — Testes locais do terminal, da página e da conferência. A causa do eco é uma hipótese; o efeito da mudança ainda não foi observado no modelo.

## 25/11/2026 — Correção da conferência após o teste da v3

- **Ferramenta e modelo** — Claude Code (Claude Sonnet 5.5).
- **Tarefa e resultado aproveitado** — Analisar a captura da v3 e corrigir a conferência, que ignorava o “Trecho de apoio:” no meio da linha. A conferência por início de linha, sugerida antes pela própria ferramenta, foi substituída.
- **Verificação** — Defeito reproduzido localmente antes da mudança; testes novos e anteriores passaram depois. Um caso de teste esperava um resultado que o código não pode garantir em texto sem aspas e foi ajustado, com o limite registrado. A correção não foi testada na Devel.

## 25/11/2026 — Revisão da conferência de citações e do prompt (v3)

- **Ferramenta e modelo** — Claude Code (Claude Sonnet 5.5), com Claude in Chrome para repetir o teste na página da Devel.
- **Tarefa** — Executar o C01 na imagem v2, registrar os resultados e revisar a conferência de citações e o prompt a partir deles.
- **Resultado aproveitado** — Registro das execuções em `AVALIACAO.md` e `EVOLUCAO.md`; conferência por linha “Trecho de apoio:” que aceita aspas retas e avisa quando não há trechos; prompt com exemplo, regra no fim e pergunta sobre o fuso.
- **Verificação** — Testes locais com a resposta real da Devel e casos de borda, mais regressão do terminal e da página contra um servidor Ollama falso. A v3 ainda não foi reconstruída nem testada na Devel. A afirmação de que o exemplo no prompt melhora o resultado é uma hipótese não confirmada.

## 23/11/2026 — Terminal chamando o Ollama (issue #4)

- **Ferramenta e modelo** — Claude Code (Claude Sonnet 5.5).
- **Tarefa** — Mover o prompt para `prompt.py`, extrair a lógica comum para `analise.py`, fazer o terminal chamar o Ollama, ajustar a conferência de citações à resposta real, transformar a página da Devel em interface com campo de texto (decisão do aluno, após ler o guia da plataforma) e criar `.env.example` e `requirements.txt`.
- **Resultado aproveitado** — `prompt.py` e `analise.py` compartilhados entre terminal e página; `main.py` com a opção `--simulado`; conferência que ignora quebras de linha; instrução pedindo citações entre aspas curvas; página com validação, texto escapado e logs sem o conteúdo do enunciado.
- **Verificação** — Execução do `main.py` e da página contra um servidor Ollama falso local (resposta normal, HTTP 500, servidor fora do ar, variáveis ausentes, entrada vazia, acima do limite e `--simulado`). A chamada ao Ollama institucional ainda não foi testada com este código, e `Dockerfile` e `.dockerignore` foram atualizados sem reconstruir a imagem, porque o Docker do computador do aluno não abriu.

## Revisão da instrução do C01

- **Ferramenta e modelo** — Codex (GPT-6.1).
- **Tarefa e resultado aproveitado** — Revisar a instrução após respostas genéricas e uma tentativa sem texto. A revisão delimitou o enunciado e detalhou o formato e os critérios do checklist.
- **Verificação** — A chamada foi conferida com cliente simulado e a imagem foi exportada. A causa da resposta vazia e a qualidade da nova saída ainda precisam ser verificadas na Devel.

## 09/11/2026 — Diagnóstico da integração com a Devel

- **Ferramenta e modelo** — Codex (GPT-6.1).
- **Tarefa** — Diagnosticar a falha de certificado e preparar uma imagem para testar a comunicação com o Ollama usando o C01 fictício.
- **Resultado aproveitado** — Opção temporária no cliente Python, ativada por variável de ambiente, e reconstrução da imagem Docker. A sugestão de usar `PYTHONHTTPSVERIFY=0` foi descartada por se aplicar ao CPython 2.7 e a imagem usar Python 3.12.
- **Verificação** — A imagem foi construída e exportada. O teste na Devel retornou HTTP 502 inicialmente e, em tentativa posterior, exibiu uma resposta do modelo. A validação com o certificado oficial e a avaliação completa da saída ficaram pendentes. Veja o [registro de evolução](EVOLUCAO.md).

