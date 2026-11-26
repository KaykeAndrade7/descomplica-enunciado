# Avaliação da extração — issue #1

Atualizado em 04/11/2026. Formato, gabaritos e critérios conferidos para a base inicial do projeto. São critérios do projeto, sem pesos de nota institucional. Base inicial: [casos fictícios](../examples/casos_avaliacao.json). Não há resultados de modelo nesta etapa.

## Formato da resposta

1. **Objetivo:** finalidade do trabalho com trecho de apoio. Quando não estiver clara, mostrar “Objetivo não identificado claramente no texto”.
2. **Entregáveis e requisitos:** tabela relacionando o que entregar ao que cada item precisa atender, com trechos que sustentem tanto a entrega quanto seus requisitos. Requisitos gerais não devem ser associados arbitrariamente a um entregável.
3. **Prazo:** manter a seção mesmo sem data; nesse caso, mostrar “Prazo não identificado no texto”. Não completar ano, horário ou fuso por conta própria.
4. **Pontos a esclarecer:** informações relevantes ausentes, conflitos e ambiguidades.

Itens opcionais mencionados também aparecem, identificados como “Opcional — não é uma exigência”, com trecho de apoio. Podem ficar junto dos itens relacionados, mantendo essa distinção explícita.

Quando houver datas conflitantes sem regra para resolver o conflito, mostrar ambas com seus trechos e pedir confirmação. Apresentar duração prevista como estimativa, separada do prazo, sem calcular uma data por conta própria.

Preservar condições como “se houver”: não transformar um requisito condicional em incondicional nem afirmar que a condição ocorreu.

Cada informação extraída deve ter apoio literal. Mensagens sobre informação ausente não exigem uma citação inexistente. Para trecho não localizado, mostrar “Não foi possível verificar no enunciado”, sem confirmar a afirmação como exigência.

Ver o [exemplo completo de resposta para C01](EXEMPLO_RESPOSTA.md). É uma saída esperada para conferência, não uma resposta de LLM executada.

## Como usar o gabarito

Cada entrada contém texto fictício, itens esperados com identificação e trechos literais, dúvidas e informações que não devem ser inventadas. Os textos não são transcrições de atividades do curso.

A resposta pode usar outra redação e agrupar itens, mantendo a ordem das seções definida acima e preservando todas as obrigações e seus qualificadores. Um mesmo trecho pode sustentar vários itens. O gabarito não exige igualdade literal da resposta inteira; os trechos de apoio precisam existir literalmente na entrada. Menções a ausência de informação não têm citação inventada.

## Critérios definidos antes da execução

| Critério | Como verificar |
|---|---|
| Cobertura | Relacionar cada ID esperado ao item correspondente da resposta; registrar os IDs omitidos. |
| Invenção | Listar obrigações, datas, ferramentas ou detalhes afirmados sem apoio. Dúvida explícita não conta como obrigação inventada. |
| Fidelidade da citação | Conferir se cada trecho citado é substring literal da entrada, com quebras de linha normalizadas. |
| Correção da interpretação | Conferir se o trecho sustenta a afirmação, incluindo negações, condições e caráter obrigatório/opcional. |
| Datas e ausência | Preservar somente a precisão presente no texto; apontar datas ou horários ausentes sem completá-los. |
| Ambiguidade | Apresentar incertezas relevantes sem decidir arbitrariamente entre regras conflitantes. |
| Estrutura e objetivo | Manter as quatro seções, relacionar entregáveis e requisitos e indicar objetivo ausente quando necessário. |
| Opcionais e condições | Mostrar opcionais sem torná-los exigências; preservar condições e separar duração prevista de prazo. |

Para cada caso, registrar quantidade de itens esperados cobertos/total, IDs omitidos, invenções, citações ausentes, interpretações incorretas e dúvidas não sinalizadas. Não calcular uma nota composta nesta primeira versão.

Objetivo nos seis casos: cobrir todos os itens esperados, sem invenções, com trechos fiéis e interpretação correta; sinalizar as dúvidas obrigatórias do gabarito. É uma meta de avaliação desta amostra, não uma garantia de comportamento em outros textos. Falhas devem permanecer registradas.

Se uma citação não for encontrada, a aplicação deve apresentar “Não foi possível verificar no enunciado”. Essa proteção é avaliada separadamente: o aviso não torna correta a extração original e não apaga a falha da avaliação.

## Registro futuro de execução

Usar uma tabela com: data, ID do caso, provedor/modelo, versão do prompt, configuração, resultado real ou simulado, itens cobertos/esperados, omissões, invenções, citações sem apoio, interpretações incorretas, dúvidas omitidas e observações. Preservar a saída permitida para conferência, sem segredos.

Conferir os gabaritos antes da primeira avaliação. Se um gabarito mudar depois, registrar motivo e versão e reavaliar as saídas afetadas; não ajustar o esperado só para favorecer o modelo. Sem LLM disponível, conferir a consistência dos exemplos não equivale a avaliar um modelo.

## Registros de execução

| Data | Caso | Modelo | Prompt e configuração | Resultado | Cobertos | Omissões | Invenções | Citações sem apoio | Interpretação incorreta | Dúvidas omitidas | Observações |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 25/11/2026 | C01 | `qwen3.5:9b-q4_K_M` (Ollama da Devel) | `prompt.py` da branch `feat/4-terminal-llm`, sem commit; imagem v2; `think: false`; TLS temporário ativo | Real, página da Devel, 1 execução | 4/4 (E1, E2, R1, P1) | Nenhuma | Leves: “instruções claras” no README e “formatação das entregas” | 0 citadas; nenhuma citação foi produzida | Afirmou “não houveram ambiguidades”, contra o gabarito | 1/1: fuso do horário | Sem trechos de apoio apesar do prompt revisado; a verificação literal não teve o que conferir. Detalhes em [Evolução](EVOLUCAO.md). |
| 25/11/2026 | C01 | `qwen3.5:9b-q4_K_M` (Ollama da Devel) | Mesma imagem v2 e mesmo prompt da execução anterior | Real, página da Devel, 2ª execução | 4/4 (E1, E2, R1, P1) | Nenhuma | Entrada “via input ou arquivo”; README com “pré-requisitos, modo de uso do comando e exemplo de entrada” | 0 citadas; nenhuma citação foi produzida | Nenhuma identificada | 1/1: fuso do horário (omitido de novo) | Entregáveis em lista, e dúvidas concretas sobre a forma de entrada e o nível de detalhe do README. Saída diferente da 1ª execução com o mesmo texto. |
| 25/11/2026 | C01 | `qwen3.5:9b-q4_K_M` (Ollama da Devel) | Mesma imagem v2 e mesmo prompt; executada pelo Claude in Chrome na porta pública do container | Real, página da Devel, 3ª execução | 4/4 (E1, E2, R1, P1) | Nenhuma | Leves: “instruções claras” no README; afirmação de que não há requisitos detalhados sobre o formato de entrada | 3 trechos de apoio, todos literais no enunciado (conferidos manualmente); o código não os verificou porque vieram entre aspas retas | Nenhuma identificada | 1/1: fuso do horário (omitido pela 3ª vez) | Primeira execução com trechos de apoio, mas agrupados no fim da resposta, sem ligação com cada item, e com aspas retas em vez das curvas pedidas. Dúvidas concretas sobre entrada, validação e formato do README. |
| 25/11/2026 | C01 | `qwen3.5:9b-q4_K_M` (Ollama da Devel) | Imagem v3 (informada pelo aluno); prompt revisado; `think: false` | Real, página da Devel, 1ª execução da v3 (captura) | 3/4 (E1, E2, P1); R1 aparece misturado ao entregável e o Objetivo não foi preenchido | Objetivo substituído pelo texto da instrução | Nenhuma identificada | 3 trechos literais no enunciado (conferidos manualmente); o código não os verificou, por estarem no meio da linha | “Lista de código-fonte Python que leia…” confunde entregável e requisito | Nenhuma: perguntou o fuso | Eco do prompt no Objetivo. Defeito da conferência corrigido depois, ainda sem nova imagem. |
| 25/11/2026 | C01 | `qwen3.5:9b-q4_K_M` (Devel) | Imagem v4; `think: false` | Real, 1ª da v4 (captura do aluno) | 4/4 | Nenhuma | “instruções detalhadas” | Citações literais; um rótulo vazio em Pontos a esclarecer, sem aviso | Nenhuma identificada | Nenhuma | [Saída](SAIDAS_V4.md). |
| 26/11/2026 | C01 | `qwen3.5:9b-q4_K_M` (Devel) | Imagem v4; página no Claude in Chrome | Real, 2ª da v4 | 4/4 | Nenhuma | Nenhuma relevante | Citações literais | Nenhuma identificada | Nenhuma | [Saída](SAIDAS_V4.md). |
| 26/11/2026 | C01 | `qwen3.5:9b-q4_K_M` (Devel) | Imagem v4 | Real, 3ª da v4 | 4/4 | Nenhuma | Nenhuma relevante | Citações literais | Nenhuma identificada | 1/1: fuso do horário | Afirmou não haver pontos a esclarecer. |
| 26/11/2026 | C02 | `qwen3.5:9b-q4_K_M` (Devel) | Imagem v4 | Real, 1 execução | 3/3 (E1, O1, O2 parcial) | Não diz que o uso da planilha é só recomendado | Nenhuma obrigação nova | 3 literais; 1 rótulo com aviso | O2: “Planilha usada”, sem marcar como opcional | Nenhuma: indicou prazo ausente | Itens opcionais listados junto dos entregáveis. |
| 26/11/2026 | C03 | `qwen3.5:9b-q4_K_M` (Devel) | Imagem v4 | Real, 1 execução | 2/2 (E1, R1) | Nenhuma | “reflexão pessoal”; “pelo menos uma” | Citações exibidas literais; 3 rótulos com aviso (E1, Prazo, Pontos) | Nenhuma relevante | Nenhuma (prazo e formato) | Aviso também em item de informação ausente. |
| 26/11/2026 | C04 | `qwen3.5:9b-q4_K_M` (Devel) | Imagem v4 | Real, 1 execução | 3/3 (E1, P1, P2) | Nenhuma | “detalhando as descobertas” | Citações literais | Nenhuma: não escolheu entre as datas | Nenhuma: conflito sinalizado | Melhor resultado da rodada. |
| 26/11/2026 | C05 | `qwen3.5:9b-q4_K_M` (Devel) | Imagem v4 | Real, 1 execução | 3/4 (E1, E2, D1); R1 só em Prazo e nos trechos | R1 não listado como requisito | “apresentar” o protótipo; perguntas especulativas | Literais na conferência manual; citações em linhas sem rótulo não foram verificadas pelo código | Pergunta trata as duas semanas como término com data e fuso | Nenhuma: envio sem data | Resposta longa e confusa. |
| 26/11/2026 | C06 | `qwen3.5:9b-q4_K_M` (Devel) | Imagem v4 | Real, 1 execução | 4/5 (R1, E1, E2, R3); R2 sem a condição | Condição “Se houver” de R2; trabalho sozinho ou em dupla | “sem erros”; “resumo da análise” | 2 literais; 4 rótulos com aviso (E1, Prazo, 2 em Pontos) | **R2 afirma que há valores ausentes a explicar** | Nenhuma: indicou prazo ausente | Falha mais grave da rodada. |
