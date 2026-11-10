# Evolução do Descomplica Enunciado

## Do problema à demonstração local

- Em 03/11/2026, o projeto foi definido para ajudar estudantes a identificar o que entregar a partir de um enunciado. A saída foi planejada como um checklist com trechos de apoio. As escolhas iniciais estão em [Decisões](DECISOES.md).
- A issue #1 definiu o contrato de entrada, o caso fictício C01 e os critérios de avaliação. O PR #13 integrou essa documentação.
- A issue #2 implementou a demonstração local no terminal, com entrada multilinha encerrada por `FIM`, validação e resposta simulada para o C01. O PR #14 integrou a implementação. O [README](../README.md) registra as verificações locais.
- Na issue #3, a página de teste em Python e o cliente Ollama foram usados para validar a integração institucional. O Dockerfile empacota a página, o cliente e o caso C01. A página escuta na porta interna 8080 e o botão **Testar C01** envia o enunciado ao Ollama via `POST /api/chat`.

## Implantação e teste da LLM institucional

| Etapa | Resultado observado |
|---|---|
| Primeira tentativa na Devel, 06/11/2026 | A imagem respondeu HTTP 200 localmente. Na Devel, o container aparecia em execução na porta 8080, mas a prévia ficou em branco e o acesso direto expirou. Foi aberto um chamado de suporte. |
| Novo fluxo de implantação, 09/11/2026 | A imagem foi criada com `docker build`, exportada com `docker save` e enviada como TAR de cerca de 43 MB. A porta 8080 foi configurada no painel. A página abriu pelo endereço público atribuído pela Devel. |
| Primeiro C01 no novo ambiente | A chamada interna ao Ollama falhou com `CERTIFICATE_VERIFY_FAILED: self-signed certificate`. Foi solicitada ao suporte a orientação para configurar o certificado ou a CA oficial. |
| Teste temporário de TLS | O cliente passou a aceitar `OLLAMA_TESTE_SEM_VERIFICACAO_TLS=1` para desativar a validação do certificado e do nome do servidor. Uma nova imagem foi construída e exportada para esse teste. A verificação permanece ativa por padrão. |
| Primeira resposta após ativar a opção | A página exibiu HTTP 502 na chamada ao Ollama. Os registros `POST / ... 200` do container correspondiam à resposta da página ao navegador. A causa do 502 ficou sem confirmação. |
| Nova tentativa com o painel indicando LLM disponível | O modelo devolveu uma resposta ao C01 fictício. A evidência foi a saída exibida na página, que continha a análise do enunciado e os arquivos sugeridos pelo modelo. |

## Avaliação da primeira resposta real

O modelo identificou o objetivo de calcular a média, os entregáveis (código-fonte e README), os requisitos e o prazo fictício de 18/11/2026 às 23h59. O trecho “README com instruções de execução” aparece literalmente na [entrada do C01](../examples/casos_avaliacao.json).

A resposta também incluiu um programa Python e instruções de README, extrapolando o escopo do checklist. A resposta foi exibida como texto bruto na página de teste. A qualidade da extração e a fidelidade de todas as citações ainda precisam passar pelos critérios de [avaliação](AVALIACAO.md).

## Segundo teste do C01 na Devel

Com o mesmo enunciado e a instrução revisada, o modelo devolveu as quatro seções em texto simples. A resposta ficou restrita ao checklist e os trechos entre aspas conferem com a entrada do C01.

As descrições ainda perderam precisão. O objetivo ficou genérico, embora o trecho de apoio mencione ler números e calcular a média. O README apareceu como documentação genérica. O prazo de 18/11/2026 às 23h59 ficou só no trecho citado. A resposta apontou dúvidas sobre o formato da entrada e o tratamento de entradas inválidas ou vazias.

## Terceiro teste do C01 na Devel

A instrução passou a pedir que cada item preserve os detalhes explícitos do enunciado, inclusive os nomes dos entregáveis e a data e o horário do prazo. Na tentativa observada, o cliente exibiu “O Ollama devolveu uma resposta sem texto.” Essa mensagem indica que o campo `message.content` não continha texto utilizável. A causa ficou sem confirmação e a qualidade da nova instrução ainda não pôde ser avaliada.

## Teste de diagnóstico na Devel

O cliente passou a mostrar o motivo de término, a contagem de tokens e a quantidade de outros campos de mensagem com texto quando a resposta final vem vazia. O teste simulado confirmou a mensagem de diagnóstico e o retorno normal de um checklist. A primeira tentativa de exportação falhou porque o motor Linux do Docker Desktop estava inacessível. Em 10/11/2026, a imagem foi reconstruída e o TAR de diagnóstico foi exportado.

O prompt da quarta versão delimita o C01 como texto a analisar, especifica as quatro seções e orienta como tratar itens opcionais, condições, datas conflitantes, lacunas e citações. Um teste local com cliente simulado confirmou o envio da instrução e do mesmo C01. Na Devel, a quarta versão voltou a exibir “O Ollama devolveu uma resposta sem texto.”

Com o diagnóstico ativo, o teste na Devel mostrou `done_reason=length`, `eval_count=3570` e um outro campo da mensagem com texto. A geração atingiu um limite antes de devolver um checklist em `message.content`. O diagnóstico não identifica o outro campo. A hipótese é que parte da geração tenha ocorrido no modo de raciocínio do modelo.

## C01 com `think: false`

Na Devel, o mesmo C01 e o mesmo prompt produziram um checklist em `message.content` após a inclusão de `think: false` na requisição. A captura mostra as quatro seções, sem resolução do exercício. Esse resultado favorece a hipótese de que o modo de raciocínio contribuiu para a resposta vazia anterior. Uma execução bem-sucedida ainda não estabelece a repetibilidade do resultado.

Na comparação manual com o gabarito, a resposta cobriu os quatro itens principais: código-fonte (E1), README com instruções de execução (E2), programa Python que calcula e mostra a média de uma lista (R1) e prazo de 18/11/2026 às 23h59 (P1). A resposta apontou uma dúvida sobre o formato da entrada, mas omitiu a ausência de fuso horário. “Apresentar o resultado na tela” e a menção a sistema operacional ou ambiente no item do README acrescentam detalhes sem apoio explícito. Os trechos das seções Objetivo e Prazo conferem com o enunciado. Em Entregáveis e requisitos, o modelo reuniu os trechos no fim da seção, dificultando a conferência por item.

Na repetição do C01 com `think: false`, o modelo voltou a entregar texto final e cobriu os quatro itens principais (E1, E2, R1 e P1). A saída variou em relação à execução anterior: omitiu todos os trechos de apoio, colocou o prazo na seção de entregáveis e requisitos e deixou de apontar o fuso ausente. Mencionou requisitos de instalação e comando de execução como detalhes do README, embora o enunciado só peça instruções de execução. A cobertura dos itens principais se repetiu em duas execuções, com variação no cumprimento do formato e na fidelidade dos detalhes.

As duas execuções usaram a imagem de teste com o modelo institucional `qwen3.5:9b-q4_K_M` no Ollama da Devel. A conferência da primeira saída foi manual, usando a [entrada e o gabarito do C01](../examples/casos_avaliacao.json). As três linhas de apoio exibidas correspondem a trechos da entrada quando se desconsideram as quebras visuais da página e se normaliza a quebra de linha entre as duas frases na seção de entregáveis. A presença literal dessas frases não dá apoio às menções de tela e sistema operacional, nem resolve o vínculo de cada item com sua citação. O teste confirma a integração da página com a LLM para o C01 fictício. O fluxo do terminal ainda usa resposta simulada.

## Próximas verificações

- Aplicar os mesmos critérios aos demais casos fictícios para verificar a cobertura, a estrutura e a presença dos trechos de apoio.
- Aplicar a verificação literal dos trechos à resposta real e sinalizar os que o código não localizar no enunciado.
- Confirmar a orientação oficial sobre o certificado, retirar a opção temporária da configuração da Devel e repetir o teste com a verificação TLS ativa.
