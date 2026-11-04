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
