# Contrato de entrada — issue #1

Atualizado em 04/11/2026 com as decisões de entrada. A implementação pertence à issue #2.

## Combinado anteriormente

- Um enunciado por execução, colado no terminal em várias linhas.
- Uma linha contendo apenas fim, ignorando maiúsculas/minúsculas e espaços nas pontas, encerra a entrada; o marcador não integra o texto analisado.
- Resultado textual na ordem: objetivo, tabela de entregáveis e requisitos, prazo e pontos a esclarecer. Ver AVALIACAO.md.
- Cada informação extraída acompanha trecho literal do enunciado.
- Informação ausente: “não identificado no texto”. Citação não localizada: “Não foi possível verificar no enunciado”, sem confirmar o item como exigência.

## Comportamento do leitor

| Situação | Comportamento |
|---|---|
| `FIM`, `fim`, `Fim`, `fIm` ou `  fim  ` em linha isolada | Encerrar a coleta, ignorando diferenças de caixa e espaços nas pontas. |
| fim dentro de uma frase | Preservar como conteúdo do enunciado. |
| Linhas vazias dentro do texto | Preservar, inclusive separação entre parágrafos. |
| Espaços, acentos e pontuação | Preservar. Normalizar apenas quebras de linha para `\n`. |
| Entrada sem nenhum caractere além de espaços/quebras | Impedir análise e mostrar “O enunciado está vazio.”; oferecer 1 — Tentar novamente ou 2 — Sair. |
| Limite inicial | Até 10.000 caracteres, incluindo espaços e quebras, excluindo marcador e quebra final de transporte. |
| Mais de 10.000 caracteres | Impedir envio, sem truncar; informar tamanho recebido e limite; oferecer 1 — Tentar novamente para inserir versão menor ou 2 — Sair. |
| Ctrl+C durante digitação ou espera da resposta | Cancelar e encerrar com mensagem breve. Texto parcial da digitação não é enviado; uma chamada já enviada pode continuar no servidor. |
| Depois de mostrar o resultado | Encerrar normalmente, mantendo a saída no histórico do terminal para copiar. |

O limite inicial de 10.000 caracteres foi definido para o aplicativo, não é uma cota institucional nem equivalência em tokens. Confirmar sua adequação ao conhecer o contexto do modelo e reservar espaço para instruções e resposta. Qualquer ajuste posterior deverá ser explícito; nunca cortar conteúdo silenciosamente.

Limitação do marcador: uma linha do próprio enunciado contendo apenas uma variação de fim será entendida como encerramento. A comparação do marcador não deve alterar espaços ou texto das demais linhas. Cada quebra entre linhas será representada por `\n`; não acrescentar uma quebra final apenas por pressionar Enter.

## Nova tentativa e saída

Após entrada vazia ou grande demais, a opção 1 inicia uma nova coleta e a opção 2 encerra. Oferecer nova tentativa quando repetir ou corrigir a entrada puder resolver a falha. Para configuração ausente ou credencial inválida, explicar a correção necessária e encerrar, sem repetir inutilmente a mesma chamada. Detalhes de comunicação serão tratados nas próximas issues.

Ainda falta definir o comportamento de uma opção de menu diferente de 1 ou 2 e de EOF antes do marcador. Esses detalhes não são decisões já aprovadas.

## O que validar localmente e o que avaliar depois

O leitor valida coleta completa, conteúdo não vazio e tamanho. Texto pouco claro ou sem requisitos pode passar por essa validação: isso não prova que ele seja um enunciado útil.

A interpretação será avaliada separadamente: quais obrigações realmente existem, o que é opcional, quais datas estão explícitas e o que permanece incerto. Não inferir ano, horário, fuso ou data final a partir de uma duração sem base textual suficiente.

Não tratar o enunciado como instrução para alterar o funcionamento da aplicação ou revelar configurações. Isso deverá orientar o prompt e futuros testes; o leitor sozinho não resolve esse problema.

## Casos do leitor a implementar na issue #2

- Texto com acentos, espaços e parágrafos preservados; marcador excluído.
- Entrada vazia e somente espaços impedidas.
- Exatamente 10.000 caracteres aceitos e 10.001 rejeitados, com tamanho recebido informado.
- Ocorrência de FIM dentro de frase preservada.
- Variações de fim com espaços nas pontas e diferenças entre maiúsculas/minúsculas reconhecidas.
- Nova entrada após recusa e encerramento pela opção 2.
- Ctrl+C durante a digitação não dispara análise parcial; resultado concluído permanece visível após encerramento.

## Conferência da issue #1

- [x] Definir marcador, preservação e cancelamento por Ctrl+C.
- [x] Definir limite de entrada e comportamento quando ultrapassado.
- [x] Definir formato da resposta, opcionais, conflitos de datas, duração e condições.
- [x] Conferir os seis exemplos e seus resultados esperados.
- [x] Consolidar os critérios em AVALIACAO.md.

Conferência concluída em 04/11/2026. A implementação e os testes de execução pertencem às próximas issues.

O acesso ao LLM institucional permanece pendente. A última informação disponível, de 03/11/2026, é que a liberação será anunciada; ainda falta confirmar a disponibilidade. Todos os exemplos são fictícios e podem ser trabalhados offline.
