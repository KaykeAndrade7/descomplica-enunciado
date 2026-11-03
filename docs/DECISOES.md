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

## Escolhas operacionais do assistente

- Nome inicial do repositório: p0-checklist-enunciados; pode ser ajustado pelo aluno.
- Branch principal: main. Evolução em branches curtas com PRs.
- Preservar histórico real. Criar os marcos p0-basico, p0-intermediario e p0-avancado somente quando os respectivos estados existirem e forem verificados.
- Publicar documentação autoral. Materiais autenticados do curso permanecem na base local.

## Propostas técnicas ainda a fechar

- Separar entrada, configuração, preparação da solicitação, chamada ao LLM, validação e apresentação, sem abstrações desnecessárias.
- Verificar localmente se os trechos de apoio existem no texto de entrada. Isso não comprova a correção semântica da interpretação.
- Definir formato interno da resposta e comportamento quando a saída do modelo for inválida; não presumir suporte nativo a JSON.
- Definir limite de entrada e parâmetros após conhecer a interface institucional.
- Selecionar versão do Python e dependências após confirmar o acesso; não instalar dependências nesta etapa.

## Critérios e exemplos a detalhar antes dos testes

Verificar requisitos omitidos ou inventados, fidelidade das citações, separação entre recomendações e obrigações, datas explícitas e informações ausentes/ambíguas. Além disso, exercitar os cenários técnicos normais e adversos exigidos no P0. Resultados ainda não existem.

O enunciado do P0 foi escolhido como primeiro exemplo local. Isso não autoriza publicar seu conteúdo nem enviá-lo a provedor externo. Para testes e demonstrações públicas, preparar enunciados fictícios ou autorizados.

## Próxima sessão — 04/11/2026

1. Confirmar acesso ao LLM institucional: endereço, modelo, autenticação, interface e limites efetivamente disponíveis.
2. Fechar o desenho técnico mínimo e os critérios dos primeiros testes com o aluno.
3. Preparar ambiente Python e executar a menor chamada real com texto fictício.
4. Construir o fluxo básico, documentando execução e mantendo commits progressivos.

O registro inicial do repositório no Moodle permanece pendente de solicitação do aluno. Criar o repositório não realiza essa submissão.
