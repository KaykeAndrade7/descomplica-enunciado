# Decisões iniciais

Registro de 03/11/2026. Hoje é dedicado à preparação e às decisões; início da implementação previsto para 04/11/2026, conforme orientação do aluno. Esta previsão é de trabalho pessoal, não um prazo institucional.

## Decisões confirmadas pelo aluno

| Decisão | Alternativa considerada | Justificativa |
|---|---|---|
| Organizar requisitos de enunciados para estudantes | Organização de anotações e temas de jogos | O aluno preferiu um problema cotidiano ligado a entender o que entregar. |
| Entrada manual pelo terminal e saída textual | Leitura de PDF e acesso a links | Manter o primeiro projeto pequeno e verificável. |
| Apresentar trecho de apoio para cada item extraído | Apenas apresentar a lista resumida | Facilitar a conferência da origem das informações. |
| Usar o LLM institucional | Outro provedor | Aproveitar o recurso oferecido pelo programa; confirmar disponibilidade e acesso. |
| Criar o repositório e decidir hoje; implementar a partir de amanhã | Começar o código imediatamente | Separar a definição do trabalho da implementação, conforme preferência do aluno. |
| Encerrar a entrada com `FIM` em uma linha isolada | Encerramento sem marcador explícito | Permitir colar um enunciado com várias linhas; o marcador não integra o texto enviado. |
| Sinalizar itens com citação não localizada como “Não foi possível verificar no enunciado” | Descartar o item ou chamá-lo apenas de “não verificado” | Explicitar a limitação e permitir revisão humana, sem tratar o item como requisito confirmado. |
| Organizar trabalho com Project, milestones, issues e PRs vinculados | Controle apenas pela documentação | Acompanhar o progresso dos três níveis e ligar mudanças a tarefas verificáveis. |
| Começar pelo contrato de entrada e avaliação offline | Integrar imediatamente um provedor alternativo | Preparar exemplos e critérios enquanto o institucional não está disponível; alternativa externa continua opcional. |

## Escolhas operacionais do assistente

- Nome definitivo escolhido pelo aluno em 03/11/2026: **Descomplica Enunciado**, repositório `descomplica-enunciado`.
- Branch principal: main. Evolução em branches curtas com PRs.
- Preservar histórico real. Criar os marcos p0-basico, p0-intermediario e p0-avancado somente quando os respectivos estados existirem e forem verificados.
- Publicar documentação autoral. Materiais autenticados do curso permanecem na base local.

## Propostas técnicas ainda a fechar

A definição do problema, público, entrada, saída e limites está fechada para iniciar o desenvolvimento. As pendências abaixo são técnicas e não representam uma nova escolha de problema.

- Separar entrada, configuração, preparação da solicitação, chamada ao LLM, validação e apresentação, sem abstrações desnecessárias.
- Detalhar a verificação local dos trechos de apoio. O objetivo é obter citações fiéis; o aviso acordado é uma proteção para desvios, não um resultado desejado. A existência do trecho não comprova a correção semântica da interpretação.
- Definir formato interno da resposta e comportamento quando a saída do modelo for inválida; não presumir suporte nativo a JSON.
- Definir limite de entrada e parâmetros após conhecer a interface institucional.
- Selecionar versão do Python e dependências após confirmar o acesso; não instalar dependências nesta etapa.

## Critérios e exemplos a detalhar antes dos testes

Verificar requisitos omitidos ou inventados, fidelidade das citações, separação entre recomendações e obrigações, datas explícitas e informações ausentes/ambíguas. Além disso, exercitar os cenários técnicos normais e adversos exigidos no P0. Resultados ainda não existem.

O enunciado do P0 foi escolhido como primeiro exemplo local. Isso não autoriza publicar seu conteúdo nem enviá-lo a provedor externo. Para testes e demonstrações públicas, preparar enunciados fictícios ou autorizados.

## Próxima sessão — 04/11/2026

1. Iniciar pela issue #1: contrato de entrada, exemplos fictícios e critérios de avaliação revisados com o aluno.
2. Preparar o fluxo local e testes offline pela issue #2.
3. Acompanhar liberação institucional. O aluno informou que ainda não está disponível e que a liberação será anunciada; relato não reconferido pelo assistente. Decidir eventual alternativa apenas quando necessária.
4. Integrar o LLM pela issue #3 quando houver acesso e interface confirmados; somente então validar o fluxo real e concluir o Básico.

Ver [organização do desenvolvimento](ORGANIZACAO.md) para o quadro, as dez issues e o fluxo de releases.

O aluno informou em 03/11/2026 que já realizou o registro inicial do repositório no Moodle. Informação fornecida pelo aluno, sem nova conferência da atividade pelo assistente.
