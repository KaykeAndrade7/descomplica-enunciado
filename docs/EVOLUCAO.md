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

## Primeiro teste da imagem v2, com campo de texto (25/11/2026)

A imagem `kaykega87gmailcom:v2` foi construída a partir do código local da branch `feat/4-terminal-llm`, ainda sem commit, e enviada à Devel. Ela traz a página com campo de texto, o prompt revisado para pedir citações entre aspas curvas, a lógica de `analise.py` e `think: false`. O modelo foi `qwen3.5:9b-q4_K_M`, configurado nas variáveis do portal, com a opção temporária de TLS ainda ativa. O enunciado foi o C01 fictício.

Resultado observado, em uma única execução: a página devolveu as quatro seções em texto simples, restritas ao checklist, sem resolver a atividade. Foram cobertos os quatro itens principais (E1 código-fonte, E2 README com instruções de execução, R1 programa que lê a lista e mostra a média, P1 prazo de 18/11/2026 às 23h59).

Falhas preservadas:

- **Nenhum trecho de apoio.** A resposta não trouxe nenhuma linha “Trecho de apoio”, apesar do prompt revisado. A conferência de citações não teve o que verificar, e o código atual não sinaliza a ausência: itens sem citação passam como se estivessem confirmados.
- **Dúvida omitida.** O gabarito espera a dúvida sobre o fuso do horário. A seção Pontos a esclarecer afirmou que “não houveram ambiguidades”, contrariando o gabarito. A frase também ignora o texto padrão pedido no prompt (“Nenhum ponto a esclarecer identificado.”).
- **Detalhes sem apoio explícito.** O README ganhou o qualificativo “instruções claras” e a seção de dúvidas citou “formatação das entregas”, que o enunciado não menciona.
- **Estrutura.** Entregáveis e requisitos vieram em parágrafo, sem a relação por item pedida no formato de resposta.

Limites desta evidência: uma execução, sem os Logs do container conferidos e sem repetição. A captura prova a chamada real e a resposta, mas não mostra a causa de o modelo ignorar o formato de citação. Resultados de execuções anteriores usaram o prompt antigo e não são comparáveis diretamente.

### Segunda execução da imagem v2

Com o mesmo C01, a mesma imagem e o mesmo prompt, a segunda execução cobriu de novo os quatro itens principais e trouxe entregáveis em lista, com pontos a esclarecer concretos: como os números são fornecidos ao programa e qual o nível de detalhe do README. Isso difere da primeira execução, que afirmou não haver ambiguidades.

Repetiram-se: nenhuma linha de “Trecho de apoio” e a omissão da dúvida sobre o fuso do horário. Apareceram detalhes sem apoio no enunciado: a entrada “via input ou arquivo” e o README com “pré-requisitos, modo de uso do comando e exemplo de entrada”. Duas execuções com o mesmo texto deram saídas diferentes, o que indica variação do modelo; duas amostras ainda não permitem estimar a frequência de cada falha.

### Terceira execução da imagem v2

Executada pelo Claude in Chrome na porta pública do container, com o C01 e o mesmo prompt. A resposta cobriu os quatro itens principais e, pela primeira vez, trouxe três linhas “Trecho de apoio”, todas literais no enunciado (conferência manual). Ainda assim:

- As citações vieram **agrupadas no fim**, sem ligação com cada item, e entre **aspas retas**. O prompt pede aspas curvas e a verificação do código só reconhece aspas curvas, então essas citações não foram verificadas pelo programa. Se uma delas fosse inventada, passaria sem aviso.
- O fuso do horário foi omitido pela terceira vez em três execuções.
- Apareceram detalhes sem apoio direto: “instruções claras” e a afirmação de que não há requisitos detalhados sobre o formato de entrada.

Nas três execuções com o mesmo texto, os trechos de apoio apareceram uma vez. O modelo consegue seguir esse pedido, mas não de forma consistente nem no formato solicitado. Três amostras não permitem estimar a frequência.

## Revisão preparada para a v3 (25/11/2026)

Com base nas três execuções da v2, foram feitas duas mudanças, ainda não reconstruídas nem testadas na Devel:

- **Código.** A conferência passou a olhar as linhas “Trecho de apoio:” e aceita aspas curvas, aspas retas e texto sem aspas. Se a resposta não trouxer nenhum trecho, o programa avisa no topo que nada foi verificado. Foi verificada localmente com a resposta real da 3ª execução e com casos de borda; a verificação só confirma a presença literal, não que o trecho sustente a afirmação.
- **Prompt.** Passou a incluir um exemplo curto do formato, a regra dos trechos no fim, o pedido de não agrupar as citações e uma pergunta sobre o fuso quando o prazo tem horário sem fuso. Removeu-se o “antes de responder, confira”, que depende de raciocínio e a execução usa `think: false`. Foi uma mudança conjunta; se o resultado melhorar, não será possível dizer qual parte ajudou.

A regra do fuso é geral, não específica do C01. Para saber se as mudanças servem além de um caso, o teste da v3 deve incluir C02 a C06 e repetir cada caso mais de uma vez.

## Primeiro teste da imagem v3 na Devel (25/11/2026)

C01 fictício, uma execução, evidência por captura da página. O aluno informou ter reconstruído a imagem e enviado à Devel; os Logs e as variáveis do container não foram conferidos.

Melhoras observadas nesta execução: os dois entregáveis e o prazo trouxeram trecho de apoio junto de cada item, literais no enunciado (conferência manual), e a dúvida sobre o fuso apareceu pela primeira vez.

Falhas preservadas:

- **Instrução ecoada.** A seção Objetivo repetiu o texto do prompt (“Descreva a tarefa concreta e o resultado esperado em uma frase…”) em vez de descrever o objetivo.
- **Formato.** Os trechos vieram na mesma linha do item, e não em linha própria, com aspas retas.
- **Defeito no código.** A conferência da v3 só reconhecia o rótulo no início da linha. Nesta resposta, **nenhuma das três citações foi verificada pelo programa**, e não apareceu aviso. Uma citação inventada nesse formato passaria sem sinalização.
- **Redação imprecisa.** “Lista de código-fonte Python que leia…” mistura o entregável com o requisito do programa.

Uma execução não mostra que o prompt melhorou de forma consistente.

**Correção.** A conferência passou a reconhecer o rótulo em qualquer posição da linha. O defeito foi reproduzido antes da mudança e testado depois, localmente, com o formato desta captura e citações inventadas. Limite: em texto sem aspas, tudo o que vem depois do rótulo até o próximo rótulo ou o fim da linha é tratado como citação. A correção ainda não está na imagem da Devel; o eco da instrução no Objetivo continua sem correção.

## Revisão do prompt para a v4 (25/11/2026)

Na v3, cada título de seção vinha seguido, na linha de baixo, de uma ordem como “Descreva a tarefa…”. A hipótese é que o modelo tratou esse texto como conteúdo da seção. O prompt passou a listar os quatro títulos, pedir apenas as conclusões abaixo deles, reunir as regras em uma lista separada e pedir que não sejam copiadas. O conteúdo das regras foi mantido; no Objetivo, a redação passou a ser “diga em uma frase o que o estudante precisa fazer”.

Os testes locais passaram, mas eles não executam o modelo. A v4 inclui também a correção da conferência. Falta construir a imagem e testar na Devel, repetindo o C01 e executando C02 a C06.

## Teste da v4 na Devel (25 e 26/11/2026)

Três execuções do C01 (a primeira pelo aluno) e uma de cada caso de C02 a C06, as últimas sete pelo Claude in Chrome, com respostas entre 6 e 13 segundos nas seis enviadas em sequência. Saídas em [SAIDAS_V4](SAIDAS_V4.md) e avaliação em [AVALIACAO](AVALIACAO.md).

Observado:

- A instrução não foi copiada em nenhuma das oito saídas, e todas trouxeram trechos de apoio.
- No C01, os quatro itens foram cobertos nas três execuções; o fuso foi perguntado em duas.
- No C04, o conflito de datas foi sinalizado sem escolher uma delas.
- C06: a condição “Se houver” foi perdida no item sobre valores ausentes, e a opção de trabalhar sozinho ou em dupla foi omitida.
- C05: a demonstração de até cinco minutos não foi listada como requisito, e uma pergunta tratou a duração de duas semanas como se tivesse data de término.
- C02: o uso da planilha não foi apresentado como apenas recomendado.

Limitações da aplicação observadas nesta rodada, ainda sem correção:

- Um rótulo “Trecho de apoio:” vazio passa sem aviso e conta como trecho.
- Citações em linhas seguintes, sem o rótulo e com aspas retas, não são verificadas.
- O aviso aparece também onde a informação está ausente, e a página não preserva o texto substituído. Não é possível saber se havia uma citação inventada ou apenas uma observação como “não há”.

Cada caso de C02 a C06 foi executado uma vez; isso não mede frequência. A comparação com versões anteriores vale apenas para o C01.

## Próximas verificações

- Aplicar os mesmos critérios aos demais casos fictícios para verificar a cobertura, a estrutura e a presença dos trechos de apoio.
- Aplicar a verificação literal dos trechos à resposta real e sinalizar os que o código não localizar no enunciado.
- Confirmar a orientação oficial sobre o certificado, retirar a opção temporária da configuração da Devel e repetir o teste com a verificação TLS ativa.
